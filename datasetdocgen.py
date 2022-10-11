#!/usr/bin/env python3

from typing import Dict
import yaml
import click
import re
import os


@click.command()
@click.option('-o', '--output-dir', 'output_dir', type=str, nargs=1)
@click.argument('yaml_files', type=str, nargs=-1)
def main(output_dir, yaml_files):
    for yaml_file in yaml_files:
        with open(yaml_file, 'r') as fh:
            metadata = yaml.safe_load(fh)
        basename = yaml_file.removesuffix('-metadata.yaml')
        output_filename = basename + '.md'
        with open(os.path.join(output_dir, output_filename), 'w') as output:
            output.write(f'# {metadata["global"]["title"]}\n\n')
            output.write('## Dataset metadata\n\n')
            output.write(make_table(metadata['global']))
            output.write('## Variable metadata\n\n')
            for variable in metadata['local']:
                variable_source_filename = basename + '-' + variable + '.md'
                variable_source_path = os.path.join(
                    output_dir, variable_source_filename
                )
                output.write(f'## {variable}\n\n')
                var_metadata = metadata['local'][variable]
                output.write(
                    make_table(
                        var_metadata, source_link=variable_source_filename
                    )
                )
                if 'source' in var_metadata:
                    with open(variable_source_path, 'w') as fh:
                        fh.write(f'`{var_metadata["source"]}`\n')


def make_table(metadata: Dict[str, str], source_link: str = None) -> str:
    lines = ['| Field | Value |', '| ---- | ---- |']
    for field, raw_value in metadata.items():
        value = (
            f'[Click here for source.]({source_link})'
            if field == 'source' and source_link is not None
            else f'{escape_for_markdown(raw_value)}'
        )
        lines.append(f'| {escape_for_markdown(field)} | {value} |')
    return '\n'.join(lines) + '\n\n'


def escape_for_markdown(text: str) -> str:
    escaped_text = text.replace('\\', '\\\\').replace('_', '\\_')
    if re.match('https?://', text):
        return f'[{escaped_text}]({text})'
    elif re.match('www[.]', text):
        return f'[{escaped_text}](http://{text})'
    else:
        return escaped_text


if __name__ == '__main__':
    main()
