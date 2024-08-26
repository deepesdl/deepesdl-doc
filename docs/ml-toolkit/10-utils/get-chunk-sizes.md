## get_chunk_sizes

```python
def get_chunk_sizes(ds: xr.Dataset) -> List[Tuple[str, int]]
```

### Description
The maximum chunk sizes for all data variables in a given `xarray.Dataset` is determined. This allows to understand the chunking scheme of the dataset and for setting up consistent chunk sizes for processing.

### Parameters
- **ds** (`xarray.Dataset`): The dataset for which the maximum chunk sizes are to be determined. The dataset should have dimensions that can be chunked.

### Returns
- `List[Tuple[str, int]]`: A list of tuples where each tuple contains a dimension name (str) and its corresponding maximum chunk size (int) over all variables.

### Example

```python
import numpy as np
import xarray as xr
from ml4xcube.utils import get_chunk_sizes

# Example dataset with chunking
data = np.random.rand(100, 200, 300)
ds = xr.Dataset({
    'temperature': (('time', 'lat', 'lon'), data),
    'precipitation': (('time', 'lat', 'lon'), data)
}).chunk({'time': 10, 'lat': 20, 'lon': 30})

# Get maximum chunk sizes
chunk_sizes = get_chunk_sizes(ds)
print(chunk_sizes)
```

In this example, the `get_chunk_sizes` function returns the chunk sizes for each dimension in the dataset.

### Notes
- The function iterates over all data variables in the dataset and retrieves their chunk sizes.
- If the variable has chunk sizes, it calculates the maximum chunk size for each dimension.
- The returned list contains tuples with dimension names and their maximum chunk sizes, which can be used for further processing.