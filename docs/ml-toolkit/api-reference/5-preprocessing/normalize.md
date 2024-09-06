## normalize

```python
def normalize(ds: Union[xr.Dataset, Dict[str, np.ndarray]], range_dict: Dict[str, List[float]], filter_var: str = None) -> Union[xr.Dataset, Dict[str, np.ndarray]]:
```

### Description
The `normalize`  function applies min-max scaling to each variable within an `xarray.Dataset` or a dictionary of numpy 
arrays, contained within the `range_dict` dictionary. This dictionary specifies range values for this operation. 
This scaling adjusts each data point to a [0, 1] range, 
based on the minimum (`xmin`) and maximum (`xmax`) values for each variable. This method is essential for scaling input data in 
various data processing and machine learning tasks, ensuring that each variable contributes equally without bias due 
to different scales. A variable specified as `filter_var` is excluded from normalization, which can be useful for 
variables, like mask indicators or filters.

### Parameters
- **ds** (`Union[xarray.Dataset, Dict[str, np.ndarray]]`): The dataset to normalize. It can either be an `xarray.Dataset` or a dictionary where keys are variable names and values are NumPy arrays.
- **range_dict** (`Dict[str, List[float]]`): A dictionary containing the minimum and maximum values (`xmin`, `xmax`) for each variable that requires normalization.
- **filter_var** (`str`): The name of a variable to exclude from normalization. This is useful for excluding non-data variables like mask or index fields.

### Returns
- `numpy.ndarray`: The normalized array, with values scaled to the range [0, 1].

### Example

```python
import numpy as np
import xarray as xr
from preprocessing import get_range, normalize

# Creating an example dataset
ds = xr.Dataset({
    'temperature': (('time', 'lat', 'lon'), np.random.rand(10, 20, 30)),
    'humidity': (('time', 'lat', 'lon'), np.random.rand(10, 20, 30)),
    'land_mask': (('time', 'lat', 'lon'), np.random.randint(0, 2, size=(10, 20, 30)))
})

# Calculate the range for 'temperature' and 'humidity'
ranges = get_range(ds, exclude_vars=['land_mask'])
print("Ranges calculated:", ranges)

# Normalize the dataset, excluding 'land_mask' from normalization
normalized_ds = normalize(ds, ranges, filter_var='land_mask')
print("Normalized Dataset:")
print(normalized_ds)

```
In this example, the `get_range` function is used to retrieve the minimum and maximum values for the 'temperature' and 'precipitation' variables in an xarray dataset. These ranges are then used by the `normalize` function to scale the data to the range [0, 1].
