## get_statistics

```python
def get_statistics(ds: Union[xr.Dataset, Dict[str, np.ndarray]], exclude_vars:List[str] = list()) -> Dict[str, List[float]]
```

### Description
The `get_statistics` function calculates and returns the mean and standard deviation for all variables in an 
`xarray.Dataset` or a dictionary of numpy arrays, except for specified variables to exclude. This function is 
useful for statistical analysis and data standardization, where mean and standard deviation are essential for tasks 
such as feature scaling.

### Parameters
- **ds** (`Union[xarray.Dataset, Dict[str, numpy.ndarray]]`):  The dataset to analyze, which can be provided either as an xarray dataset or a dictionary where keys are variable names and values are numpy arrays.
- **exclude_vars** (`List[str]`): A list of variable names to exclude from the statistical calculations. This can be useful for ignoring non-analytical variables like identifiers or masks.


### Returns
- `Dict[str, List[float]]`: A dictionary where each key is a variable name and the value is a list containing the mean and standard deviation of that variable.

### Example

```python
import numpy as np
import xarray as xr
from ml4xcube.preprocessing import get_statistics

# Example dataset
ds = xr.Dataset({
    'temperature': (('time', 'lat', 'lon'), np.random.rand(10, 20, 30)),
    'precipitation': (('time', 'lat', 'lon'), np.random.rand(10, 20, 30)),
    'land_mask': (('lat', 'lon'), np.random.randint(0, 2, size=(20, 30)))
})

# Exclude the 'land_mask' variable from statistical calculations
stats = get_statistics(ds, exclude_vars=['land_mask'])

# Output the calculated statistics
for var, values in stats.items():
    print(f"{var} - Mean: {values[0]}, Standard Deviation: {values[1]}")
```
A random dataset is created. Subsequently the mean and standard deviation for the standardization of the variable `temperature`.

