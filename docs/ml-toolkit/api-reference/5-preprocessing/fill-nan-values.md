## fill_masked_data

```python
def fill_nan_values(ds: Dict[str, np.ndarray], vars: List[str], method: str = 'mean', const: Union[float, str, bool] = None) ->  Union[Dict[str, np.ndarray], xr.Dataset]
```

### Description

The `fill_nan_values` function fills `NaN` values in the dataset using a specified method. The methods available are 'mean', 'noise', or 'constant'. Depending on the method, `NaN` values are replaced with the mean of non-`NaN` values, random noise within the range of non-`NaN` values, or a specified constant value.
In some cases in certain areas no values are intended (e.g. where mask values `False`). To incorporate samples containing boundaries (like coastlines in ESDC), the `fill_masked_data` function can be utilized to prepare the data for masked machine learning. This approach is demonstrated in this [jupyter notebook](https://github.com/deepesdl/ML-Toolkits/blob/master/Examples/use_case_lst_at_pytorch_mlflow.ipynb).

### Parameters

- **ds** (`Union[Dict[str, numpy.ndarray], xarray.Dataset]`): The dataset to fill. It should be a dictionary or `xarray.Dataset` where keys are variable names and with the values containing the data to fill.
- **vars** (`List[str]`): The list of variables for which to fill NaN values. These variables should be present in the dataset.
- **method** (`str`): The method to use for filling NaN values. Options are `mean`, `sample_mean`, `noise`, `constant`, or None.
  - **None**: `NaN`s are not filled.
  - **mean**: `NaN`s are filled with the mean value of the non-`NaN` values
  - **sample_mean**: `NaN`s are filled with the sample mean value.
  - **noise**: `NaN` are filled with random noise within the range of the non-`NaN` values.
  - **constant**: `NaN`s are filled with the specified constant value (`const`).
- **const** (`Union[float, str, bool]`): The constant value to use for filling `NaN` values when the method is 'constant'. This parameter is required when the method is 'constant'.
-

### Returns

- ` Union[Dict[str, numpy.ndarray], xarray.Dataset]`: The dataset with `NaN` values filled, where keys are variable names and values are NumPy arrays with filled data.

### Example

```python
import numpy as np
from ml4xcube.preprocessing import fill_nan_values

# Example dataset
ds = {
    'temperature': np.random.rand(10, 20, 30),
    'precipitation': np.random.rand(10, 20, 30)
}

# Introduce some NaN values
ds['temperature'][0, 0, 0] = np.nan
ds['precipitation'][1, 1, 1] = np.nan

# Fill NaN values using the mean method
filled_ds_mean = fill_nan_values(ds, vars=['temperature', 'precipitation'], method='mean')

# Fill NaN values using the noise method
filled_ds_noise = fill_nan_values(ds, vars=['temperature', 'precipitation'], method='noise')

# Fill NaN values using a constant value
filled_ds_constant = fill_nan_values(ds, vars=['temperature', 'precipitation'], method='constant', const=0.0)


```

In this example, the `fill_nan_values` function fills the NaN values in the dataset using different methods: 'mean', 'noise', and 'constant'.

### Notes

- The `vars` parameter specifies the list of variables for which to fill `NaN` values. Ensure these variables exist in the dataset.
- When using the 'constant' method, the `const` parameter must be provided to specify the constant value for filling `NaNs`.
- The function handles both single-dimensional and multi-dimensional arrays for filling `NaN` values.
