# DeepESDL data cubes

DeepESDL provides a growing list of relevant variables for Earth System Science. 
Most of them have been derived from Earth Observation, but the compilation also 
includes model or re-analysis data if deemed useful.
DeepESDL is very grateful to all data owners for kindly providing the datasets 
and allowing us to process, and redistribute them free of charge. 
All data cubes generated and distributed by DeepESDL come without any warranty, 
neither from the owners, from the DeepESDL, nor from ESA.

During ingestion into the DeepESDL, datasets are typically transformed in 
space and 
time to fit to the common grid of the data cube, a process that necessarily 
modifies the original data. If you are looking for the original data, please 
follow the links within the dataset attributes for each variable and contact 
the data owners.

# Datasets

Data access is possible in two main manners within DeepESDL. xcube
data stores provide on-the-fly access to datasets via the data stores framework.
Other datasets are made anaylsis-ready and persisted in object storage for
fastest access.

-   [xcube Data Stores](datastores.md)
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
