# DeepESDL example notebooks

This directory contains example notebooks which are also available in [DeepESDL 
Catalog](https://deepesdl.readthedocs.io/en/latest/guide/jupyterlab/#getting-started-notebooks).
Both sources must be kept in sync manually.

## Adding new example notebooks to DeepESDL Catalog

To add new notebooks to the DeepESDL Catalog or modify existing ones, you 
need to be part of the DeepESDL admin team. 
The DeepESDL admin team can add update notebooks via the Terminal in their 
DeepESDL Workspace. The getting started example notebooks are stored in 
`~/.shared/deepesdl/notebooks/1_getting-started/` , please follow some naming 
convention when adding new notebooks: 
1. Add the next higher integer as a prefix to your notebook. 
2. Separate words by underscores. Please choose a notebook path name which 
   will also work as a title, as the notebook pathname will be used as the 
   title displayed in the catalog. I.e. 01_Access_public_cubes.ipynb is 
   resolved into "01 Access public cubes" in the catalog overview.

**Please make sure not to publish any Credentials in the notebooks, so make 
sure to always hit save before uploading them to GitHub or to the catalog, 
making sure you will publish the state of the notebook which you currently 
see.** 

If you want to add any other notebooks, which should appear towards the end 
of the catalog, add a new subfolder to the `~/.shared/deepesdl/notebooks/`
with an integer as prefix, and add there any further specified notebooks. 