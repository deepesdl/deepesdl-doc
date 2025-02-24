## rechunk_cube

```python
def rechunk_cube(source_cube: xr.DataArray, target_chunks: Dict[str, int] | Tuple[int] | List[int], target_path: str)
```

### Description
The `rechunk_cube` function rechunks an xarray `DataArray` to a new chunking scheme and stores the result at the specified path. 

### Parameters
- **source_cube** (`xarray.DataArray`): The input `DataArray` that you want to rechunk. This `DataArray` should be already chunked or be capable of being chunked.
- **target_chunks** (`Dict[str, int] | Tuple[int] | List[int]`): The desired chunk sizes for the rechunking operation. This can be specified in different formats:
  - **Dictionary**: Specify sizes for each named dimension, e.g., `{'lon': 60, 'lat': 1, 'time': 100}`. 
  - **Tuple or List**: Specify sizes by order, corresponding to the array's dimensions, e.g., `(60, 1, 100)`.
- **target_path** (`str`): The path where the rechunked `DataArray` should be stored, typically a path to a Zarr store. 

### Returns
- `None`: The function does not return any value. It prints a message upon successful completion of the rechunking process.

### Example

```python
import numpy as np
import xarray as xr
from ml4xcube.utils import rechunk_cube

# Example data
source_cube = xr.DataArray(
    np.random.rand(100, 200, 300),
    dims=['time', 'lat', 'lon'],
    name='example_data'
)

# Desired chunk sizes
target_chunks = {'time': 10, 'lat': 20, 'lon': 30}

# Rechunk the DataArray
rechunk_cube(source_cube, target_chunks=target_chunks, target_path='rechunked_data.zarr')

```
In this example, the `source_cube` is rechunked according to the specified `target_chunks` and stored at the given `target_path`.

