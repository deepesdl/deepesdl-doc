# User guide

This user guide helps you getting started with the main components of 
DeepESDL.

There are three components of DeepESDL: 
1. [DeepESDL JupyterLab](#deepesdl-jupyterlab)
2. [DeepESDL xcube viewer](#deepesdl-xcube-viewer)
3. [DeepESDL datacubes](#deepesdl-datacube-resources)


# DeepESDL JupyterLab

## Basic usage

This section provides a brief introduction for users to the basic features of
the JupyterLab environment as deployed on the DeepESDL system. 
For more in-depth documentation on the various components, see the links in the
section [Further Information](#further-information).

### Logging in and starting the JupyterLab profile

To use the DeepESDL JupyterLab environment, navigate to
<https://deep.earthsystemdatalab.net/> with a web browser (a recent version of
Firefox, Chrome, or Safari is recommended).

DeepESDL uses a GitHub to authenticate, so if you are already registered as a 
DeepESDL user, please use your GitHub account to log in. 
If your Jupyter server is not already running, you may be presented
with a menu of user JupyterLab profiles to use for your session; there might be 
one or more JupyterLab profiles to choose from, depending on the computational 
resources needs of your team. Please select a suitable profile for 
your current task; it might not always require the strongest computational 
resources available.
After choosing your environment, you will see a progress bar appear for a few 
seconds while it is started for you. 
The JupyterLab interface will then appear in your web browser, ready for
use.


### Choosing a JupyterLab profile

If you don't already have a running DeepESDL Jupyter session, you will be 
presented with a list of one or more available user JupyterLab profiles when 
you log in. 
A user JupyterLab profiles provides a particular combination of pre-installed 
package versions and resource settings. 

If you have already started your session and need to change JupyterLab profiles, 
you can do this by selecting *Hub control panel* from the *File* menu within
JupyterLab. Then click the ‘Stop my server’ button and wait for your current
server to shut down. When the ‘Start my server’ button appears, you can click
on it to return to the user JupyterLab profiles menu.

### Logging out

To log out, select ‘Log out’ from the ‘File’ menu within JupyterLab. 

Note that your JupyterLab session will continue in the background even after
you have logged out, but will eventually be terminated due to inactivity. 
If you wish to stop your session explicitly,
you can use the hub control panel as described in the 
[Choosing a JupyterLab profile](#choosing-a-jupyterlab-profile) section above.



# DeepESDL xcube viewer

The DeepESDL xcube viewer is reachable via 
https://viewer.earthsystemdatalab.net/ .

![img.png](../img/xcube-viewer.png)

The viewer currently shows public datasets, and later will allow to see 
team/user cubes when logged in. The login will be via GitHub as for the DeepESDL
JupyterLab. 

For the functionality of the viewer, please refer to the documentation:
https://xcube.readthedocs.io/en/latest/viewer.html#functionality


# DeepESDL datacubes

DeepESDL provides a growing list of relevant variables for Earth System Science. 
Most of them have been derived from Earth Observation, but the compilation also 
includes model or re-analysis data if deemed useful.
DeepESDL is very grateful to all data owners for kindly providing the data sets 
free of charge. They come without any warranty, neither from the owners, 
the DeepESDL team or ESA.

At ingestion into the DeepESDL, all data sets are transformed in space and time 
to fit to the common grid of the data cube, a process that necessarily modifies 
the original. If you are looking for the original data, please follow the links 
within the dataset attributes for each variable and contact the data owners.

To access the documentation of available datasets, please have a look in the 
[datasets section](../datasets/datasets.md).


## Further information

 - The [JupyterLab documentation](https://jupyterlab.readthedocs.io/):
   an in-depth user guide for the JupyterLab interface.
 - [How to Use JupyterLab](https://www.youtube.com/watch?v=A5YyoCKxEOU):
   a short introductory video tutorial.
 - [Markdown cells](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html),
   a guide to writing Markdown in Jupyter notebooks.
 - The [xcube documentation](https://xcube.readthedocs.io/): user
   guide and API reference for the xcube libraries.
