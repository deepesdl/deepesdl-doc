## apply_filter

```python
def apply_filter(ds: Dict[str, np.ndarray], filter_var: str, drop_sample: bool = False) -> Dict[str, np.ndarray]
```

### Description
The `apply_filter` function applies a filter to a dataset. If `drop_sample` is True and any value in a sample does not belong to the mask (`False`), the function drops the entire sample. If `drop_sample` is `False`, it sets all values to `NaN` that do not belong to the mask (`False`). For lists of points, it keeps the current behavior of dropping single values.

### Parameters
- **ds** (`Dict[str, numpy.ndarray]`): The dataset to filter. It should be a dictionary where keys are variable names and values are numpy arrays.
- **filter_var** (`str`): The variable name to use as the filter mask, which must be contained in the dataset.
- **drop_sample** (`bool`): A boolean flag to determine whether to drop the entire subarray or set values to `NaN`.
- 
### Returns
- `Dict[str, numpy.ndarray]`: The dataset after filtering NaN values as a dictionary where keys are variable names and values are filtered numpy arrays.

### Example

```python
import numpy as np
from ml4xcube.preprocessing import apply_filter
from ml4xcube.cube_utilities import split_chunk

# Example dataset
chunk = {
    'temperature': np.random.rand(10, 20, 30),
    'precipitation': np.random.rand(10, 20, 30),
    'filter_mask': np.random.choice([True, False], size=(10, 20, 30))
}

# Split the chunk
split_data = split_chunk(chunk, sample_size=[('time', 1), ('lat', 2), ('lon', 2)], overlap=[('time', 0.5), ('lat', 0.5), ('lon', 0.5)])

# Apply the filter with drop_sample set to True
filtered_ds = apply_filter(split_data, filter_var='filter_mask', drop_sample=True)

# Apply the filter with drop_sample set to False
filtered_ds_nan = apply_filter(split_data, filter_var='filter_mask', drop_sample=False)

```
The `apply_filter` function applies the filter mask to the dataset. Depending on the value of `drop_sample`, it either drops entire subarrays or sets invalid values to `NaN`.

### Notes
- The `filter_var` parameter specifies the variable used as the filter mask. Ensure this variable exists in the dataset.
- If `drop_sample` is `True`, the function drops entire subarrays if any value does not belong to the mask.
- If `drop_sample` is `False`, the function sets invalid values to `NaN`.
- The function handles lists of points separately by dropping single values if they are `NaN`.