## plot_slice

```python
def plot_slice(
    ds: xr.DataArray, var_to_plot: str, xdim: str, ydim: str, filter_var: str ='land_mask', title: str ='Slice Plot',
    label: str ='Cube Slice', color_map: str ='viridis', xlabel: str ='Longitude', ylabel: str ='Latitude',
    save_fig: bool = False, file_name: str ='plot.png', fig_size: Tuple[int, int] =(15, 10), vmin: float = None,
    vmax: float = None, ticks: List[float] = None
) -> None
```

### Description
The `plot_slice` function plots a slice of data from an `xarray.DataArray` with an optional mask for context. It visualizes the specified variable using a heatmap and can highlight land borders if a mask is provided (e.g. land mask for ESDC). The function also supports saving the plot to a file.

### Parameters

- **ds** (`xarray.DataArray`): DataArray containing the data to plot.
- **var_to_plot** (`str`): Name of the variable to visualize.
- **xdim** (`str`): Name of the x dimension to plot (e.g., longitude).
- **ydim** (`str`): Name of the y dimension to plot (e.g., latitude).
- **filter_var** (`str`): Name of the variable used for masking relevant areas for plotting. Defaults to `'land_mask'`.
- **title** (`str`): Title of the plot. Defaults to `'Cube Slice Plot'`.
- **label** (`str`): Legend label for the plot. Defaults to `'Cube Slice'`.
- **color_map** (`str`): Color map to use for the plot. Defaults to `'viridis'`.
- **xlabel** (`str`): Label for the x-axis. Defaults to `'Longitude'`.
- **ylabel** (`str`): Label for the y-axis. Defaults to `'Latitude'`.
- **save_fig** (`bool`): If `True`, saves the figure to a file. Defaults to `False`.
- **file_name** (`str`): Name of the file to save the plot to, if `save_fig` is `True`. Defaults to `'plot.png'`.
- **fig_size** (`tuple`): Size of the figure to create. Defaults to `(15, 10)`.
- **vmin** (`float`): Minimum value for the color bar. Defaults to `None`.
- **vmax** (`float`): MMaximum value for the color bar. Defaults to`None`.
- **ticks** (`List[float]`): List of tick values for the color bar. Defaults to `None`.

### Returns
- `None`: The function creates a plot but does not return any value.

### Example

```python
import numpy as np
import xarray as xr
from ml4xcube.xr_plots import plot_slice

# Example usage with a sample dataset
ds = xr.Dataset({
    'temperature': (('time', 'latitude', 'longitude'), np.random.rand(10, 20, 30)),
    'precipitation': (('time', 'latitude', 'longitude'), np.random.rand(10, 20, 30)),
    'land_mask': (('latitude', 'longitude'), np.random.choice([True, False], size=(20, 30)))
})

# Select a specific time slice (valid index within the example data range)
ds_slice = ds.isel(time=0)

# Plot the slice
plot_slice(
    ds          = ds_slice,
    var_to_plot = 'temperature',
    xdim        = 'longitude',
    ydim        = 'latitude',
    filter_var  = 'land_mask',
    title       = 'Temperature Plot',
    label       = 'Temperature (°C)',
    color_map   = 'coolwarm',
    xlabel      = 'Longitude',
    ylabel      = 'Latitude',
    save_fig    = True,
    file_name   = 'temperature_plot.png',
    fig_size    = (12, 8),
    vmin        = -10,
    vmax        = 30,
    ticks       = [-10, 0, 10, 20, 30]
)
```

### Notes
- Ensure that the `filter_var` is present in the dataset to use it as a mask.
- Adjust the `fig_size`, `vmin`, `vmax`, and `ticks` parameters as needed to customize the plot appearance.

