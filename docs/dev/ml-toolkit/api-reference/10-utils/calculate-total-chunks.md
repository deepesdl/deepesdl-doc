## calculate_total_chunks

```python
def calculate_total_chunks(ds: xr.Dataset, block_size: List[Tuple[str, int]] = None) -> int
```

### Description
The total number of chunks for an `xarray.Dataset` is calculated based on specified or default chunk sizes. 

### Parameters
- **ds** (`xarray.Dataset`): The dataset for which the total number of chunks will be calculated. The dataset should have dimensions that can be chunked.
- **block_size** (`Optional[List[Tuple[str, int]]]`): A sequence of tuples specifying the block size for each dimension. Each tuple should contain a dimension name and a block size for that dimension. If not provided, the function will use the dataset's default chunk sizes.

### Returns
- `int`: The total number of chunks in the dataset based on the specified or default chunk sizes.

### Example

```python
import numpy as np
import xarray as xr
from ml4xcube.utils import calculate_total_chunks

# Example dataset
data = np.random.rand(100, 200, 300)
ds = xr.Dataset({
    'temperature': (('time', 'lat', 'lon'), data),
    'precipitation': (('time', 'lat', 'lon'), data)
})

# Define the block size (chunk size)
block_size = [('time', 10), ('lat', 20), ('lon', 30)]

# Calculate total chunks
total_chunks = calculate_total_chunks(ds, block_size=block_size)
print(f"Total number of chunks: {total_chunks}")
```
Based on the specified blocks the number of chunks is calculated.

### Notes

- The `block_size` parameter allows you to specify custom chunk sizes. If not provided, the function will use the dataset's default chunk sizes.
- Ensure that the provided `block_size` values are appropriate for the dimensions of the dataset.