# xcube Data Stores

The xcube data stores Framework is described in detail in the xcube 
[documentation](https://xcube.readthedocs.io/en/latest/dataaccess.html).
In this section, the currently available data stores are presented with an 
example for each of them. For more detailed examples, please refer to the 
getting started notebook section of the jupyterlab 
[user guide](../guide/jupyterlab.md#getting-started-notebooks).

-   [DeepESDL public datasets](#deepesdl-datasets-in-public-object-storage)
-   [xcube CMEMS data store](#xcube-cmems-data-store)
-   [xcube ESA CCI data store](#xcube-esa-cci-data-store)
-   [xcube Sentinel Hub data store](#xcube-sentinel-hub-data-store)
-   [xcube Copernicus Climate Change Service data store](#xcube-copernicus-climate-change-service-c3s-data-store)

## DeepESDL datasets in public object storage

The DeepESDL Consortium provides a growing number of datasets which are made 
analysis-ready and persisted in public object storage for easy access. 
An overview of available persisted datasets is given section 
[datasets](datasets.md). 

To access the DeepESDL persisted datasets, please follow the example: 

Initializing the xcube datastore for s3 object storage:
```python
from xcube.core.store import new_data_store
store = new_data_store("s3", 
                       root="deep-esdl-public", 
                       storage_options=dict(anon=True))
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

## Contribute datacubes to the public

If you have created your own dataset and wish to make it available to the 
public in the **deep-esdl-public** cloud bucket, that's fantastic!
For onboarding new data cubes to deep-esdl-public, you need to make sure 
your dataset creation is documented and reproducible, and that the 
documentation is accessible. This can be e.g. your own GitHub repository, or 
you could contribute to the [DeepESDL cube-gen repository](https://github.com/deepesdl/cube-gen).


## xcube CMEMS data store
The xcube Copernicus Marine Data Store (CMEMS) data store allows for reading and 
exploring data from the 
[Copernicus Marine Data Store](https://data.marine.copernicus.eu/products).

A user login is required to access the data provided by CMEMS.
If you do not have cmems user yet, you can register for an 
[account](https://resources.marine.copernicus.eu/registration-form). 
For DeepESDL Jupyter Lab default credentials are configured, but due to 
bandwidth 
limitation by CMEMS performance may impair when used by several people
simultaneously. 

To use your own CMEMS account:
```python
# replace with your user name and pwd
#cmemsuser='your-user-name'
#cmemspwd='your-user-password'
```
Initializing the xcube datastore for CMEMS:

```python
from xcube.core.store import new_data_store
store = new_data_store('cmems')
```

If you use your own CMEMS account: 

```python
# store = new_data_store('cmems', 
#                        cmems_user=cmemsuser, 
#                        cmems_user_password = cmemspwd)
# store = new_data_store('cmems')
```

List all available datasets: 

```python
store.list_data_ids()
```

To open a certain dataset, please replace the path with the path to the 
desired dataset, which was listed in `store.list_data_ids()`

```python
dataset = store.open_data('dataset-bal-reanalysis-wav-hourly',
                          'dataset:zarr:cmems')
```


## xcube ESA CCI data store
The xcube ESA Climate Change Initiative (CCI) data store allows for reading and 
exploring data from the 
[ESA Climate Change Initiative](https://climate.esa.int/en/esa-climate/esa-cci/).
More information on the data sets offered can be found in the
[Open Data Portal](https://climate.esa.int/en/odp/#/dashboard).


Initializing the xcube datastore for CCI:

```python
from xcube.core.store import new_data_store
store = new_data_store('cciodp')
```

The cci datastore offers many datasets, therefore listing all available ones 
will reveal a long list of results. The store can thus be searched by specific 
parameters, which can be listed:

```python
store.get_search_params_schema()
```

A target data set can then be be opened following the below schema  
example below:

```python
dataset = store.open_data('esacci.SST.day.L4.SSTdepth.multi-sensor.multi-platform.OSTIA.2-1.sst',
                          variable_names=['analysed_sst'],
                          time_range=['1981-08-31','2016-12-31'])

```

## xcube Sentinel Hub data store

The xcube Sentinel Hub (SH) data store allows for reading and exploring data provided by the 
[Sentinel Hub cloud API](https://www.sentinel-hub.com/).

**Please note:** In order to access data from the commercial Sentinel Hub service, you need Sentinel 
Hub API credentials. 

DeepESDL users may apply for sponsored Sentinel Hub subscriptions - 
please contact the DeepESDL team or directly appy via the [Network of Resources portal](https://nor-discover.cloudeo.group/Service/EDC-Sentinel-Hub/SponsoringWizardPricelist).


Initializing the xcube datastore for Sentinel Hub:

```python
from xcube.core.store import new_data_store
store = new_data_store('sentinelhub', num_retries=400)
```

The Sentinel Hub xcube data store offers different datasets which are 
accessible via data ids:

```python
list(store.get_data_ids())
```

For requesting Sentinel Hub data subsetting is crucial. In the below example 
a Sentinel-2 L2A is requested.

```python
dataset = store.open_data('S2L2A', 
                          variable_names=['B04'], 
                          bbox=[9.7, 53.4, 10.2, 53.7], 
                          spatial_res=0.00018, 
                          time_range=('2020-08-10','2020-08-20'), 
                          time_period='1D',
                          tile_size= [1024, 1024])
```

## xcube Copernicus Climate Change Service (C3S) data store

The xcube [Climate Data Store](https://cds.climate.copernicus.eu) (CDS)
allows to read and explore temperature data from the Copernicus Climate 
Change Service (C3S). 

To access data from the Climate Data Store, you need a CDS API key. You can 
obtain the UID and API key as follows:

1.    Create a user account on the [CDS Website](https://cds.climate.copernicus.
eu/user/register).
2.    Log in to the website with your user name and password.
3.    Navigate to your user profile on the website. Your API key is shown 
      at the bottom of the page.

Then export the `CDSAPI_URL` and `CDSAPI_KEY` environment variables, 
replacing `[UID]` and `[API-KEY]` with the actual values from your account:

```bash
export CDSAPI_URL=https://cds.climate.copernicus.eu/api/v2
export CDSAPI_KEY=[UID]:[API-KEY]
```

For DeepESDL Jupyter Lab default credentials are configured, but due to 
bandwidth limitation by CDS performance may impair when used by several 
people simultaneously. 

Initializing the xcube datastore for C3S:

```python
from xcube.core.store import new_data_store
store = new_data_store('cds')
```

List all available datasets: 

```python
store.list_data_ids()
```

Get more info about a specific dataset. This includes a description of the 
possible open formats:

```python
store.describe_data('reanalysis-era5-single-levels-monthly-means:monthly_averaged_reanalysis')
```
There are 4 required parameters, so we need to provide them to open a dataset:

```python
dataset = store.open_data('reanalysis-era5-single-levels-monthly-means:monthly_averaged_reanalysis', 
                          variable_names=['2m_temperature'], 
                          bbox=[-10, 45, 40, 65], 
                          spatial_res=0.25, 
                          time_range=['2001-01-01', '2010-12-31'])
``` 

## Contribute a xcube plugin for a new datastore
Do you have an API or a data source which you wish to make available via the 
xcube data stores framework? We would be very happy if you like to 
contribute to the open source xcube software ecosystem! 
The xcube data stores framework is described in detail in the xcube 
[documentation](https://xcube.readthedocs.io/en/latest/dataaccess.html). 
There you can have a look at the details of what is mandatory for a data 
store. Furthermore, you can get inspiration from existing data store plugins:
- [xcube-cds](https://github.com/dcs4cop/xcube-cds)
- [xcube-cci](https://github.com/dcs4cop/xcube-cci)
- [xcube-cmems](https://github.com/dcs4cop/xcube-cmems)
- [xcube-sh](https://github.com/dcs4cop/xcube-sh)

In case of questions, please feel free to reach out to us! We will give 
our best to support you :)