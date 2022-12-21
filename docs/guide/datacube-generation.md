# DeepESDL datacube generation

The data cubes already provided by DeepESDL might not be sufficient 
for your application. However, this should not stop you from creating the 
resources you need from source input data and enable you to do your research. 
DeepESDL carefully adheres to the reproducibility of dataset resources. Therefore, 
there are two approaches to generate datasets. 
In the simpler one, the data is retrieved from an existing datastore without persisting the 
dataset, usually using a Jupyter notebook. 
If a dataset shall be persisted, maybe even re-published,  and is furthermore based on input data that 
needs to be e.g. downloaded beforehand or other preprocessing steps are 
performed, then the cube generation recipe approach is recommended.  Note that the Cube Gen team follows this approach for all cubes generated and published by DeepESDL. 

## Cube generation recipe approach for static data cubes

### Cube specification format
For each data cube, a unique specification is created that describes 
the cubes spatio-temporal dimensions, resolutions, coverages, and the data 
sources used to generate the cube’s target data variables. To specify each 
cube, a dedicated JSON format is created that fully describes the target 
cube’s characteristics. We use a special GeoJSON Feature format for this 
purpose so each cube definition is both human- and machine-readable and can 
be ingested and rendered by many existing tools. The GeoJSON 
Feature’s geometry represents the geographical coverage of the cube, while the 
GeoJSONFeature’s properties provide numerous further details. To describe many 
similar cubes, e.g., for using multiple spatial resolutions for same 
variables, a GeoJSON FeatureCollection may be used instead. To validate the 
JSON cube specification files, we provide a dedicated online JSON Schema 
in the DeepESDL dataset-spec GitHub repository:
 https://github.com/deepesdl/dataset-spec/blob/main/dataset-defs/template.schema.json

### Cube generation recipe

The cube generation recipe ensures, that an existing dataset provided by 
DeepESDL can be reproduced by following the documented steps and specifications. Here we describe the 
recipe structure of the provided datasets within DeepESDL.

Each predefined DeepESDL data cube is fully described in a transparent and 
comprehensive way by a dedicated sub-folder in the DeepESDL GitHub [repository 
cube-gen](https://github.com/deepesdl/cube-gen). 
Such sub-folder is what we call a cube generation recipe:
   `cube-gen/${cube-name}/`

It contains the machine-readable GeoJSON file that fully specifies the data 
cube `cube-gen/${cube-name}/cube.geojson` and provides the 
detailed human-readable information about the cube including how to generate 
it from sources in `cube-gen/${cube-name}/README.md`.  
After a cube has been released and published, we record the changes in 
`cube-gen/${cube-name}/CHANGES.md`.  
In each data cube sub-folder, further
sub-folders may exist that contain resources and sources such as 
configuration files and Python modules.
We have defined the following common sub-folder structure, but others may be used 
too:   
*    `cube-gen/${cube-name}/input-collect/`     
      Fetch, download,or copy inputs.
*    `cube-gen/${cube-name}/input-preprocess/`   
      Transform, concatenate, convert to interm. Zarr.
*    `cube-gen/${cube-name}/output-merge/`  
      Merge interm. Zarrs to target cube.
*    `cube-gen/${cube-name}/output-postprocess/`   
      Apply any postprocessing.  

Cube generation recipes are designed to be comprehensive, transparent, 
reproducible, and relocatable. That is, with very little configuration 
changes, they should be executable in different environments.

## Dynamic data cubes from Data Stores

Persistently stored data cubes have the advantage that they have a physical 
representation, i.e. they “exist” at a given storage location. That way 
the data can be “frozen” and can be assigned a version and/or a DOI. In 
addition, access to static data cubes persisted in cloud object storage 
is usually fast and scalable. 

However, there are potential issues and challenges with static cubes. Data 
sources of data cubes can become outdated,
or are simply updated, like it is the case for new EO data observations 
added to an existing product archive. In such cases, related data cubes should 
be updated too, hereby creating considerable maintenance effort and risks for the integrity of the data cube. In addition,
the generation of static data cubes is in many cases a plain duplication of 
data that is actually defined and described elsewhere. The data cube must 
ensure to stay in sync with original data sources and metadata.
Finally, static cubes can only satisfy requirements of one user or use 
case in an optimal way. By definition, they do not allow for streamlined and 
tailored datasets. 

A possible solution to mitigate these issues and address 
the challenges are dynamic data cubes. Dynamic data cubes exist in-memory 
only and will provide data in a “lazy” way. That is, chunks of a data cube 
are fetched on-demand, hence computed on-the-fly, including all the 
required transformation steps starting with the ingestion of source data. 
Dynamic cubes are generated for a given configuration that describes the 
data cube to be generated. 

Dynamic data cubes for a given single data source can be easily retrieved 
using xcube data stores. The following Python code opens a data cube 
representing a Sentinel-2 L2A data cube with the SentinelHubAPI as data source:

```python
from xcube.core.store import new_data_store
store = new_data_store("sentinelhub", **credentials)
cube = store.open_data("S2L2A", 
                       variable_names=["B03","B06","B8A"],
                       bbox=..., 
                       spatial_res=...,
                       time_range=..., 
                       time_period=...
                       )
```

Dynamic cubes are application-specific and configured by individual users.

Below is an overview of the possible xcube data stores that can be 
used to create dynamic cubes together with the title of an example notebook, 
if there is one available. A description of how the example notebooks can be 
accessed is in section [DeepESDL JupyterLab](jupyterlab.md#getting-started-notebooks):

| Data store ID | Content                               | Example Notebook        | Access                            |
|---------------|---------------------------------------|-------------------------|-----------------------------------|
| s3            | Any Zarr dataset on AWS S3 or similar | 01 Access public cubes  | Depends on permissions            |
| cmems         | CMEMS datasets                        | 02 Generate CMEMS cubes | Requires registration, free       |
| cciodp        | All ESA CCI datasets                  | 03 Generate CCI Cubes   | Free                              |
| cds           | Climate data store                    |                         | Requires registration, free       |
| sentinelhub   | Sentinel 1 to 3, Landsat, ...         |                         | Requires registration, with costs |
