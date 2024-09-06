## assign_dims

```python
def assign_dims(data: Dict[str, da.Array|xr.DataArray], dims: Tuple[str]) -> Dict[str, xr.DataArray]
```

### Description
The `assign_dims` function assigns dimension names to each variable in a dataset based on the provided dimension names. This function is useful for standardizing the dimensional metadata of dask arrays or xarray DataArrays within a dictionary and for the creation of xarray Datasets.

### Parameters
- **data** (`Dict[str, dask.array | xarray.DataArray]`): A dictionary where keys are variable names and values are of type `dask.array` or `xarray.DataArray`.
- **dims** (`Tuple[str]`): A tuple of dimension names to assign to the arrays.

### Returns
- `Dict[str, xarray.DataArray]`: A dictionary where keys are variable names and values are of type`xarray.DataArray` with assigned dimensions.

### Example

```python
import dask.array as da
from ml4xcube.utils import assign_dims

# Example data
data = {
    'temperature': da.random.random((10, 20, 30)),
    'precipitation': da.random.random((10, 20, 30))
}

# Assign dimensions
dims = ('time', 'lat', 'lon')
assigned_dims_data = assign_dims(data, dims)

# Output the data with assigned dimensions
for var, dataarray in assigned_dims_data.items():
    print(f"{var}: {dataarray.dims}")
```
The dimensions 'time', 'lat', and 'lon' are assigned to the data arrays in the dictionary.