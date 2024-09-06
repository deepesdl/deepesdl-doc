## get_insights

```python
def get_insights(cube: xr.Dataset, variable: str, layer_dim: str = None) -> None
```

### Description
Various characteristics of a data cube represented by an `xarray.DataArray` are extracted and printed. 
The function provides information such as the variable's name, dimension names and ranges, the size of the data cube, the number and percentage of `NaN` values, and the range of data values. 
Additionally, it identifies the maximum and minimum gap sizes within the data cube layers

### Parameters

- **cube** (`xarray.Dataset`): The input data cube.
- **variable** (`str`): variable to extract the `DataArray` containing the data to receive insights from
- **layer_dim** (`str`): The dimension along which to iterate and extract detailed layer-specific information. First dimension is default if not specified. 

### Returns
- `None`: The function prints the extracted characteristics of the data cube.

### Example

```python
import xarray as xr
from ml4xcube.cube_insights import get_insights

# Load sample data
ds = xr.open_zarr('sample_data.zarr')
ds = ds['temperature']

# Get insights from the data cube
get_insights(ds)
```
The `get_insights` function, prints the following statistics (example for a cube containing dimensions named Time, Latitude, and Longitude):

```
100%|████████████████████| 10/10 [00:09<00:00,  1.10it/s]
The data cube has the following characteristics:
 
Variable:             Land Surface Temperature
Shape:                (time: 10, lat: 2160, lon: 4320)
Time range:           2002-05-21 - 2002-08-01
Latitude range:       -89.958° - 89.958°
Longitude range:      -179.958° - 179.958°
Total size:           93312000
Size of each layer:   9331200
Total gap size:       74069847 -> 79 %
Maximum gap size:     87 % on 2002-06-06
Minimum gap size:     75 % on 2002-08-01
Value range:          222.99 - 339.32
```