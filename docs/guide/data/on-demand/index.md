# On-demand data cubes
## xcube data stores

Dynamically create your own data cubes from data sources from the underlying source data at the time of request.
This makes it possible to select specific variables, define spatial and temporal subsets, 
and always work with the most up-to-date data.
On-demand generation is more flexible than persisted cubes, 
but may require longer preparation times, depending on dataset size and configuration.

## Data Access 

Through xcube, several datastores can be accessed for creating on-demand cubes.
For details on configuration and usage of each datastore, please refer to the [xcube documentation](https://xcube.readthedocs.io/en/latest/dataaccess.html#available-data-stores) or
the [example notebooks](../../jupyterlab/notebooks/xcube-datastores/Generate_C3S_CDS_cubes.ipynb).

- [Copernicus Climate Data Store (CDS)](../../jupyterlab/notebooks/xcube-datastores/Generate_C3S_CDS_cubes.ipynb)
- [Copernicus Marine Service (CMEMS)](../../jupyterlab/notebooks/xcube-datastores/Generate_CMEMS_cubes.ipynb)
- [Copernicus Land Monitoring Service (CLMS)](https://github.com/xcube-dev/xcube-clms/blob/main/examples/notebooks/CLMS_lazy_load.ipynb)
- [EOPF Sample Service](https://github.com/EOPF-Sample-Service/xcube-eopf/blob/main/examples/sentinel_2.ipynb)
- [ESA Climate Data Centre (CCI)](../../jupyterlab/notebooks/xcube-datastores/Generate_CCI_cubes.ipynb)
- [ESA SMOS](https://github.com/xcube-dev/xcube-smos/blob/main/notebooks/demo-store.ipynb)
- [Global Ecosystem Dynamics Investigation (GEDI)](https://github.com/xcube-dev/xcube-gedidb/blob/main/examples/notebooks/gedi_data_store.ipynb)
- [Sentinel Hub](../../jupyterlab/notebooks/xcube-datastores/Generate_SentinelHub_cubes.ipynb)
- [SpatioTemporal Asset Catalog (STAC)](../../jupyterlab/notebooks/xcube-datastores/Access_data_from_nonsearchable_stac_catalog.ipynb)
- [Zenodo](../../jupyterlab/notebooks/xcube-datastores/Access_data_from_Zenodo.ipynb)  






