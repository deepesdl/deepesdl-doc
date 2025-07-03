[![Documentation Status](https://readthedocs.org/projects/deepesdl/badge/?version=latest)](https://deepesdl.readthedocs.io/en/latest/?badge=latest)

# DeepESDL documentation

This repository contains the source files for the DeepESDL documentation.

The current [DeepESDL Documentation](https://earthsystemdatalab.net/).

## To contribute to the new DeepESDL Documentation:
1. Create new branch based on `main` branch. This is your working branch.
2. Add your new content to the dedicated Markdown file. Please make sure, that
   1. you save images in the folder you're working in,
      path: `{folder-name-of-chapter}/img/xxxx.png`
   2. test your changes locally (see info below)
3. When done, create a Pull Request to merge your contributions into `main`. 
   A Brockmann Consult team member will review the changes.
4. Once merged, a Brockmann Consult team member will delete the branch.


Check the Material for mkdocs 
[documentation](https://squidfunk.github.io/mkdocs-material/setup/) for 
further layout information.

## Building the docs
If you want to run the documentation locally to test your changes:

1. create a python environment with environment_doc.yml   
   `$ conda env create -f environment_doc.yml`
2. run documentation locally: `$ mkdocs serve`



## Building the docs for the legacy documentation (please don't use)

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
