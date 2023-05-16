#!/usr/bin/env python

import math
import os
import pathlib
import re
import shutil
from functools import cached_property, partial
from typing import Any, Dict, Optional, List, Tuple, cast

from tenacity import retry, stop_after_attempt, wait_exponential
from xcube.core.store import new_data_store, DatasetDescriptor
import signal
import click


@click.group()
def main():
    pass


@main.command()
@click.option(
    '--max-datasets',
    metavar='N',
    type=int,
    default=None,
    help='maximum number of datasets to catalogue per data store',
)
@click.option(
    '--use-stock-map',
    is_flag=True,
    help='use very low-res stock map tiles instead of web tiles',
)
@click.option(
    '--stores',
    type=str,
    default=None,
    help='comma-separated IDs of stores to catalogue '
    '(if omitted, catalogue all stores)',
)
@click.option(
    '--suffixes',
    type=str,
    default=None,
    help='comma-separated list of data ID suffixes to include for s3 and file '
    'stores (if omitted, include all suffixes)',
)
@click.option(
    '--data-id-filter',
    type=str,
    default=None,
    help='only include datasets whose ID contains this string',
)
def catalogue(
    max_datasets: Optional[int] = None,
    use_stock_map: bool = False,
    stores: Optional[str] = None,
    suffixes: Optional[str] = None,
    data_id_filter: Optional[str] = None
):
    store_ids = None if stores is None else stores.split(',')
    data_suffixes = None if suffixes is None else suffixes.split(',')
    catalogue_ = Catalogue(
        dest_dir='catalogue',
        max_datasets=max_datasets,
        use_stock_map=use_stock_map,
        store_ids=store_ids,
        data_suffixes=data_suffixes,
        data_id_filter=data_id_filter
    )
    catalogue_.write_catalogue()


def _retry_failed(retry_state):
    print(f'Too many retries. {retry_state}')


def handler(signum, frame):
    raise Exception("timeout")


def _get_desc_with_timeout(store, data_id) -> Optional[DatasetDescriptor]:
    """ Get dataset description with a 60-second timeout

    Uses signals, so only works on POSIX systems.

    Args:
        store: an xcube data store
        data_id: ID of a dataset in the store

    Returns: a descriptor for the dataset, if the store returned this
        within the time limit; otherwise None

    """
    result = None
    signal.alarm(60)
    try:
        result = store.describe_data(data_id)
        print('describe_data returned')
    except Exception as e:
        if e.args == ('timeout', ):
            print('describe_data timed out')
        else:
            raise e
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, handler)
    return result


