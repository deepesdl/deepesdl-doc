# 4. Cube Insights

In order to decide which preprocessing steps are required by your machine learning application, the `insights` module
offers tools for extracting and analyzing characteristics of an `xarray.DataArray` object. This module includes
functions to assess the completeness and distribution of data within the cube.

## Demo Notebook

The corresponding Jupyter notebook containing the entire workflow can be accessed here:

- [Landsurface Temperature Insights](https://github.com/deepesdl/ML-Toolkits/blob/master/Examples/cube_insights.ipynb)

The detailed workflow in order to analyze the specifics of a data cube is demonstrated in the following:

```python
import xarray as xr
from ml4xcube.insights import get_insights

# Load sample data
ds = xr.open_zarr('sample_data.zarr')
ds = ds['temperature']

# Get insights from the data cube
get_insights(ds)
```

The `get_insights` function, prints the following statistics (example for a cube containing dimensions named time, latitude, and longitude):

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

Utiliting the get_gap_heat_map the amount of missing values over time can be computed for every latitude/longitude pixel:

```python
import xarray as xr
from ml4xcube.plotting import plot_slice
from ml4xcube.insights import get_gap_heat_map

# Load sample data
ds = xr.open_zarr('sample_data.zarr')
ds = ds['temperature']

# Generate and visualize the gap heat map
gap_heat_map = get_gap_heat_map(ds)
dataset   = gap_heat_map.to_dataset(name='temperature')

plot_slice(
    ds          = dataset,
    var_to_plot = 'temperature',
    color_map   = "plasma",
    title       = "Filled artificial gaps matrix",
    label       = "Number of gaps",
    xdim        = "lon",
    ydim        = "lat"
)


```

Running this example results in the following illustration, showing a heatmap of data gaps in the land surface temperature
variable over time. The number of available data ranges from 0 to 10, corresponding to the 10 frames in the analyzed cube:

<p align="center">
    <img src="../../img/heatmap.png" alt="Gap Heat Map" width="70%">
</p>
<p align = "center"><i>
Heatmap of available data in the land surface temperature variable over time</i>
</p>