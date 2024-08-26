## assign_rand_split

```python
def assign_rand_split(ds: xr.Dataset, split: float = 0.8) -> xr.Dataset
```

### Description
Randomly assigns a training/test split indicator to each element in an `xarray.Dataset` based on a specified split ratio. This method ensures that the distribution of training and testing data is balanced across the entire dataset.

### Parameters
- **ds** (`xarray.Dataset`): The input dataset.
- **split** (`float`):  The proportion of the dataset to be used for training. Defaults to `0.8`.

### Returns
- `xarray.Dataset`: The dataset with an additional 'split' variable indicating the random split, where `1.` represents training data and `0.` represents testing data.


### Example

```python
import numpy as np
import xarray as xr
from ml4xcube.data_split import assign_rand_split

# Example dataset
data = xr.Dataset({'temperature': (('time', 'lat', 'lon'), np.random.rand(10, 2, 3))})
split_dataset = assign_rand_split(data, 0.7)
print(split_dataset)
```

In the example, each point in the dataset is randomly assigned to the train set with a 70% probability or to the test set 
with a 30% probability. The random split is demonstrated in the image below:

<p align="center">
<img src="../../img/train_test_assignment_rnd.png" width="70%" height="70%">
</p>
<p align = "center"><i>
Random Assignment of Train/Test Split</i>
</p>