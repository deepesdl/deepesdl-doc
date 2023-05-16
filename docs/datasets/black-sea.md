# Black Sea Data Cube

## How to open this dataset in DeepESDL JupyterLab
```python
from xcube.core.store import new_data_store
store = new_data_store("s3", root="deep-esdl-public", storage_options=dict(anon=True))
ds = store.open_data('black-sea-1x1024x1024.zarr')
```

## Bounding box map

![Bounding box map](black-sea.png)<br>
<span style="font-size: x-small">Map tiles and data from <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">the ODbL</a>.</span>

## Basic information

| Parameter | Value |
| ---- | ---- |
| Bounding box longitude (°) | 26.0 to 41.998999999999725 |
| Bounding box latitude (°) | 39.000000000000156 to 48.0 |
| Time range | 2015-12-31 to 2017-12-31 |
| Time period | 1D |
| Publisher | Brockmann Consult GmbH |

[Click here for full dataset metadata.](#full-metadata)

## Variable list

Click on a variable name to jump to the variable’s full metadata.

| Variable | Long name | Units |
| ---- | ---- | ---- |
| [VHM0](#VHM0) | Spectral Significant Wave Height \(Hm0\) | m |
| [chl](#chl) | Chlorophyll Concentration | mg m^\-3 |
| [sla](#sla) | Sea Level Anomaly | m |
| [sss](#sss) | Sea Surface Salinity | psu |
| [sst](#sst) | Sea Surface Temperature | K |
| [ugos](#ugos) | Absolute Geostrophic Velocity: Zonal Component | m s^\-1 |
| [ugosa](#ugosa) | Geostrophic Velocity Anomalies: Zonal Component | m s^\-1 |
| [vgos](#vgos) | Absolute Geostrophic Velocity: Meridian Component | m s^\-1 |
| [vgosa](#vgosa) | Geostrophic Velocity Anomalies: Meridian Component | m s^\-1 |

## Full variable metadata

### <a name="VHM0"></a>VHM0

| Field | Value |
| ---- | ---- |
| grid\_mapping | crs |
| long\_name | Spectral Significant Wave Height \(Hm0\) |
| processing\_level | L4 |
| references | [https://resources\.marine\.copernicus\.eu/product\-detail/BLKSEA\_MULTIYEAR\_WAV\_007\_006/DOCUMENTATION](https://resources.marine.copernicus.eu/product-detail/BLKSEA_MULTIYEAR_WAV_007_006/DOCUMENTATION) |
| source | CMEMS, Black Sea Waves Reanalysis |
| standard\_name | sea\_surface\_wave\_significant\_height |
| units | m |
| valid\_max | 6\.0 |
| valid\_min | 0\.0 |

### <a name="chl"></a>chl

| Field | Value |
| ---- | ---- |
| grid\_mapping | crs |
| long\_name | Chlorophyll Concentration |
| processing\_level | L3 |
| references | [http://www\.eo4sibs\.uliege\.be/doc/EO4SIBS\_DUM\_ATBD\_OceanColour\.pdf](http://www.eo4sibs.uliege.be/doc/EO4SIBS_DUM_ATBD_OceanColour.pdf) |
| source | EO4SIBS, Level 3 Chl\-a, 300m, daily and monthly |
| standard\_name | chlorophyll\_concentration |
| units | mg m^\-3 |
| valid\_max | 31\.0 |
| valid\_min | 0\.0 |

### <a name="crs"></a>crs

| Field | Value |
| ---- | ---- |
| crs\_wkt | GEOGCS\["WGS 84",DATUM\["WGS\_1984",SPHEROID\["WGS 84",6378137,298\.257223563,AUTHORITY\["EPSG","7030"\]\],AUTHORITY\["EPSG","6326"\]\],PRIMEM\["Greenwich",0,AUTHORITY\["EPSG","8901"\]\],UNIT\["degree",0\.0174532925199433,AUTHORITY\["EPSG","9122"\]\],AXIS\["Latitude",NORTH\],AXIS\["Longitude",EAST\],AUTHORITY\["EPSG","4326"\]\] |
| geographic\_crs\_name | WGS 84 |
| grid\_mapping\_name | latitude\_longitude |
| inverse\_flattening | 298\.257223563 |
| longitude\_of\_prime\_meridian | 0\.0 |
| prime\_meridian\_name | Greenwich |
| reference\_ellipsoid\_name | WGS 84 |
| semi\_major\_axis | 6378137\.0 |
| semi\_minor\_axis | 6356752\.314245179 |

### <a name="sla"></a>sla

| Field | Value |
| ---- | ---- |
| grid\_mapping | crs |
| long\_name | Sea Level Anomaly |
| processing\_level | L4 |
| references | [http://www\.eo4sibs\.uliege\.be/doc/EO4SIBS\_D4\.4\_AltimetryL4\_DUM\_v1\.1\.pdf](http://www.eo4sibs.uliege.be/doc/EO4SIBS_D4.4_AltimetryL4_DUM_v1.1.pdf) |
| source | EO4SIBS, Level 4, geostrophic currents, multi\-mission gridded merged products for a period of 1 year, 0\.0625°\*0\.0625°, daily |
| standard\_name | sea\_surface\_height\_above\_sea\_level |
| units | m |
| valid\_max | 0\.5 |
| valid\_min | \-0\.5 |

### <a name="sss"></a>sss

| Field | Value |
| ---- | ---- |
| grid\_mapping | crs |
| long\_name | Sea Surface Salinity |
| processing\_level | L3 |
| references | [http://www\.eo4sibs\.uliege\.be/doc/EO4SIBS\_DUM\_ATBD\_Salinity\.pdf](http://www.eo4sibs.uliege.be/doc/EO4SIBS_DUM_ATBD_Salinity.pdf) |
| source | EO4SIBS, Level 3 SSS, 0\.25°\*0\.25°, 9\-day averaged produced daily |
| standard\_name | sea\_surface\_salinity |
| units | psu |
| valid\_max | 29\.0 |
| valid\_min | 1\.0 |

### <a name="sst"></a>sst

| Field | Value |
| ---- | ---- |
| grid\_mapping | crs |
| long\_name | Sea Surface Temperature |
| processing\_level | L3 |
| references | [https://resources\.marine\.copernicus\.eu/product\-detail/SST\_BS\_SST\_L3S\_NRT\_OBSERVATIONS\_010\_013/DOCUMENTATION](https://resources.marine.copernicus.eu/product-detail/SST_BS_SST_L3S_NRT_OBSERVATIONS_010_013/DOCUMENTATION) |
| source | CMEMS, Black Sea \- High Resolution and Ultra High Resolution L3S Sea Surface Temperature |
| standard\_name | sea\_surface\_temperature |
| units | K |
| valid\_max | 305\.0 |
| valid\_min | 270\.0 |

### <a name="ugos"></a>ugos

| Field | Value |
| ---- | ---- |
| grid\_mapping | crs |
| long\_name | Absolute Geostrophic Velocity: Zonal Component |
| processing\_level | L4 |
| references | [http://www\.eo4sibs\.uliege\.be/doc/EO4SIBS\_D4\.4\_AltimetryL4\_DUM\_v1\.1\.pdf](http://www.eo4sibs.uliege.be/doc/EO4SIBS_D4.4_AltimetryL4_DUM_v1.1.pdf) |
| source | EO4SIBS, Level 4, geostrophic currents, multi\-mission gridded merged products for a period of 1 year, 0\.0625°\*0\.0625°, daily |
| standard\_name | surface\_geostrophic\_eastward\_sea\_water\_velocity |
| units | m s^\-1 |
| valid\_max | 2\.0 |
| valid\_min | \-2\.0 |

### <a name="ugosa"></a>ugosa

| Field | Value |
| ---- | ---- |
| grid\_mapping | crs |
| long\_name | Geostrophic Velocity Anomalies: Zonal Component |
| processing\_level | L4 |
| references | [http://www\.eo4sibs\.uliege\.be/doc/EO4SIBS\_D4\.4\_AltimetryL4\_DUM\_v1\.1\.pdf](http://www.eo4sibs.uliege.be/doc/EO4SIBS_D4.4_AltimetryL4_DUM_v1.1.pdf) |
| source | EO4SIBS, Level 4, geostrophic currents, multi\-mission gridded merged products for a period of 1 year, 0\.0625°\*0\.0625°, daily |
| standard\_name | surface\_geostrophic\_eastward\_sea\_water\_velocity\_assuming\_sea\_level\_for\_geoid |
| units | m s^\-1 |
| valid\_max | 2\.0 |
| valid\_min | \-2\.0 |

### <a name="vgos"></a>vgos

| Field | Value |
| ---- | ---- |
| grid\_mapping | crs |
| long\_name | Absolute Geostrophic Velocity: Meridian Component |
| processing\_level | L4 |
| references | [http://www\.eo4sibs\.uliege\.be/doc/EO4SIBS\_D4\.4\_AltimetryL4\_DUM\_v1\.1\.pdf](http://www.eo4sibs.uliege.be/doc/EO4SIBS_D4.4_AltimetryL4_DUM_v1.1.pdf) |
| source | EO4SIBS, Level 4, geostrophic currents, multi\-mission gridded merged products for a period of 1 year, 0\.0625°\*0\.0625°, daily |
| standard\_name | surface\_geostrophic\_northward\_sea\_water\_velocity |
| units | m s^\-1 |
| valid\_max | 2\.0 |
| valid\_min | \-2\.0 |

### <a name="vgosa"></a>vgosa

| Field | Value |
| ---- | ---- |
| grid\_mapping | crs |
| long\_name | Geostrophic Velocity Anomalies: Meridian Component |
| processing\_level | L4 |
| references | [http://www\.eo4sibs\.uliege\.be/doc/EO4SIBS\_D4\.4\_AltimetryL4\_DUM\_v1\.1\.pdf](http://www.eo4sibs.uliege.be/doc/EO4SIBS_D4.4_AltimetryL4_DUM_v1.1.pdf) |
| source | EO4SIBS, Level 4, geostrophic currents, multi\-mission gridded merged products for a period of 1 year, 0\.0625°\*0\.0625°, daily |
| standard\_name | surface\_geostrophic\_northward\_sea\_water\_velocity\_assuming\_sea\_level\_for\_geoid |
| units | m s^\-1 |
| valid\_max | 2\.0 |
| valid\_min | \-2\.0 |

## <a name="full-metadata"></a>Full dataset metadata

| Field | Value |
| ---- | ---- |
| Conventions | CF\-1\.9 |
| acknowledgment | EO4SIBS, CMEMS, DeepESDL project |
| contributor\_name | Brockmann Geomatics Sweden AB |
| contributor\_url | [www\.brockmann\-geomatics\.se](http://www.brockmann-geomatics.se) |
| creator\_email | info@brockmann\-consult\.de |
| creator\_name | Brockmann Consult GmbH |
| creator\_url | [www\.brockmann\-consult\.de](http://www.brockmann-consult.de) |
| date\_modified | 2022\-08\-19 16:19:15\.359970 |
| geospatial\_lat\_max | 47\.9985 |
| geospatial\_lat\_min | 39\.001500000000156 |
| geospatial\_lat\_resolution | 0\.0030000000000001137 |
| geospatial\_lon\_max | 41\.997499999999725 |
| geospatial\_lon\_min | 26\.0015 |
| geospatial\_lon\_resolution | 0\.0030000000000001137 |
| id | black\-sea\-256x256x256 |
| institution | Brockmann Consult GmbH |
| license | Terms and conditions of the DeepESDL data distribution |
| project | DeepESDL |
| publisher\_email | info@brockmann\-consult\.de |
| publisher\_name | Brockmann Consult GmbH |
| publisher\_url | [www\.brockmann\-consult\.de](http://www.brockmann-consult.de) |
| source | EO4SIBS, CMEMS |
| time\_coverage\_end | 2017\-12\-31T00:00:00\.000000000 |
| time\_coverage\_start | 2016\-01\-01T00:00:00\.000000000 |
| title | Black Sea Data Cube |

