# Hydrology Cube

## How to open this dataset in DeepESDL JupyterLab
```python
from xcube.core.store import new_data_store
store = new_data_store("s3", root="deep-esdl-public", storage_options=dict(anon=True))
ds = store.open_data('hydrology-1D-0.009deg-100x60x60-3.0.2.zarr')
```

## Bounding box map

![Bounding box map](hydrology-1D-0-009deg-100x60x60-3-0-2-zarr.png)<br>
<span style="font-size: x-small">Map tiles and data from <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">the ODbL</a>.</span>

## Basic information

| Parameter | Value |
| ---- | ---- |
| Bounding box longitude (°) | -5.70080002975464 to 37.76919997024536 |
| Bounding box latitude (°) | 28.339799316406264 to 48.17579931640626 |
| Time range | 2014-12-31 to 2022-10-06 |
| Time period | 1D |
| Publisher | DeepESDL Team |

[Click here for full dataset metadata.](#full-metadata)

## Variable list

Click on a variable name to jump to the variable’s full metadata.

| Variable | Long name | Units |
| ---- | ---- | ---- |
| [E](#E) | Evaporation | mm d^\-1 |
| [SM](#SM) | Soil Moisture | % Relative Saturation |
| [SWE](#SWE) | Snow Water Equivalent | 1 |
| [precip](#precip) | Precipitation | mm d^\-1 |

## Full variable metadata

### <a name="E"></a>E

| Field | Value |
| ---- | ---- |
| acknowledgement | Hydrology 4D |
| color\_bar\_name | plasma |
| color\_value\_max | 10 |
| color\_value\_min | 0 |
| description | Evaporation |
| long\_name | Evaporation |
| original\_add\_offset | 0\.0 |
| original\_name | E |
| original\_scale\_factor | 1\.0 |
| processing\_steps | Gridding nc datasets |
| source | 4dmed\_data\.eodchosting\.eu/4dmed\_data/GLEAM\_openloop\_V1\.1 |
| standard\_name | evaporation |
| units | mm d^\-1 |

### <a name="SM"></a>SM

| Field | Value |
| ---- | ---- |
| acknowledgement | Hydrology 4D |
| color\_bar\_name | plasma\_r |
| color\_value\_max | 1 |
| color\_value\_min | 0 |
| description | TU Wien RT1\-Sentinel\-1 soil moisutre retrievals |
| long\_name | Soil Moisture |
| original\_add\_offset | 0\.0 |
| original\_name | SM |
| original\_scale\_factor | 1\.0 |
| processing\_steps | Gridding nc datasets, daily aggregates |
| source | 4dmed\_data\.eodchosting\.eu/4dmed\_data/TUWien\_RT1\_SM |
| standard\_name | soil\_moisture |
| units | % Relative Saturation |
| untis | % relative saturation |

### <a name="SWE"></a>SWE

| Field | Value |
| ---- | ---- |
| acknowledgement | Hydrology 4D |
| color\_bar\_name | Blues\_alpha |
| color\_value\_max | 2000 |
| color\_value\_min | 0 |
| description | Snow Water Equivalent |
| long\_name | Snow Water Equivalent |
| original\_add\_offset | 0\.0 |
| original\_name | SWE |
| original\_scale\_factor | 1\.0 |
| processing\_steps | Gridding nc datasets |
| source | 4dmed\_data\.eodchosting\.eu/4dmed\_data/SWE/SWE\_CPC\_GPM\_ERA5downT\_RadGhent\_filter5mm |
| standard\_name | snow\_water\_equivalent |
| units | 1 |

### <a name="precip"></a>precip

| Field | Value |
| ---- | ---- |
| acknowledgement | Hydrology 4D |
| color\_bar\_name | viridis\_alpha |
| color\_value\_max | 100 |
| color\_value\_min | 0 |
| description | Precipitation |
| long\_name | Precipitation |
| original\_add\_offset | 0\.0 |
| original\_name | precip |
| original\_scale\_factor | 1\.0 |
| processing\_steps | Gridding nc datasets |
| source | 4dmed\_data\.eodchosting\.eu/4dmed\_data/CNR\_products/precipitation\_GPM\_CPC\_SM2RAIN\-ASCAT |
| standard\_name | precipitation |
| units | mm d^\-1 |

## <a name="full-metadata"></a>Full dataset metadata

| Field | Value |
| ---- | ---- |
| Conventions | CF\-1\.10 |
| acknowledgment | All data providers are acknowledged inside each variable |
| contributor\_name | University of Leipzig, Brockmann Consult GmbH |
| contributor\_url | [https://www\.uni\-leipzig\.de/](https://www.uni-leipzig.de/), [https://www\.brockmann\-consult\.de/](https://www.brockmann-consult.de/) |
| creator\_name | University of Leipzig, Brockmann Consult GmbH |
| creator\_url | [https://www\.uni\-leipzig\.de/](https://www.uni-leipzig.de/), [https://www\.brockmann\-consult\.de/](https://www.brockmann-consult.de/) |
| date\_modified | 2023\-12\-21T11:50:17\.830496 |
| geospatial\_lat\_max | 48\.17579932 |
| geospatial\_lat\_min | 28\.33979932 |
| geospatial\_lat\_resolution | 0\.009 |
| geospatial\_lat\_units | degrees\_north |
| geospatial\_lon\_max | 37\.76919997 |
| geospatial\_lon\_min | \-5\.70080003 |
| geospatial\_lon\_resolution | 0\.009 |
| geospatial\_lon\_units | degrees\_east |
| id | hydrology\-1D\-0\.009deg\-100x60x60\-3\.0\.2\.zarr |
| license | Terms and conditions of the DeepESDL data distribution |
| project | DeepESDL |
| publisher\_name | DeepESDL Team |
| publisher\_url | [https://www\.earthsystemdatalab\.net/](https://www.earthsystemdatalab.net/) |
| time\_coverage\_end | 2022\-10\-06T12:00:00\.000000000 |
| time\_coverage\_start | 2015\-01\-01T12:00:00\.000000000 |
| title | Hydrology Cube |

