## standardize

```python
def standardize(ds: Union[xr.Dataset, Dict[str, np.ndarray]], stats_dict: Dict[str, List[float]], filter_var: str = None) -> Union[xr.Dataset, Dict[str, np.ndarray]]
```

### Description
The `standardize` function performs standardization fpr all variables within an `xarray.Dataset` or a dictionary of 
NumPy arrays, contained in the `stats_dict` dictionary. This dictionary provides mean and standard deviation values. 
This standardization process adjusts each data point 
so that the resulting distribution of each variable has a mean of 0 and a standard deviation of 1. This is crucial for 
many statistical analyses and machine learning models to ensure that features have comparable scales without biasing 
the model due to the variance in magnitude. Variables specified by `filter_var` are excluded from standardization, which 
is beneficial for non-data variables like masks or indices.

### Parameters
- **ds** (`Union[xarray.Dataset, Dict[str, numpy.ndarray]]`): The dataset to standardize. It can either be an `xarray.Dataset` or a dictionary where keys are variable names and values are NumPy arrays.
- **stats_dict** (`Dict[str, List[float]]`): A dictionary containing the minimum and maximum values (`xmin`, `xmax`) for each variable that requires normalization.
- **filter_var** (`str`): The name of a variable to exclude from normalization. This is useful for excluding non-data variables like mask or index fields.

### Returns
- `Union[xarray.Dataset, Dict[str, numpy.ndarray]]`: The standardized dataset. The data structure returned depends on the input; it will return an `xarray.Dataset` if provided with one, otherwise it will return a dictionary.

### Example

```python
import numpy as np
import xarray as xr
from preprocessing import get_statistics, standardize

# Creating an example dataset
ds = xr.Dataset({
    'temperature': (('time', 'lat', 'lon'), np.random.rand(10, 20, 30)),
    'humidity': (('time', 'lat', 'lon'), np.random.rand(10, 20, 30)),
    'land_mask': (('time', 'lat', 'lon'), np.random.randint(0, 2, size=(10, 20, 30)))
})

# Calculate statistics for 'temperature' and 'humidity'
stats = get_statistics(ds, exclude_vars=['land_mask'])
print("Statistics calculated:", stats)

# Standardize the dataset, excluding 'land_mask' from standardization
standardized_ds = standardize(ds, stats, filter_var='land_mask')
print("Standardized Dataset:")
for var in ['temperature', 'humidity']:
    print(f"Standardized {var}: mean={np.mean(standardized_ds[var].values)}, std={np.std(standardized_ds[var].values)}")
```
A random dataset is created. Subsequently the mean and standard deviation are used for the standardization of 
`temperature` and `humidity` variables.

### Notes
- Standardization is carried out by subtracting the mean and dividing by the standard deviation. If the standard deviation is zero (indicating no variability within the variable), the variable values are reduced by the mean alone since division by zero is not feasible.
- This function supports excluding specific variables from the standardization process, which is especially useful for preserving the integrity of certain types of data like binary masks or categorical indices. 
- The function intelligently handles both `xarray.Dataset` and dictionary formats, making it versatile for different data handling contexts in scientific computing and machine learning.
