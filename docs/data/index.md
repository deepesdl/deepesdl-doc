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


[Get Started!](../guide/jupyterlab/notebooks/Access_public_cubes.ipynb){ .md-button .md-button--accent }

---

## Available Data Sources

|                                                                                                                                                                                                                                   | Data Source | Datasets / Collections | Tags                                  | How to Access                                                                                                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|------------------------|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![CDS](https://climate.copernicus.eu/sites/default/files/custom-uploads/branding/C3S%E2%80%93POS%E2%80%93LINE.png){.logo-icon-table}                                                                                                                          | **[Copernicus Climate Data Store (CDS)](https://cds.climate.copernicus.eu/)** | ERA5, Climate Projections, Sectoral Indices | `climate` `reanalysis` `forecast`     | [Example Notebook](../guide/jupyterlab/notebooks/Generate_C3S_CDS_cubes.ipynb)                                                                                                                |
| ![CMEMS](https://knowledge4policy.ec.europa.eu/sites/default/files/53443b17-0adb-44e1-8fd3-662fa7eda708.png){.logo-icon-table}                                                                                                    | **[Copernicus Marine Service (CMEMS)](https://marine.copernicus.eu/)** | Ocean physics, ocean color, forecasts | `ocean` `marine` `forecast`           | [Example Notebook](../guide/jupyterlab/notebooks/Generate_CMEMS_cubes.ipynb)                                                                                                                        |
| ![CLMS](img/logo_clms.png){.logo-icon-table}                                                                                                                                                                                      | **[Copernicus Land Monitoring Service (CLMS)](https://land.copernicus.eu/en/dataset-catalog)** | Dynamic Land Cover, CORINE | `land use` `vegetation`               | _Coming soon_                                                                                                                                                                                 |
| ![EOPF](https://www.dlr.de/de/eoc/forschung-transfer/projekte-und-missionen/eopf-sentinel-zarr-samples-service/esa_eopf_logo_2025_color_esa_16x9.jpg/@@images/image-1000-d87d614b71d37583fc8cf99cfbf55b0d.jpeg){.logo-icon-table} | **[EOPF Sample Service](https://zarr.eopf.copernicus.eu/)** | Sentinel datasets in Zarr format | `sentinel` `sample` `zarr`            | _Coming soon_                                                                                                                                                                                 |
| ![ESA CCI](https://brand.esa.int/files/2020/05/ESA_logo_2020_Deep-scaled.jpg){.logo-icon-table}                                                                                                                                   | **[ESA Climate Data Centre (CCI)](https://climate.esa.int/en/data/#/dashboard)** | Essential Climate Variables (ECVs) | `climate` `ECVs` `environment`        | [Example Notebook](../guide/jupyterlab/notebooks/Generate_CCI_cubes.ipynb)                                                                                                                          |
| ![SMOS](https://www.esa.int/eologos/images/smos.jpg){.logo-icon-table}                                                                                                                                                            | **[ESA SMOS](https://earth.esa.int/eogateway/missions/smos)** | Soil Moisture & Ocean Salinity | `soil-moisture` `salinity` `satellite` | _Coming soon_                                                                                                                                                                                 |
| ![GEDI](https://gedi.umd.edu/wp-content/uploads/2020/10/GEDI_16_10.jpg){.logo-icon-table}                                                                                                                                         | **[Global Ecosystem Dynamics Investigation (GEDI)](https://gedi.umd.edu/)** | Canopy height, biomass, elevation | `canopy height` `biomass` `lidar`     | _Coming soon_                                                                                                                                                                                 |
| ![Sentinel Hub](https://www.sentinel-hub.com/img/press/sentinel_hub_by_planet_logo_big.png){.logo-icon-table}                                                                                                                     | **[Sentinel Hub](https://www.sentinel-hub.com/)** | Sentinel‑1/2/3/5P, Landsat, MODIS | `satellite` `optical` `radar` `multi-source` | [Example Notebook](../guide/jupyterlab/notebooks/Generate_SentinelHub_cubes.ipynb)                                                                                                                  |
| ![STAC](https://stacspec.org/public/images-original/STAC-04.png){.logo-icon-table}                                                                                                                                                | **[SpatioTemporal Asset Catalog (STAC)](https://stacspec.org/en/about/datasets/)** | Sentinel, Planet, PROBA‑V | `catalog` `search` `satellite`        | [General Example Notebook](../guide/jupyterlab/notebooks/Access_data_from_nonsearchable_stac_catalog.ipynb), [CDSE Example Notebook](../guide/jupyterlab/notebooks/Access_Sentinel2_data_from_CDSE.ipynb) |
| ![Zenodo](https://about.zenodo.org/static/img/logos/zenodo-black-border.svg){.logo-icon-table}                                                                                                                                    | **[Zenodo](https://zenodo.org/)** | Scientific open data (various) | `general` `open-data`                 | [Example Notebook](../guide/jupyterlab/notebooks/Access_data_from_Zenodo.ipynb)                                                                                                                     |
| ![DeepESDL](../img/logo/cube_small.png){.logo-icon-table}                                                                                                                                                                         | **DeepESDL Public Data Cubes** | Pre-packaged ESDL data cubes | `analysis-ready` `multi-source`       | [Example Notebook](../guide/jupyterlab/notebooks/Access_public_cubes.ipynb)                                                                                                                         |

---

## Want to Use Your Own Data?

DeepESDL supports seamless integration of your own datasets into the analysis-ready cube environment. This allows joint 
processing and comparison with public Earth System data.  
👉 [Learn how to integrate your own data](../guide/jupyterlab/notebooks/Upload_files_to_shared_team_s3_storage.ipynb)

