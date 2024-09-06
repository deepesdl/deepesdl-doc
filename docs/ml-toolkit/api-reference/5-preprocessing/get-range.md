## get_range

```python
def get_range(ds: Union[xr.Dataset, Dict[str, np.ndarray]], exclude_vars:List[str] = list()) -> Dict[str, List[float]]
```

### Description
The `get_range` function computes the minimum and maximum values for all variables within an `xarray.Dataset` or a 
dictionary of `numpy` arrays, excluding specified variables. This utility is useful for preprocessing 
tasks like normalization where knowing the range of data values is crucial. Users can specify certain variables to 
exclude from the range calculations, such as mask variables that do not represent the actual data range of interest.

### Parameters
- **ds** (`Union[xarray.Dataset, Dict[str, numpy.ndarray]]`): The dataset to analyze, provided either as an xarray dataset or a dictionary where keys are variable names and values are numpy arrays.
- **exclude_vars** (`List[str]`): List of variable names to exclude from the range calculations. Useful for ignoring auxiliary or non-data variables like masks or identifiers.

### Returns
- `Dict[str, List[float]]`: A dictionary where each key is a variable name and the value is a list containing the minimum and maximum values of that variable.

### Example

```python
import numpy as np
import xarray as xr
from ml4xcube.preprocessing import get_range

# Example dataset
ds = xr.Dataset({
    'temperature': (('time', 'lat', 'lon'), np.random.rand(10, 20, 30)),
    'precipitation': (('time', 'lat', 'lon'), np.random.rand(10, 20, 30)),
    'land_mask': (('lat', 'lon'), np.random.randint(0, 2, size=(20, 30)))
})

# Exclude the 'land_mask' variable from range calculations
ranges = get_range(ds, exclude_vars=['land_mask'])

# Output the calculated ranges
for var, r in ranges.items():
    print(f"{var} range: {r}")

# Example of how these ranges might be used for normalization
normalized_datasets = {var: (ds[var] - r[0]) / (r[1] - r[0]) for var, r in ranges.items()}

# Display normalized datasets
for var, data in normalized_datasets.items():
    print(f"Normalized {var}: {data}")

```
In this example, the `get_range` function is used to retrieve the minimum and maximum values for the `temperature` and 
`precipitation` variables in an `xarray.Dataset`. These ranges are then used by the `normalize` function to scale the 
data to the range `[0, 1]`.