class Catalogue:
    def __init__(
        self,
        dest_dir: str,
        max_datasets: Optional[int] = None,
        use_stock_map: bool = False,
        store_ids: Optional[List[str]] = None,
        data_suffixes: Optional[List[str]] = None,
        data_id_filter: Optional[str] = None
    ):
        self.store_records = self.create_stores()
        self.dest_dir = pathlib.Path(dest_dir)
        self.max_datasets = max_datasets
        self.use_stock_map = use_stock_map
        self.store_ids = store_ids
        self.data_suffixes = (
            ('',)
            if data_suffixes is None
            else tuple(s.lower() for s in data_suffixes)
        )
        self.data_id_filter = '' if data_id_filter is None else data_id_filter
        self.map_manager = MapManager(
            image_dir=pathlib.Path(dest_dir, 'maps'),
            use_stock_map=use_stock_map,
        )

    @staticmethod
    def create_stores() -> Dict[str, 'StoreRecord']:
        max_depth = 8

        user_store = (
            [
                (
                    'user',
                    'User data (private)',
                    'user_store',
                    dict(
                        data_store_id="s3",
                        root=f"agriculture-vlab-user/"
                        f"{os.environ['JUPYTERHUB_USER']}/",
                        max_depth=max_depth,
                    ),
                )
            ]
            if 'JUPYTERHUB_USER' in os.environ
            else []
        )

        # noinspection PyTypeChecker
        store_definitions = (
            [
                (
                    'lab',
                    'Jupyter Lab filesystem',
                    'lab_store',
                    dict(data_store_id="file", root=str(pathlib.Path.home())),
                )
            ]
            + user_store
            + [
                (
                    'deepesdl',
                    'deepESDL',
                    'FIXME',
                    dict(
                        data_store_id="s3",
                        root="deep-esdl-public/",
                        max_depth=max_depth,
                    ),
                ),
                (
                    'scratch',
                    'Temporary data',
                    'scratch_store',
                    dict(
                        data_store_id="s3",
                        root="agriculture-vlab-scratch/",
                        max_depth=max_depth,
                    ),
                ),
                (
                    'test',
                    'AVL data (testing)',
                    'test_store',
                    dict(
                        data_store_id="s3",
                        root="agriculture-vlab-data-test/",
                        max_depth=max_depth,
                    ),
                ),
                (
                    'staging',
                    'AVL data (staging)',
                    'staging_store',
                    dict(
                        data_store_id="s3",
                        root="agriculture-vlab-data-staging/",
                        max_depth=max_depth,
                    ),
                ),
                (
                    'data',
                    'AVL data',
                    'data_store',
                    dict(
                        data_store_id="s3",
                        root="agriculture-vlab-data/",
                        max_depth=max_depth,
                    ),
                ),
                (
                    'public',
                    'User data (shared)',
                    'public_store_read',
                    dict(
                        data_store_id="s3",
                        root=f"agriculture-vlab-public/",
                        max_depth=max_depth,
                    ),
                ),
                (
                    'cds',
                    'Copernicus Climate Data Store data',
                    None,
                    dict(data_store_id='cds'),
                ),
                (
                    'cciodp',
                    'ESA Climate Change Initiative data (from ODP)',
                    None,
                    dict(data_store_id='cciodp'),
                ),
                (
                    'ccizarr',
                    'ESA Climate Change Initiative data (Zarr format)',
                    None,
                    dict(data_store_id='ccizarr'),
                ),
                (
                    'cmems',
                    'Copernicus Marine Environment Monitoring Service',
                    None,
                    dict(data_store_id='cmems'),
                ),
                (
                    'sentinelhub',
                    'SentinelHub',
                    None,
                    dict(data_store_id='sentinelhub'),
                ),
            ]
        )

        return {args[0]: StoreRecord(*args) for args in store_definitions}

    def write_catalogue(self):
        pathlib.Path.mkdir(self.dest_dir, parents=True, exist_ok=True)
        index_path = self.dest_dir / 'index.md'
        with open(index_path, 'w') as fh:
            fh.write(
                '# AVL Dataset catalogue\n\n## Data stores\n\n'
                'Click on a store name for more details.\n\n'
                '| Store name | Description |\n'
                '|------------|-------------|\n'
            )

            for store_id in self.store_records:
                if self.store_ids is None or store_id in self.store_ids:
                    fh.write(
                        f'| [{store_id}]({store_id}/index.md) | '
                        f'{self.store_records[store_id].desc} |\n'
                    )

                    self.write_catalogue_for_store(store_id)

    def write_catalogue_for_store(self, store_id: str):
        path = self.dest_dir / store_id
        pathlib.Path.mkdir(path, parents=True, exist_ok=True)
        data_ids = self.store_records[store_id].store.get_data_ids()
        data_store_id = \
            self.store_records[store_id].store_args['data_store_id']

        def filter_ids(ids):
            count = 0
            for id_ in ids:
                non_file_store = data_store_id not in ['s3', 'file']
                suffix_ok = id_.lower().endswith(self.data_suffixes)
                data_id_ok = re.search(self.data_id_filter, id_) is not None
                if (suffix_ok or non_file_store) and data_id_ok:
                    yield id_
                    count += 1
                if count == self.max_datasets:
                    return

        with open(path / 'index.md', 'w') as fh:
            # fh.write(f'# Data store: {store_id}\n\n')
            var_name = self.store_records[store_id].var_name
            fh.write(
                f'## Store variable name in JupyterLab: `{var_name}` &emsp;'
                f'{self._make_copy_button("variable name", var_name)}\n\n'
            )
            empty = True
            for data_id in filter_ids(data_ids):
                if empty:
                    fh.write('## Datasets in this store\n\n')
                    fh.write('Click on a dataset link for more details.\n\n')
                empty = False
                fh.write(
                    f'[{data_id}]({self.data_id_to_filename(data_id)})<br>\n'
                )
                self.write_catalogue_for_dataset(store_id, data_id)
            if empty:
                fh.write('## There are no datasets available in this store.')

    @retry(stop=stop_after_attempt(2),
           wait=wait_exponential(multiplier=1, min=30, max=120),
           retry_error_callback=_retry_failed)
    def write_catalogue_for_dataset(self, store_id: str, data_id: str):
        basename = self.data_id_to_filename(data_id)
        path = self.dest_dir / store_id / basename
        print('Fetching:', store_id, data_id)
        store_record = self.store_records[store_id]
        store = store_record.store
        # fsspec is not fork-safe so we skip the timeout for s3;
        # timeout should in any case only be needed for CCI, CDS, CMEMS,
        # and SH.
        desc = (
            store.describe_data(data_id)
            if store_record.store_args['data_store_id'] == 's3'
            else _get_desc_with_timeout(store, data_id)
        )
        if desc is None:
            return
        assert isinstance(desc, DatasetDescriptor)
        desc = cast(DatasetDescriptor, desc)
        title = (
            desc.attrs.get('title', data_id)
            if hasattr(desc, 'attrs') and isinstance(desc.attrs, dict)
            else data_id
        )
        with open(str(path) + '.md', 'w') as fh:
            # It would be safer also to Markdown-escape the title, but
            # if we do that then MkDocs shows the ugly, escaped form in
            # the navigation bar at the top.
            fh.write(
                f'# {title}\n\n'
                # f'**Dataset identifier:** '
                # f'{self.escape_for_markdown(data_id)}<br>\n'
                # f'**Data store:** {store_id}<br>\n'
            )
            # TODO: link to open in viewer?
            open_command = store_record.get_code_snippet(data_id)
            # fh.write(
            #     f'## How to open this dataset in AVL JupyterLab '
            #     f'&emsp;{self._make_copy_button("code", open_command)}\n'
            #     f'```python\n{open_command}\n```\n\n'
            # )
            valid_attrs = hasattr(desc, 'attrs') and isinstance(
                desc.attrs, dict
            )

            if 'SMOS' in data_id:
                bbox = (-180, 0, 180, 85)
            elif hasattr(desc, 'bbox') and desc.bbox is not None:
                bbox = desc.bbox
            elif valid_attrs:
                bbox = (
                    desc.attrs.get('geospatial_lon_min', -180),
                    desc.attrs.get('geospatial_lat_min', -90),
                    desc.attrs.get('geospatial_lon_max', 180),
                    desc.attrs.get('geospatial_lat_max', 90),
                )
            else:
                bbox = (-180, -90, 180, 90)

            if self._is_bbox_valid(bbox):
                self.map_manager.write_map(
                    bbox, self.dest_dir / store_id / (basename + '.png')
                )
                fh.write(
                    f'## Bounding box map\n\n'
                    f'![Bounding box map]({basename + ".png"})<br>\n'
                    '<span style="font-size: x-small">Map tiles and data from '
                    '<a href="http://openstreetmap.org">OpenStreetMap</a>,'
                    ' under '
                    '<a href="http://www.openstreetmap.org/copyright">'
                    'the ODbL</a>.</span>\n\n'
                )
            if valid_attrs:
                fh.write('## Basic information\n\n')
                fh.write(self.dataset_desc_to_markdown(desc, bbox))
            fh.write(
                '## Variable list\n\nClick on a variable name to jump to the '
                'variable’s full metadata.\n\n'
            )
            if isinstance(desc.data_vars, dict):
                fh.write(self.variables_to_markdown(desc.data_vars))
                fh.write('## Full variable metadata\n\n')
                for var_name, variable in desc.data_vars.items():
                    fh.write(f'### <a name="{var_name}"></a>{var_name}\n\n')
                    if hasattr(variable, 'attrs') and isinstance(
                        variable.attrs, dict
                    ):
                        fh.write(self.make_table(variable.attrs))

            if valid_attrs:
                fh.write(
                    '## <a name="full-metadata"></a>Full dataset metadata\n\n'
                )
                fh.write(self.make_table(desc.attrs))

    @staticmethod
    def _make_copy_button(description, content):
        html_snippet = (
            '<button id="copybutton"'
            f'title="Copy the {description} to the clipboard">⧉</button>'
            '<script>copybutton.addEventListener("pointerdown",'
            f'() =\\> navigator.clipboard.writeText("{content}"))'
            '</script>'
        )
        return html_snippet

    @staticmethod
    def _is_bbox_valid(bbox: Tuple[float, float, float, float]) -> bool:
        """
        Checks whether an object is a valid representation of a bounding
        box in degrees. This should catch cases where a bbox is given in
        an undeclared non-WGS84 CRS.

        Args:
            bbox: a bounding box

        Returns: True if and only if the bbox is a 4-tuple of valid longitude
        and latitude values in degrees
        """

        print(bbox)
        bbox = tuple(map(partial(round, ndigits=4), bbox))
        if not isinstance(bbox, tuple):
            return False
        if len(bbox) != 4:
            return False
        return (
            -180 <= bbox[0] <= 180
            and -90 <= bbox[1] <= 90
            and -180 <= bbox[2] <= 180
            and -90 <= bbox[3] <= 90
        )

    @staticmethod
    def data_id_to_filename(data_id: str):
        return re.sub('[/.:]', '-', data_id)

    @staticmethod
    def dataset_desc_to_markdown(
        desc: DatasetDescriptor, bbox: Tuple[float, float, float, float]
    ) -> str:
        """Create a brief summary from a dataset description and bounding box

        Args:
            desc: dataset descriptor
            bbox: bounding box

        Returns:
            Markdown source containing information about the dataset
        """

        def row_if_attr(title, keys: list):
            # Return table row only if one of the keys is present in attrs.
            for key in keys:
                if key in desc.attrs:
                    return f'| {title} | {desc.attrs[key]} |\n'
            return ''

        return (
            f'| Parameter | Value |\n'
            f'| ---- | ---- |\n'
            f'| Bounding box longitude (°) | {bbox[0]} to {bbox[2]} |\n'
            f'| Bounding box latitude (°) | {bbox[1]} to {bbox[3]} |\n'
            + (
                f'| Time range | {desc.time_range[0]} to '
                f'{desc.time_range[1] or "present"} |\n'
                if desc.time_range
                else ''
            )
            + (
                f'| Time period | {desc.time_period} |\n'
                if desc.time_period
                else ''
            )
            + row_if_attr('Publisher', ['publisher', 'publisher_name'])
            + f'\n'
            '[Click here for full dataset metadata.](#full-metadata)\n\n'
        )

    def variables_to_markdown(self, variables: Dict[str, Any]) -> str:
        """Create table with brief information about the variables in a dataset

        Args:
            variables: a list of dictionaries of variable properties

        Returns:
            Markdown source for a table summarizing the variables

        """
        assert variables is not None
        lines = ['| Variable | Long name | Units |', '| ---- | ---- | ---- |']
        for varname, variable in variables.items():
            if varname == 'crs':
                continue
            attrs = (
                variable.attrs
                if hasattr(variable, 'attrs')
                and isinstance(variable.attrs, dict)
                else {}
            )
            long_name = self.escape_for_markdown(
                attrs.get('long_name', '[none]')
            )
            name = self.escape_for_markdown(varname)
            units = self.escape_for_markdown(attrs.get('units', '[none]'))
            lines.append(f'| [{name}](#{name}) | {long_name} | {units} |')
        return '\n'.join(lines) + '\n\n'

    def make_table(self, data: Dict[str, Any], source_link: str = None) -> str:
        """Create a Markdown table showing the entries in a dictionary

        Args:
            data: the data to be displayed
            source_link: if supplied and if a `source` key is present, the
                value for "source" in the table will be replaced with a
                Markdown link to this location.

        Returns:
            Markdown source for a table
        """
        lines = ['| Field | Value |', '| ---- | ---- |']
        for field, raw_value in data.items():
            value = (
                f'[Click here for source.]({source_link})'
                if field == 'source' and source_link is not None
                else f'{self.escape_for_markdown(raw_value)}'
            )
            lines.append(f'| {self.escape_for_markdown(field)} | {value} |')
        return '\n'.join(lines) + '\n\n'

    @staticmethod
    def escape_for_markdown(content: Any) -> str:
        """Turn any value into a Markdown source string

        For a string, characters which have special meaning in Markdown will
        be escaped to ensure that they display correctly. Additionally, if the
        string begins with "http://", "https://", or "www." it will be turned
        into a Markdown link.

        For a dictionary or list, each element will be processed recursively
        with another call to this function, and they will be joined into a
        single string with ", " and/or ": " as separators.

        Any other type will be turned into a string with the ``str`` function
        and processed as a string.

        Args:
            content: anything

        Returns:
            a correctly escaped Markdown representation of the input
        """

        if type(content) == list:
            return ', '.join(map(Catalogue.escape_for_markdown, content))
        elif type(content) == dict:
            return ', '.join(
                Catalogue.escape_for_markdown(k)
                + ': '
                + Catalogue.escape_for_markdown(v)
                for k, v in content.items()
            )
        elif type(content) == str:
            escaped_text = (
                re.sub(
                    r'\n+',
                    r' ',
                    re.sub(r'[][({`*_#+.!})\\-]', r'\\\g<0>', content),
                )
                .replace('<', '&lt;')
                .replace('>', '&gt;')
            )
            if re.match('https?://[^ ]+$', content):
                return f'[{escaped_text}]({content})'
            elif re.match('www[.][^ ]+$', content):
                return f'[{escaped_text}](http://{content})'
            else:
                return escaped_text
        else:
            return Catalogue.escape_for_markdown(str(content))


