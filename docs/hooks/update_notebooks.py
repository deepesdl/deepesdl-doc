import shutil
from pathlib import Path


def on_pre_build(config):
    """
    Runs the updates once before the build of the documentation

    References:
    - mkdocs hooks: https://www.mkdocs.org/user-guide/configuration/?#hooks
    - mkdocs events: https://www.mkdocs.org/dev-guide/plugins/#on_pre_build

    Args:
     - config: global MkDocsConfig Object
    """
    source = Path.cwd() / "notebooks"
    destination = Path.cwd() / "docs/guide/jupyterlab/notebooks"

    _update_files_in_docs(source, destination)
    print(f"[hooks] Updated notebooks: {source} to {destination}")


def _update_files_in_docs(source: Path, destination: Path):
    """
    Adds notebooks to docs/notebooks

    Args:
        - source: Path to original notebooks
        - destination: Path to copy original notebooks to prepare for and add to
        mkdocs documentation
    """
    shutil.copytree(source,
                    destination,
                    dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns(
                        '2023_WCRP',
                        '20240612_nor_webinar_xcube',
                        'ISPRS-2024',
                        'README.md'
                    ))
