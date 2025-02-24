## assign_mask

```python
def assign_mask(ds: xr.Dataset, mask: da.Array, mask_name: str = None, stack_dim: str = 'time') -> xr.Dataset
```

### Description
The `assign_mask` function incorporates a mask into an `xarray.Dataset`, optionally expanding it along a specified 
dimension. This is particularly useful when you need to apply the same mask across multiple data points in a dataset,
such as across different time steps or other dimensions. The function ensures that the mask is properly aligned with 
the dataset's dimensions and chunks, facilitating seamless integration.

### Parameters
- **ds** (`xarray.Dataset]`): TThe dataset to which the mask will be assigned.
- **mask** (`dask.array`):  The mask array to be integrated into the dataset. It must be compatible in shape or expandable to the dimensions of the dataset.
- **mask_name** (`str`): The name assigned to the mask variable within the dataset. Defaults to `filter_mask` if not provided.
- **stack_dim** (`str`): The dimension along which to expand the mask. If not specified, the mask will not be expanded. Defaults to expanding along the 'time' dimension if no value is provided.

### Returns
- `xarray.Dataset`: The updated dataset containing the new mask variable.

### Example

```python
import xarray as xr
import dask.array as da
from ml4xcube.preprocessing import assign_mask

# Example dataset
data = xr.Dataset({
    'temperature': (('time', 'lat', 'lon'), da.random.random((10, 20, 30), chunks=(5, 10, 10)))
})

# Example mask
mask_array = da.ones((10, 20, 30), chunks=(5, 10, 10))

# Assign mask to dataset without expansion
dataset_with_mask = assign_mask(data, mask_array, mask_name='custom_mask')

# Example mask
mask_array = da.ones((20, 30), chunks=(10, 10))

# Assign mask to dataset with expansion along 'time'
dataset_with_expanded_mask = assign_mask(data, mask_array, mask_name='custom_mask_2', stack_dim='time')

print(dataset_with_mask)
print(dataset_with_expanded_mask)

```

### Notes
- If the specified `stack_dim` is specified but not a dimension within the dataset, a `ValueError` is raised. 
- This function ensures that the mask is expanded and rechunked appropriately to match the dataset's dimensions and chunk sizes, facilitating efficient computations on large datasets. 
- The mask is added to the dataset as a new data variable using the specified `mask_name`, or defaults to `filter_mask` if no name is provided
