# DeepESDL xcube Viewer

The DeepESDL xcube Viewer is reachable at [viewer.earthsystemdatalab.net](https://viewer.earthsystemdatalab.net).

![img.png](../img/xcube-viewer.png)

The viewer contains public datasets only, but will later also provide user/team 
cubes when logged in. The login will be the same as for the DeepESDL JupyterLab.

For a more detailed description of the viewer functionality, please refer to a dedicated section in the
[xcube viewer documentation](https://xcube-dev.github.io/xcube-viewer).



## Publish a dataset in a public DeepESDL Viewer

In order to publish a data cube in a public DeepESDL Viewer take the following steps:

* Check if the data cube is ready for publication with the following tools

     * **[xrlint](https://bcdev.github.io/xrlint/):** A tool to validate `xrarray.Dataset` with a set of recommended rules 
     * **xcube Viewer extension:** in the JuypterLab use the dedicated Jupyter Notebook to test the representation of
       the data cube in the Viewer (see `Visualize_data_with_xcube_viewer.ipynb`)

* Store the data cube in team storage on S3 
  
    * for more information see `Upload_files_to_shared_team_s3_storage.ipynb`

* For the publication contact the DeepESDL team (`esdl-support@brockmann-consult.de`) and communicate whether 

    * the data cube should be published in the Viewer and stored in a public DeepESDL bucket, or
    * the data cube should only be available for visualisation purposes in the xcube Viewer

