## undo_normalizing

```python
def undo_standardizing(x: np.ndarray, xmean: float, xstd: float) -> np.ndarray
```

### Description
This function performs the inverse operation of standardization, transforming standardized data back to its original scale.

### Parameters
- **ds** (`numpy.ndarray`): The standardized array.
- **xmean** (`str`): The mean value used for the original standardization.
- **xstd** (`bool`): The standard deviation value used for the original standardization.
- 
### Returns
- `numpy.ndarray`:  The destandardized array.

### Example

```python
import numpy as np
import xarray as xr
from ml4xcube.postprocessing import undo_standardization
from ml4xcube.preprocessing import get_statistics, standardize

# Example dataset
ds = xr.Dataset({
    'temperature': (('time', 'lat', 'lon'), np.random.rand(10, 20, 30)),
})

# Calculate statistics
statistics = get_statistics(ds, 'temperature')

print(f"Mean: {statistics[0]}, Standard Deviation: {statistics[1]}")

# Standardize the 'temperature' variable
standardized_temperature = standardize(ds['temperature'].values, *statistics)
print(f"Normalized temperature: {standardized_temperature}")

# Revert the standardization
original_temperature = undo_standardization(standardized_temperature, *statistics)
```
This example demonstrates how to revert standardized data back to its original scale using the `undo_standardizing` function.