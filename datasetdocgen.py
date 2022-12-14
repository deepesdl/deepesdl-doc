#!/usr/bin/env python3

"""Generate description in Markdown and map image for a dataset from geojson"""

from typing import Dict, Any, List
import yaml
import click
import re
import os
import matplotlib.pyplot as plt

import cartopy
import cartopy.io.img_tiles
import matplotlib.patches as patches


@click.command()
@click.option('-o', '--output-dir', 'output_dir', type=str, nargs=1)
@click.option('-n', '--name', 'name', type=str, nargs=1)
@click.argument('json_files', type=str, nargs=-1)
def main(output_dir, name, json_files):
    for json_file in json_files:
        with open(json_file, 'r') as fh:
            metadata = yaml.safe_load(fh)
        basename = (
            name
            if name is not None
            else os.path.basename(json_file).removesuffix('.geojson')
        )
        output_filename = basename + '.md'
        bbox_image_path = os.path.join(output_dir, basename + '.png')
        with open(os.path.join(output_dir, output_filename), 'w') as output:
            props = metadata['properties']
            output.write(f'# {props["title"]}\n\n')
            output.write('## Basic information\n\n')
            output.write(f'![Bounding box map]({basename + ".png"})<br>\n')
            output.write(
                '<span style="font-size: x-small">Map tiles by <a href="http://stamen.com">'
                'Stamen Design</a>, under '
                '<a href="http://creativecommons.org/licenses/by/3.0">'
                'CC BY 3.0</a>. Data by '
                '<a href="http://openstreetmap.org">OpenStreetMap</a>,'
                ' under '
                '<a href="http://www.openstreetmap.org/copyright">'
                'ODbL</a>.</span>\n\n'
            )
            output.write(make_basic_info(props))
            output.write('## Variable list\n\n')
            output.write(make_variable_list_table(props['variables']))
            output.write('## Full variable metadata\n\n')
            for variable in props['variables']:
                variable_source_filename = (
                    basename + '-' + variable['name'] + '.md'
                )
                variable_source_path = os.path.join(
                    output_dir, variable_source_filename
                )
                output.write(
                    f'### <a name="{variable["name"]}"></a>'
                    f'{variable["long_name"]}\n\n'
                )
                output.write(
                    make_table(variable, source_link=variable_source_filename)
                )
                if 'source' in variable:
                    with open(variable_source_path, 'w') as fh:
                        fh.write(f'`{variable["source"]}`\n')
            output.write(
                '## <a name="full-metadata"></a>' 'Full dataset metadata\n\n'
            )
            output.write(
                make_table(
                    {k: v for k, v in props.items() if k != 'variables'}
                )
            )
        make_map(props, bbox_image_path)


def make_basic_info(props: Dict[str, Any]) -> str:
    """Create a brief summary from a dictionary of dataset properties.

    Args:
        props: dictionary of dataset properties

    Returns:
        Markdown source containing information about the dataset
    """
    return (
        f'| Parameter | Value |\n'
        f'| ---- | ---- |\n'
        f'| Bounding box latitude | {props["geospatial_lat_min"]} to '
        f'{props["geospatial_lat_max"]} |\n'
        f'| Bounding box longitude | {props["geospatial_lon_min"]} to '
        f'{props["geospatial_lon_max"]} |\n'
        f'| Time range | {props["time_coverage_start"]} to '
        f'{props["time_coverage_end"]} |\n' +
        (f'| Time period | {props["time_period"]} |\n'
         if 'time_period' in props else '') +
        f'| Publisher | {props["publisher_name"]} |\n\n'
        '[Click here for full dataset metadata.](#full-metadata)\n\n'
    )


def make_variable_list_table(variables: List[Dict[str, Any]]) -> str:
    """Create a table with brief information about the variables in a dataset

    Args:
        variables: a list of dictionaries of variable properties

    Returns:
        Markdown source for a table summarizing the variables

    """
    lines = ['| Variable | Identifier | Units |', '| ---- | ---- | ---- |']
    for variable in variables:
        long_name = escape_for_markdown(variable.get('long_name', '[none]'))
        name = escape_for_markdown(variable.get('name', '[none]'))
        units = escape_for_markdown(variable.get('units', '[none]'))
        lines.append(f'| [{long_name}](#{name}) | {name} | {units} |')
    return '\n'.join(lines) + '\n\n'


def make_table(data: Dict[str, Any], source_link: str = None) -> str:
    """Create a table showing the entries in a dictionary

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
            else f'{escape_for_markdown(raw_value)}'
        )
        lines.append(f'| {escape_for_markdown(field)} | {value} |')
    return '\n'.join(lines) + '\n\n'


def escape_for_markdown(content: Any) -> Any:
    """Turn a string or list into a Markdown source string

    For a string, characters which have special meaning in Markdown will
    be escaped to ensure that they display correctly. Additionally, if the
    string begins with "http://", "https://", or "www." it will be turned into
    a Markdown link.

    For a list, each element will be processed recursively with another call
    to this function, and they will be joined into a single string with ", "
    as separator.

    For any other type, the output is the same as the input.

    Args:
        content: anything

    Returns:
        For strings and lists: Markdown source which will produce a
        representation of the input. For any other type: the input value.
    """
    if type(content) == list:
        return ', '.join(map(escape_for_markdown, content))
    elif type(content) == str:
        escaped_text = re.sub(r'[][({`*_#+.!})\\-]', r'\\\g<0>', content)
        if re.match('https?://', content):
            return f'[{escaped_text}]({content})'
        elif re.match('www[.]', content):
            return f'[{escaped_text}](http://{content})'
        else:
            return escaped_text
    else:
        return content


def make_map(props: Dict[str, Any], output_path: str) -> None:
    """Create a bounding box map from a dataset's properties

    The map shows the dataset's bounding box at the centre of a map covering a
    larger area.

    Args:
        props: property dictionary for a dataset
        output_path: the path to which to write the map. The output format
            is determined by the file extension of this path.
    """
    x0 = props['geospatial_lon_min']
    x1 = props['geospatial_lon_max']
    y0 = props['geospatial_lat_min']
    y1 = props['geospatial_lat_max']
    w = x1 - x0
    h = y1 - y0

    # Above a certain size, we switch from a regional LAEA projection to
    # a global Mollweide projection.
    large = w > 45 or h > 45

    margin_factor = 0.2  # how much margin to include around the bbox
    image_tiles = cartopy.io.img_tiles.Stamen('terrain-background')
    plt.figure()
    projection = (
        cartopy.crs.Mollweide(central_longitude=(x0 + x1) / 2)
        if large
        else cartopy.crs.LambertAzimuthalEqualArea(
            (x0 + x1) / 2,
            (y0 + y1) / 2
            # centre the projection over our bbox
        )
    )
    ax = plt.axes(projection=projection)
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

    # We use a crude test to choose the tile resolution; ideally we should
    # calculate this more carefully from the bbox size and final image
    # resolution.
    ax.add_image(image_tiles, 3 if large else 6)

    bbox_rect_patch = patches.Rectangle((x0, y0), w, h)
    # Since projected rectangle sides may not be straight, we interpolate
    # them into many short line segments which can be projected separately. In
    # some cases cartopy can do this automatically, but it doesn't seem to work
    # for our projection and parameters (as of cartopy 0.21.0), so we use the
    # manual approach.
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
    plt.tight_layout(pad=0)
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0.1)


if __name__ == '__main__':
    main()
