## undo_normalizing

```python
def undo_normalizing(x: np.ndarray, xmin: float, xmax: float) -> np.ndarray
```

### Description
This function performs the inverse operation of normalization, transforming normalized data back to its original scale.

### Parameters
- **ds** (`numpy.ndarray`): The normalized array.
- **xmin** (`str`): The minimum value used for the original normalization.
- **xmax** (`bool`): The maximum value used for the original normalization.
- 
### Returns
- `numpy.ndarray`:  The denormalized array.

### Example

```python
import numpy as np
import xarray as xr
from ml4xcube.postprocessing import undo_normalization
from ml4xcube.preprocessing import get_range, normalize

# Example dataset
ds = xr.Dataset({
    'temperature': (('time', 'lat', 'lon'), np.random.rand(10, 20, 30)),
    'precipitation': (('time', 'lat', 'lon'), np.random.rand(10, 20, 30))
})

# Get the range of the 'temperature' variable
temperature_range = get_range(ds, 'temperature')
print(f"Temperature range: {temperature_range}")

# Normalize the 'temperature' variable
normalized_temperature = normalize(ds['temperature'].values, *temperature_range)
print(f"Normalized temperature: {normalized_temperature}")

# Revert the normalization
original_temperature = undo_normalization(normalized_temperature, *temperature_range)
```
This example demonstrates how to revert normalized data back to its original scale using the `undo_normalizing` function.