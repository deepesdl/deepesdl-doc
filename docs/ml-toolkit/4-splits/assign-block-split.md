## assign_block_split

```python
def assign_block_split(ds: xr.Dataset, block_size: List[Tuple[str, int]] = None, split: float = 0.8) -> xr.Dataset
```

### Description
Assigns blocks of data to training or testing sets based on a specified split ratio. 
This method uses a deterministic random seed generated from the indices of each block, ensuring that the same blocks are consistently assigned to the same subset across different runs, given the same initial conditions.

### Parameters
- **ds** (`xarray.Dataset`): The input dataset.
- **block_size** (`List[Tuple[str, int]]`): List of tuples specifying the dimensions and their respective sizes for block division. If `None`, chunk sizes are inferred from the dataset.
- **split** (`float`): The fraction of data to assign to the training set. The remainder is assigned to the testing set. Default is `0.8`.

### Returns
- `xarray.Dataset`: The dataset with an added 'split' variable that indicates whether each block belongs to the training set (`1.`) or the testing set (`0.`).

### Example

```python
import numpy as np
import xarray as xr
from ml4xcube.data_split import assign_block_split

# Example dataset
data = xr.Dataset({'temperature': (('time', 'lat', 'lon'), np.random.rand(10, 2, 3))})
block_size = [('time', 5), ('lat', 2), ('lon', 3)]
split_dataset = assign_block_split(data, block_size)
print(split_dataset)
```

<p align="center">
<img src="../train_test_assignment_bs.png" width="70%" height="70%">
</p>
<p align = "center"><i>
Block Assignment of Train/Test Split</i>
</p>