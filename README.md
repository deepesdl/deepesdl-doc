[![Documentation Status](https://readthedocs.org/projects/deepesdl/badge/?version=latest)](https://deepesdl.readthedocs.io/en/latest/?badge=latest)

# DeepESDL documentation

This repository contains the source files for the DeepESDL documentation.


## Building the docs

    $ conda install -c conda-forge mkdocs mkapi

## How to generate the documentation from a cube

To generate the overview pages for a datacube, you need to install the 
conda environment specified in environment.yml .

For the deep-esdl public bucket, you need to run 

    $ ./datasetdocgen2.py catalogue --stores deepesdl

It will create a new subfolder called cataloge/deepesdl. Move the files 
that you want to the actual directory docs/datasets. Please make sure, that 
the information is fetched correctly and that the map of coverage 
corresponds to your dataset. 