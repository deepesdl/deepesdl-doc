## get_dim_range

```python
def get_dim_range(cube: xr.DataArray, dim: str) -> Union[Tuple[float, float], Tuple[str, str]]
```

### Description
Calculates and returns the minimum and maximum values of a specified dimension within an `xarray.Dataset`. This function supports dimensions with numerical or datetime data types, making it versatile for a range of data analysis contexts.

### Parameters
- **cube** (`xarray.DataArray`): The input data cube from which the dimension range is to be calculated.
- **dim** (`str`): The name of the dimension for which the range is to be determined.

### Returns
- `Union[Tuple[float, float], Tuple[str, str]]`: The minimum and maximum values of the dimension. For datetime dimensions, these values are formatted as strings; for numerical dimensions, they are returned as numbers.



### Example

Here's how you might use the `get_dim_range` function to find the range of the 'time' dimension in a dataset:
```python
import numpy as np
import xarray as xr
from ml4xcube.utils import get_dim_range

# Create a sample DataArray with datetime and numerical data
times = np.array(['2020-01-01', '2020-01-02', '2020-01-03'], dtype='datetime64[D]')
data = np.random.rand(3, 2, 2)  # Random data for 3 days, 2 latitudes, and 2 longitudes
cube = xr.DataArray(data, dims=['time', 'latitude', 'longitude'], coords={'time': times})

# Get the range of the 'time' dimension
time_range = get_dim_range(cube, 'time')
print("Time Dimension Range:", time_range)
```
A simple `xarray.DataArray` with a 'time' dimension is created and `get_dim_range` is used to extract and print the date range.