class StoreRecord:
    """Creates and wraps a store with some catalogue-relevant metadata"""

    def __init__(
        self, store_id: str, desc: str, var_name: str, store_args: dict
    ):
        """Initialize a store record

        Args:
            store_id: store identifier to use in the catalogue
            desc: human-readable description of the store
            var_name: name of pre-initialized store variable in JupyterLab
            store_args: passed directly to `new_data_store`
        """

        self.store_id = store_id
        self.desc = desc
        self.var_name = var_name
        self.store_args = store_args

    @cached_property
    def store(self):
        return new_data_store(**self.store_args)

    @staticmethod
    def _make_param_template(schema):
        snippet = ''
        for param in schema.required:
            snippet += ', '
            snippet += f'{param}='
            param_type = schema.properties[param].type
            if param_type == 'array' or 'array' in param_type:
                snippet += '[?]'
            else:
                snippet += '?'
        return snippet

    def get_code_snippet(self, data_id):
        snippet = ''
        if self.var_name is None:
            var_name = f"{self.store_id}_store"
            store_schema = self.store.get_data_store_params_schema()
            snippet = (
                f"{var_name} = new_data_store("
                f"'{self.store_id + self._make_param_template(store_schema)}'"
                f")\n"
            )
        else:
            var_name = self.var_name
        ds_schema = self.store.get_open_data_params_schema(data_id=data_id)
        snippet += (
            f"ds = {var_name}.open_data("
            f"'{data_id + self._make_param_template(ds_schema)}')"
        )
        return snippet


