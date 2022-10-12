#!/usr/bin/env python3

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
@click.argument('json_files', type=str, nargs=-1)
def main(output_dir, json_files):
    for yaml_file in json_files:
        with open(yaml_file, 'r') as fh:
            metadata = yaml.safe_load(fh)
        basename = yaml_file.removesuffix('.geojson')
        output_filename = basename + '.md'
        bbox_image_path = os.path.join(output_dir, basename + '.png')
        with open(os.path.join(output_dir, output_filename), 'w') as output:
            props = metadata['properties']
            output.write(f'# {props["title"]}\n\n')
            output.write('## Basic information\n\n')
            output.write(f'![Bounding box map]({basename + ".png"})\n\n')
            output.write(make_basic_info(props))
            output.write('## Variable list\n\n')
            output.write(make_variable_list_table(props['variables']))
            output.write('## Full variable metadata\n\n')
            for variable in props['variables']:
                variable_source_filename = \
                    basename + '-' + variable['name'] + '.md'
                variable_source_path = os.path.join(
                    output_dir, variable_source_filename
                )
                output.write(f'### <a name="{variable["name"]}"></a>'
                             f'{variable["long_name"]}\n\n')
                output.write(
                    make_table(
                        variable, source_link=variable_source_filename
                    )
                )
                if 'source' in variable:
                    with open(variable_source_path, 'w') as fh:
                        fh.write(f'`{variable["source"]}`\n')
            output.write('## <a name="full-metadata"></a>'
                         'Full dataset metadata\n\n')
            output.write(make_table({k: v for k, v in props.items()
                                     if k != 'variables'}))
        make_map(props, bbox_image_path)


def make_basic_info(props: Dict[str, Any]) -> str:
    lines = []
    lines.append(f'| Parameter | Minimum | Maximum |')
    lines.append(f'| ---- | ---- | ---- |')
    lines.append(f'| Bounding box latitude | {props["geospatial_lat_min"]} | '
                 f'{props["geospatial_lat_max"]} |')
    lines.append(f'| Bounding box longitude | {props["geospatial_lon_min"]} | '
                 f'{props["geospatial_lon_max"]} |')
    lines.append(f'| Time range | {props["time_coverage_start"]} | '
                 f'{props["time_coverage_end"]} |')
    lines.append(f'\nPublisher: {props["publisher_name"]}\n')
    lines.append('[Click here for full dataset metadata.](#full-metadata)')
    return '\n'.join(lines) + '\n\n'


def make_variable_list_table(variables: List[Dict[str, Any]]) -> str:
    lines = ['| Variable | Identifier | Units |', '| ---- | ---- | ---- |']
    for variable in variables:
        long_name = escape_for_markdown(variable.get('long_name', '[none]'))
        name = escape_for_markdown(variable.get('name', '[none]'))
        units = escape_for_markdown(variable.get('units', '[none]'))
        lines.append(f'| [{long_name}](#{name}) | {name} | {units} |')
    return '\n'.join(lines) + '\n\n'


def make_table(metadata: Dict[str, Any], source_link: str = None) -> str:
    lines = ['| Field | Value |', '| ---- | ---- |']
    for field, raw_value in metadata.items():
        value = (
            f'[Click here for source.]({source_link})'
            if field == 'source' and source_link is not None
            else f'{escape_for_markdown(raw_value)}'
        )
        lines.append(f'| {escape_for_markdown(field)} | {value} |')
    return '\n'.join(lines) + '\n\n'


def escape_for_markdown(content: Any) -> Any:
    if type(content) != str:
        return content
    escaped_text = content.replace('\\', '\\\\').replace('_', '\\_')
    if re.match('https?://', content):
        return f'[{escaped_text}]({content})'
    elif re.match('www[.]', content):
        return f'[{escaped_text}](http://{content})'
    else:
        return escaped_text


def make_map(props: Dict[str, Any], output_path):
    x0 = props['geospatial_lon_min']
    x1 = props['geospatial_lon_max']
    y0 = props['geospatial_lat_min']
    y1 = props['geospatial_lat_max']
    w = x1 - x0
    h = y1 - y0
    margin_factor = 0.2
    tiles = cartopy.io.img_tiles.Stamen('terrain-background')
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection=tiles.crs)
    ax.set_extent([x0 - margin_factor * w, x1 + margin_factor * w,
                   y0 - margin_factor * h, y1 + margin_factor * h],
                  crs=cartopy.crs.Geodetic())
    ax.add_image(tiles, 6)
    rect = patches.Rectangle((x0, y0), w, h, linewidth=1,
                             edgecolor='r', facecolor='none',
                             transform=cartopy.crs.Geodetic())
    ax.add_patch(rect)
    plt.tight_layout(pad=0)
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0.1)


if __name__ == '__main__':
    main()
