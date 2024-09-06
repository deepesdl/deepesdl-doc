## iter_data_var_blocks

```python
def iter_data_var_blocks(ds: xr.Dataset, block_size: List[Tuple[str, int]] = None) -> Iterator[Dict[str, np.ndarray]]
```

### Description
An iterator that provides all data blocks of all data variables in the given dataset is created. Allows iterating over chunks.

### Parameters
- **ds** (`xarray.Dataset`): The dataset to iterate over
- **block_size** (`List[Tuple[str, int]]`): A sequence of tuples specifying the block size for each dimension. Each tuple should contain a dimension name and a block size for that dimension. If not provided, the function will use the dataset's default chunk sizes.

### Yields
- `Iterator[Dict[str, numpy.ndarray]]`: An iterator of dictionaries where keys are variable names from the dataset and values are data blocks as NumPy arrays. Each iteration yields a dictionary representing a single data block for all variables.

### Example

```python
import numpy as np
import xarray as xr
from ml4xcube.utils import iter_data_var_blocks

# Example dataset
data = np.random.rand(100, 200, 300)
ds = xr.Dataset({
    'temperature': (('time', 'lat', 'lon'), data),
    'precipitation': (('time', 'lat', 'lon'), data)
})

# Define the block size (chunk size)
block_size = [('time', 10), ('lat', 20), ('lon', 30)]

# Iterate over data blocks
for block in iter_data_var_blocks(ds, block_size=block_size):
    for var_name, chunk in block.items():
        print(f"{var_name} chunk shape: {chunk.shape}")
```
The `iter_data_var_blocks` function iterates over the dataset, yielding chunks of data according to the specified block sizes.

### Notes

- The `block_size` parameter allows you to specify custom chunk sizes. If not provided, the function will use the dataset's default chunk sizes.
- Ensure that the provided `block_size` values are appropriate for the dimensions of the dataset.