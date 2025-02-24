## drop_nan_values

```python
def drop_nan_values(ds: Dict[str, np.ndarray], vars: List[str], mode: str = 'auto', filter_var: str = 'filter_mask') -> Dict[str, np.ndarray]
```

### Description
The `drop_nan_values` function filters out samples containing `NaN` values from a dataset, using various modes to determine how NaNs affect the data inclusion. This function is applicable to datasets represented as dictionaries of numpy arrays. It can handle both lists of points and multi-dimensional arrays. Additionally, it can utilize a mask variable from the dataset to define valid data points, aligning the filtering process with specific validity conditions dictated by the mask.
### Parameters
- **ds** (`Dict[str, numpy.ndarray]`): The dataset to filter, provided as a dictionary where keys are variable names and values are numpy arrays.
- **vars** (`List[str]`): A list of variable names to check for `NaN` values.
- **mode** (`str`): If not `None`, specifies the method for handling areas with missing values:
  - **auto**: Drops the entire sample if any part contains a `NaN`.
  - **if_all_nan** (`List[str]`): Drops the sample only if it is entirely composed of `NaN`s.
  - **masked** (`List[str]`): Drops valid regions (as defined by `filter_var`) containing any `NaN`s. Requires `filter_var` to be defined.
- **filter_var** (`str`):  An optional argument specifying the name of a mask variable in the dataset. If provided, this mask is used to determine the validity of a sample.
 
### Returns
- `Dict[str, numpy.ndarray]`:  The dataset dictionary with the NaN-containing entries filtered out according to the specified mode.

### Example

```python
import numpy as np
from ml4xcube.preprocessing import drop_nan_values

# Creating a dataset with NaN values
dataset = {
    'temperature': np.random.rand(10, 20, 30),
    'precipitation': np.random.rand(10, 20, 30),
    'filter_mask': np.random.choice([True, False], size=(10, 20, 30))
}
dataset['temperature'][0, 0, 0] = np.nan
dataset['precipitation'][1, 1, 1] = np.nan

# Specifying the variables to check for NaNs
variables = ['temperature', 'precipitation']

# Filter the dataset in 'auto' mode
filtered_ds_auto = drop_nan_values(dataset, vars=variables, mode='auto')

# Filter the dataset in 'masked' mode using a filter mask
filtered_ds_masked = drop_nan_values(dataset, vars=variables, mode='masked', filter_var='filter_mask')

```
The `drop_nan_values` function filters out samples containing `NaN` values from the dataset. If a `filter_var` is provided, it also uses this mask to determine the validity of the samples.
If values are considered relevant according to the mask (`True`), samples containing containing `NaN` values in these specific regions are dropped. 
If no relevant values according to the filter mask exist the sample is also dropped.

### Notes
- The function provides flexible handling of NaN values, with the ability to adjust the strictness of filtering through the `mode` parameter. 
- When the `mode` is `masked`, the function checks for NaNs specifically in areas deemed valid by the `filter_var`. If any valid area contains a NaN, the whole subarray is considered invalid. 
- For datasets with dimensions of 1 (lists of points), NaNs are dropped individually. For higher dimensions (2, 3, or 4), the function can operate by checking across the specified axes, contingent on the selected mode.