class MapManager:
    """Creates and manages map images, re-using them where possible

    Creating a bounding box map is slow and many datasets have identical
    bounding boxes, so this class is used to make sure that identical bounding
    box maps are not re-rendered unnecessarily.
    """

    def __init__(self, image_dir: pathlib.Path, use_stock_map: bool = False):
        # TODO create a temporary directory if image directory not specified
        self.image_dir: pathlib.Path = image_dir
        self.use_stock_map = use_stock_map
        image_dir.mkdir(parents=True, exist_ok=True)

    def write_map(
        self,
        bbox: Tuple[float, float, float, float],
        destination: pathlib.Path,
    ) -> None:
        """Return a path to a map representing a specified bounding box

        The map will be created if necessary.

        Args:
            bbox: a bounding box in WGS84 degrees
            destination: path to which to write the map
        """

        # Round bbox values to 4 d.p., which is sufficient precision,
        # keeps the filename length reasonable, and allows reuse of
        # identical-looking bbox maps even if the actual values are not
        # identical.
        basename = '_'.join(map(lambda x: f'{x:.4f}', bbox)) + '.png'
        path = self.image_dir / basename
        if not path.exists():
            self.make_map(bbox, path.as_posix())
        shutil.copy2(path, destination)

    def make_map(
        self, bbox: Tuple[float, float, float, float], output_path: str
    ) -> None:
        """Create a bounding box map

        The map shows the bounding box at the centre of a map covering a
        larger area.

        Args:
            bbox: bounding box to represent
            output_path: the path to which to write the map. The output format
                is determined by the file extension of this path.
        """

        import cartopy.io.img_tiles
        import matplotlib.patches as patches
        from matplotlib.backends.backend_agg import \
            FigureCanvasAgg as FigureCanvas
        from matplotlib.figure import Figure

        # We round bounding box values because it sometimes breaks for
        # very-nearly-round values, e.g. (-180, -60, 179.99999999, 80.0).
        # 4 d.p. corresponds to ~10m resolution, which should be enough
        # for any of our datasets.
        x0, y0, x1, y1 = tuple(map(partial(round, ndigits=4), bbox))
        w = x1 - x0
        h = y1 - y0

        # Above a certain size, we switch from a regional LAEA projection to
        # a global Mollweide projection.
        large = w > 45 or h > 45

        margin_factor = 0.4  # how much margin to include around the bbox
        # image_tiles = cartopy.io.img_tiles.Stamen('terrain-background')
        image_tiles = cartopy.io.img_tiles.OSM()
        fig = Figure()
        FigureCanvas(fig)
        projection = (
            cartopy.crs.Mollweide(central_longitude=(x0 + x1) / 2)
            if large
            else cartopy.crs.LambertAzimuthalEqualArea(
                (x0 + x1) / 2,
                (y0 + y1) / 2
                # centre the projection over our bbox
            )
        )
        ax = fig.add_subplot(111, projection=projection)
        if large:
            ax.set_global()
        else:
            ax.set_extent(
                [
                    x0 - margin_factor * w,
                    x1 + margin_factor * w,
                    y0 - margin_factor * h,
                    y1 + margin_factor * h,
                ],
                crs=cartopy.crs.Geodetic(),
            )

        # We use a fairly crude calculation to choose the tile resolution;
        # ideally we should take the pixel dimensions of the final image
        # into account here as well as the geographical bounding box size.
        max_dim_deg = max(w, h)
        if max_dim_deg > 45:
            max_dim_deg = 360
        zoom_level = min(12, int(math.log2(360 / max_dim_deg)))
        if self.use_stock_map or large:
            # Stock imagery is low-res but fast, so we use it for large areas
            # or when explicitly requested.
            ax.stock_img()
        else:
            ax.add_image(image_tiles, zoom_level)

        bbox_rect_patch = patches.Rectangle((x0, y0), w, h)
        # Since projected rectangle sides may not be straight, we interpolate
        # them into many short line segments which can be projected
        # separately. In some cases cartopy can do this automatically,
        # but it doesn't seem to work for our projection and parameters (as
        # of cartopy 0.21.0), so we use the manual approach.
        bbox_path_patch = patches.PathPatch(
            bbox_rect_patch.get_path()
            .transformed(bbox_rect_patch.get_patch_transform())
            .interpolated(100),
            linewidth=2,
            edgecolor='red',
            facecolor='none',
            transform=cartopy.crs.Geodetic(),
            zorder=1e6,  # on top
        )
        ax.add_patch(bbox_path_patch)
        ax.gridlines(draw_labels=not large, color='white')
        fig.tight_layout(pad=0)
        print('*' + output_path)
        fig.savefig(output_path, bbox_inches='tight', pad_inches=0.1)


if __name__ == '__main__':
    main()
