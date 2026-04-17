---
hide:
  navigation.footer
---


# Data

DeepESDL provides access to a broad range of Earth System datasets through a unified, analysis-ready 
data cube framework. Whether you're working on climate research, land use monitoring, or marine studies, DeepESDL helps 
you access, integrate, and analyze diverse data sources—without the need for heavy local storage or complex preprocessing.

Data is accessed **lazily** using the powerful [xcube library](https://xcube.readthedocs.io/en/latest/dataaccess.html), 
which accesses data directly from remote services. This means you can work with massive datasets on-demand—saving time, 
storage, and effort.

In addition to public data sources, DeepESDL supports the integration of **your own datasets** into the same framework, 
enabling seamless joint analysis and visualization. For guidance on integrating your own data, see
[this guide](#want-to-use-your-own-data).

<br>

[Get Started!](../guide/jupyterlab/notebooks/generic-notebooks/Access_public_cubes.ipynb){ .md-button }

---

## Available Data Sources

| Data Source | Example | How to Access | Plugin repository |
|-------------|--------|---------------|-------------------|
| **[Copernicus Climate Data Store (CDS)](https://cds.climate.copernicus.eu/)** | `new_data_store("cds")` | [Example Notebook](../guide/jupyterlab/notebooks/xcube-datastores/Generate_C3S_CDS_cubes.ipynb) | [Github](https://github.com/xcube-dev/xcube-cds) |
| **[Copernicus Marine Service (CMEMS)](https://marine.copernicus.eu/)** | `new_data_store("cmems")` | [Example Notebook](../guide/jupyterlab/notebooks/xcube-datastores/Generate_CMEMS_cubes.ipynb) | [Github](https://github.com/xcube-dev/xcube-cmems) |
| **[Copernicus Land Monitoring Service (CLMS)](https://land.copernicus.eu/en/dataset-catalog)** | `new_data_store("clms")` | [Example Notebook <br/>(external link)](https://github.com/xcube-dev/xcube-clms/blob/main/examples/notebooks/CLMS_lazy_load.ipynb)<br/> [Example Notebook <br/>(external link)](https://github.com/xcube-dev/xcube-clms/blob/main/examples/notebooks/CLMS_preload.ipynb) | [Github](https://github.com/xcube-dev/xcube-clms) |
| **[DeepESDL Public Data Cubes](../guide/data/pre-generated/index.md)** | `new_data_store("s3", root="deep-esdl-public")` | [Example Notebook](../guide/jupyterlab/notebooks/generic-notebooks/Access_public_cubes.ipynb) |  |
| **[EOPF Sample Service](https://zarr.eopf.copernicus.eu/)** | `new_data_store("eopf-zarr")` | [Example Notebook <br/>(external link)](https://github.com/EOPF-Sample-Service/xcube-eopf/blob/main/examples/sentinel_2.ipynb) | [Github](https://github.com/EOPF-Sample-Service/xcube-eopf) |
| **[ESA Climate Data Centre (CCI)](https://climate.esa.int/en/data/#/dashboard)** | `new_data_store("cciodp")`<br/>`new_data_store("ccizarr")` | [Example Notebook](../guide/jupyterlab/notebooks/xcube-datastores/Generate_CCI_cubes.ipynb) | [Github](https://github.com/xcube-dev/xcube-cci) |
| **[ICOS Data Portal](https://www.icos-cp.eu/data-services)** | `new_data_store("icosdp")` | [Example Notebook <br/>(external link)](https://github.com/xcube-dev/xcube-icosdp/blob/main/examples/access_fluxcom_x_base.ipynb) | [GitHub](https://github.com/xcube-dev/xcube-icosdp) |
| **[ESA SMOS](https://earth.esa.int/eogateway/missions/smos)** | `new_data_store("smos")` | [Example Notebook <br/>(external link)](https://github.com/xcube-dev/xcube-smos/blob/main/notebooks/demo-store.ipynb) | [Github](https://github.com/xcube-dev/xcube-smos) |
| **[Global Ecosystem Dynamics Investigation (GEDI)](https://gedi.umd.edu/)** | `new_data_store("gedi")` | [Example Notebook <br/>(external link)](https://github.com/xcube-dev/xcube-gedidb/blob/main/examples/notebooks/gedi_data_store.ipynb) | [Github](https://github.com/xcube-dev/xcube-gedi) |
| **[Sentinel Hub](https://www.sentinel-hub.com/)** | `new_data_store("sentinelhub")` | [Example Notebook](../guide/jupyterlab/notebooks/xcube-datastores/Generate_SentinelHub_cubes.ipynb) | [Github](https://github.com/xcube-dev/xcube-sh) |
| **[SpatioTemporal Asset Catalog (STAC)](https://stacspec.org/en/about/datasets/)** | `new_data_store("stac")`<br/>`new_data_store("stac-cdse")`<br/>`new_data_store("stac-cdse-ardc")` | [General Example Notebook](../guide/jupyterlab/notebooks/xcube-datastores/Access_data_from_nonsearchable_stac_catalog.ipynb),<br/> [CDSE Example Notebook](../guide/jupyterlab/notebooks/xcube-datastores/Access_Sentinel2_data_from_CDSE.ipynb) | [Github](https://github.com/xcube-dev/xcube-stac) |
| **[Zenodo](https://zenodo.org/)** | `new_data_store("zenodo")` | [Example Notebook](../guide/jupyterlab/notebooks/xcube-datastores/Access_data_from_Zenodo.ipynb) | [Github](https://github.com/xcube-dev/xcube-zenodo) |

## Want to Use Your Own Data?

DeepESDL supports seamless integration of your own datasets into the analysis-ready cube environment. This allows joint 
processing and comparison with public Earth System data.  
👉 [Learn how to integrate your own data.](../guide/jupyterlab/notebooks/team-storage/Upload_files_to_shared_team_s3_storage.ipynb)

