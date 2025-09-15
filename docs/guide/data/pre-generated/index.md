# Analysis-ready data cubes
## DeepESDL datasets in public object storage

The DeepESDL Consortium provides a growing number of datasets which are made
analysis-ready and persisted in public object storage for easy access:

-   [Earth System Data Cube](ESDC.md)
-   [Black Sea Cube](black-sea.md)
-   [Land Cover Cube](LC-1x2025x2025-2-0-0-levels.md)
-   [Ocean Cube](ocean-1M-9km-1x1080x1080-1-4-0-zarr.md)
-   [SMOS freeze/thaw Cube](SMOS-snow-1x720x720-1-0-1-zarr.md)
-   [SMOS ocean salinity Cube](SMOS-L2C-OS-20230101-20231231-1W-res0-1x1000x1000-levels.md)
-   [SMOS soil moistrue Cube](SMOS-L2C-SM-20230101-20231231-1W-res0-1x1000x1000-levels.md)
-   [Polar Cube](polar-100m-1x2048x2048-1-0-1-zarr.md)
-   [Permafrost Cube](esa-cci-permafrost-1x1151x1641-0-0-2-zarr.md)
-   [Hydrology Cube](hydrology-1D-0-009deg-100x60x60-3-0-2-zarr.md)



## Data Access

To access the DeepESDL persisted datasets, please follow the example or explore the 
dedicated example [Jupyter Notebook](../../jupyterlab/notebooks/generic-notebooks/Access_public_cubes.ipynb):

Initializing the xcube datastore for s3 object storage:
```python
from xcube.core.store import new_data_store
store = new_data_store("s3", 
                       root="deep-esdl-public")
```
List all available datasets:

```python
store.list_data_ids()
```

To open a certain dataset, please replace the path with the path to the
desired dataset, which was listed in `store.list_data_ids()`

```python
dataset = store.open_data('black-sea-1x1024x1024.zarr')
```


