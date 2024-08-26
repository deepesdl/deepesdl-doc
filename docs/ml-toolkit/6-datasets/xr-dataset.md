## XrDataset

The `XrDataset` class within the `datasets.xr_dataset` module is specifically tailored to sample smaller datasets that are manageable in memory. 
It is created for scenarios where direct, rapid manipulation of data in memory is feasible and preferable over the more complex, disk-based operations typical of very large datasets. 
This capability makes it ideal for machine learning applications where dataset size allows for quick iterations and immediate feedback on preprocessing and modeling efforts.
This class aims provides tools to selectively process data chunks based on specified criteria and apply data cleaning operations such as NaN value handling and optional filtering based on specific variables.
It efficiently concatenates processed chunks into a single dataset for further analysis or model training.
### Constructor

```python
def __init__(self, ds: xr.Dataset, chunk_indices: List[int] = None, rand_chunk: bool = True, drop_nan: str = 'auto',
             apply_mask: bool = True, drop_sample: bool = False, fill_method: str = None, const: float = None,
             filter_var: str = 'filter_mask', patience: int = 500, block_size: List[Tuple[str, int]] = None,
             sample_size: List[Tuple[str, int]] = None, overlap: List[Tuple[str, float]] = None, callback: Callable = None,
             num_chunks: int = None, to_pred: Union[str, List[str]] = None, scale_fn: str = 'standardize'):
```

#### Parameters
   - **ds** (`xarray.Dataset`): The input dataset to extract the training samples from.
   - **chunk_indices** (`List[int]`): List of indices specifying which chunks to process.
   - **rand_chunk** (`bool`): If True, chunks are selected randomly; otherwise, they are processed sequentially.
   - **drop_nan** (`str`): If not `None`, specifies the method for handling areas with missing values:
     - **auto**: Drops the entire sample if any part contains a `NaN`.
     - **if_all_nan** (`List[str]`): Drops the sample only if it is entirely composed of `NaN`s.
     - **masked** (`List[str]`): Drops valid regions (as defined by `filter_var`) containing any `NaN`s. Requires `filter_var` to be defined.
   - **apply_mask** (`bool`): Whether to apply a filtering condition to the data chunks.
   - **drop_sample** (`bool`): If True, drops any samples that doesn't contain relevant values according to the `filter_var` criteria completely.
   - **fill_method** (`str`): Method used to fill masked or NaN data.
     - **None**: `NaN`s are not filled.
     - **mean**: `NaN`s are filled with the mean value of the non-`NaN` values
     - **sample_mean**: `NaN`s are filled with the sample mean value.
     - **noise**: `NaN` are filled with random noise within the range of the non-`NaN` values.
     - **constant**: `NaN`s are filled with the specified constant value (`const`).
   - **const** (`float`): Constant value used when fill_method is 'constant'.
   - **filter_var** (`str`): Filter mask name used for filtering data chunks.
   - **patience** (`int`): The number of consecutive iterations without a valid chunk before stopping.
   - **block_size** (`List[Tuple[str, int]]`): Size of the chunks to process, which can define memory usage and performance. If `None` the chunk size of ds is utilized.
   - **sample_size** (`List[Tuple[str, int]]`): List of tuples specifying the sizes of the resulting dataset's samples
   - **overlap** (`List[Tuple[str, float]]`): List of tuples specifying the overlap proportion of the resulting dataset's samples
   - **callback** (`Callable`): Optional function applied to each chunk after initial processing.
   - **num_chunk** (`int`):  Specifies the number of chunks to process if not processing all.
   - **to_pred** (`Union[str, List[str]]`): Variable or list of variables to construct the dependent variable or sample to predict.
   - **scale_fn** (`str`): Feature scaling function to apply (`standardize`, `normalize`, or `None`).

### get_datasets
Retrieves the fully processed dataset, ready for use in applications or further analysis. This method ensures that all preprocessing steps are applied and the data is returned in a manageable format.

```python
def get_datasets(self) -> Union[Dict[str, np.ndarray], Tuple[Tuple[np.ndarray, np.ndarray], Tuple[np.ndarray, np.ndarray]]]
```
#### Parameters
- `None`: This method has no input parameters.

#### Returns
- `Union[Dict[str, np.ndarray], Tuple[Tuple[np.ndarray, np.ndarray], Tuple[np.ndarray, np.ndarray]]]`: Returns the processed dataset.
  - If `to_pred` is `None`: Returns a dictionary where keys are variable names and values are concatenated numpy arrays representing the dataset.
  - If `to_pred` is provided: Returns a tuple containing:
      (X_train, y_train): Training features and targets.
      (X_test, y_test): Testing features and targets.


### Example

```python
import numpy as np
import xarray as xr
from ml4xcube.splits import assign_block_split
from ml4xcube.datasets.xr_dataset import XrDataset

# Example dataset with chunking
data = np.random.rand(100, 200, 300)
dataset = xr.Dataset({
    'temperature': (('time', 'lat', 'lon'), data),
    'precipitation': (('time', 'lat', 'lon'), data)
}).chunk({'time': 10, 'lat': 50, 'lon': 50})

# Initialize the XrDataset
xr_dataset = XrDataset(
    ds          = dataset,
    rand_chunk  = True,
    drop_nan    = 'if_all_nan',
    fill_method = 'mean',
    sample_size = [('time', 1),('lat', 10), ('lon', 10)], 
    overlap     = [('time', 0.),('lat', 0.8), ('lon', 0.8)],
    to_pred     = 'precipitation',
    num_chunks  = 3
)

# Retrieve the processed dataset
train_data, test_data = xr_dataset.get_datasets()
```
This example demonstrates initializing the `XrDataset` class with a dataset, where chunks are randomly selected. 
`NaN` values are managed by replacing them with the sample mean, and specific sample sizes and overlaps are defined to 
create the datasets. precipitation is predicted based on temperature.
The processed train and test data is then retrieved, showcasing the class's capability to efficiently manage and 
preprocess smaller datasets suitable for machine learning models and other analytical tasks. 



### Notes
- `XrDataset` is designed in order to obtain data samples from `num_chunks` unique chunks.
- If `num_chunks` is not provided it will be set automatically determined, using `chunk_indices` if assigned or the number of total chunks in the dataset
- until `num_chunks` chunks are found containing valid data samples the `patience` parameter is used. It manages the number of attempts to find the next valid chunk before stopping.
- Sampling with `XrDataset` provides the following options:
  - Use specific chunks if `chunk_indices `are set.
  - Limit `num_chunks` to the total chunks if exceeded.
  - Default `num_chunks` to total chunks if unspecified.
  - Ensure all chunks in `num_chunks` contain valid, non-`NaN` data.