## get_chunk_by_index

```python
def get_chunk_by_index(ds: xr.Dataset, index: int, block_size: List[Tuple[str, int]] = None) -> Dict[str, np.ndarray]
```

### Description
`get_chunk_by_index` retrieves a specific data chunk from an `xarray.Dataset` based on a given linear index. This way the extraction of subsets is feasible. Further the chunks of a cube can be iterated.

### Parameters
- **ds** (`xarray.Dataset`): The `xarray.Dataset` from which to retrieve a chunk.
- **index** (`int`): The index of the chunk to retrieve. This index will be converted to a multi-dimensional index based on the chunk sizes.
- **block_size** (`List[Tuple[str, int]]`): An optional list of tuples specifying the block size for each dimension. Each tuple should contain a dimension name and a block size for that dimension. A chunk with the specified block sizes will be returned. If not provided, the function will use the dataset's default chunk sizes.
### Returns
- `Dict[str, np.ndarray]`: A dictionary where keys are variable names from the dataset and values are NumPy arrays containing the data of the specified chunk.

### Example

```python
import numpy as np
import xarray as xr
from ml4xcube.utils import get_chunk_by_index

# Example dataset
data = np.random.rand(100, 200, 300)
ds = xr.Dataset({
    'temperature': (('time', 'lat', 'lon'), data),
    'precipitation': (('time', 'lat', 'lon'), data)
})

# Define the block size (chunk size)
block_size = [('time', 10), ('lat', 20), ('lon', 30)]

# Get the 5th chunk (index starts from 0)
chunk_data = get_chunk_by_index(ds, index=5, block_size=block_size)

# Output the chunk data
for var_name, chunk in chunk_data.items():
    print(f"{var_name} chunk shape: {chunk.shape}")

```
The `get_chunk_by_index` function retrieves the 5th chunk from the dataset, using the specified block sizes for each dimension.
