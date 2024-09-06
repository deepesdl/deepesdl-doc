## split_chunk

```python
def split_chunk(chunk: Dict[str, np.ndarray], sample_size: List[Tuple[str, int]] = None,
                overlap: List[Tuple[str, float]] = None) -> Dict[str, np.ndarray]
```

### Description
The `split_chunk` function splits a given chunk of data into smaller data samples or points based on the provided sample size and optional overlap configurations. This function is useful for data preprocessing, particularly when dealing with large datasets that need to be divided into manageable parts for analysis or model training.

### Parameters
- **chunk** (`Dict[str, numpy.ndarray]`): A dictionary where keys are variable names and values are NumPy arrays representing the data chunk to be split.
- **sample_size** (`List[Tuple[str, int]]`): A list of tuples specifying the sample size for each dimension. Each tuple consists of a dimension name (str) and the corresponding sample size (int). If `None` the chunk is split into points.
- **overlap** (`List[Tuple[str, float]]`): A list of tuples specifying the overlap for overlapping samples due to chunk splitting. Each tuple consists of a dimension name (str) and the overlap percentage (float) between 0 and 1. If `None`, the resulting samples don't overlap.

### Returns
- `Dict[str, np.ndarray]`: A dictionary where keys are variable names and values are NumPy arrays containing the split data samples or points.

### Example

```python
import numpy as np
from ml4xcube.utils import split_chunk

# Example chunk data
chunk = {
    'temperature': np.random.rand(10, 10, 10),
    'precipitation': np.random.rand(10, 10, 10)
}

# Split the chunk
split_data = split_chunk(chunk, sample_size=[('time', 5), ('lat', 5), ('lon', 5)], overlap=[('time', 0.5), ('lat', 0.5), ('lon', 0.5)])
print(split_data)

```

The above code splits the chunk of data into smaller samples based on the specified sample size and optional overlap, resulting in a dictionary with the split data for each variable.

### Notes
- The `overlap` parameter allows you to specify overlapping regions between the samples, which can be useful for certain types of analyses or training machine learning models where context from neighboring samples is important.
- Ensure that the specified `sample_size` and overlap values are appropriate for the dimensions and size of the input chunk to avoid errors or unexpected behavior.