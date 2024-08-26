## create_split

```python
def create_split(
        data: Union[xr.Dataset, Dict[str, np.ndarray]], to_pred: Union[List[str], str] = None,
        exclude_vars: List[str] = list(), feature_vars: List[str] = None, stack_axis: int = -1
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]
```

### Description
The `create_split` function efficiently generates train-test splits for machine learning models by using a predefined 
`split` variable within a dataset. This method supports inputs in the form of either `xarray.Dataset` or a dictionary of `numpy` arrays. 
It allows for flexible specification of feature and target variables, along with optional exclusions and custom stacking 
configurations for input dimensions.

### Parameters
- **data** (`Union[xr.Dataset, Dict[str, np.ndarray]]`): The data set from which to generate the split, provided either as an xarray dataset or a dictionary of variables.
- **to_pred** (`Union[List[str], str]`):  Names of the variables to be used as targets. Can be a single string or a list of strings.
- **exclude_vars** (`List[str]`):  Names of the variables to exclude from the feature set. Defaults to an empty list.
- **feature_vars** (`List[str]`):  Explicit list of variable names to use as features. If `None`, the function automatically determines which variables to use based on exclusion criteria and target variables.

### Returns
- `Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]`: A tuple containing numpy arrays for training features, testing features, training targets, and testing targets.

### Example

```python
import numpy as np
from ml4xcube.splits import create_split

# Example data setup
data = {
    'temperature': np.random.rand(100, 10),
    'humidity': np.random.rand(100, 10),
    'split': np.random.choice([0., 1.], size=(100,))
}

# Specify the variables to predict and the feature set
to_predict = 'temperature'
features = ['humidity']

# Create train and test splits
X_train, X_test, y_train, y_test = create_split(data, to_pred=to_predict, feature_vars=features)

print('Training features shape:', X_train.shape)
print('Training labels shape:', y_train.shape)

```
This example illustrates the use of `create_split` to prepare data arrays for training and testing a model, where 
`temperature` is the target variable and `humidity` serves as a feature variable. 
The `split` variable within the data cube specifies which entries belong to the training set (1.) and which to the testing set (0.).
It can be assigned using the [assign_block_split](assign-block-split.md) or the [assign_rand_split](assign-rand-split.md)
method.
