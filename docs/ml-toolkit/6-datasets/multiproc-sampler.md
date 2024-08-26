## MultiProcSampler

The `MultiProcSampler` class is a specialized component of the `datasets` module, designed to efficiently prepare large datasets for machine learning applications. 
By leveraging Python's `multiprocessing` module, this class facilitates parallel processing to handle extensive datasets rapidly and effectively. 
This class is particularly beneficial in environments where the handling and transformation of large volumes of data are required before training sophisticated machine learning models.
It applies functionality to preprocess, scale, and partition data into training and testing sets, which are then stored in an efficient format for later retrieval.

### Constructor

```python
def __init__(
   self, ds: xr.Dataset, rand_chunk: bool = False, data_fraq: float = 1.0, nproc: int = 4,
   apply_mask: bool = True, drop_sample: bool = True, fill_method: str = None, const: float = None,
   filter_var: str = 'land_mask', chunk_size: Tuple[int, ...] = None, train_cube: str = 'train_cube.zarr',
   test_cube: str = 'test_cube.zarr', drop_nan: str = 'auto', array_dims: Tuple[str, ...] = ('samples',),
   data_split: float = 0.8, chunk_batch: int = None, callback: Callable = None,
   block_size: List[Tuple[str, int]] = None, sample_size: List[Tuple[str, int]] = None,
   overlap: List[Tuple[str, float]] = None, scale_fn: str = 'standardize'
)
```

#### Parameters
   - **ds** (`xarray.Dataset`): The input dataset to extract train and test data from
   - **rand_chunk** (`bool`): If True, chunks are selected randomly; otherwise, they are processed sequentially.
   - **data_fraq** (`float`):  Fraction of the data to process, allowing for partial dataset processing.
   - **nproc** (`int`): Number of processor cores to use for parallel processing.
   - **apply_mask** (`bool`): Whether to apply a filtering condition to the data chunks.
   - **drop_sample** (`bool`): If true, `NaN` values are dropped during filter application.
   - **fill_method** (`str`): Method used to fill masked or `NaN` data.
     - **None**: `NaN`s are not filled.
     - **mean**: `NaN`s are filled with the mean value of the non-`NaN` values
     - **sample_mean**: `NaN`s are filled with the sample mean value.
     - **noise**: `NaN` are filled with random noise within the range of the non-`NaN` values.
     - **constant**: `NaN`s are filled with the specified constant value (`const`).
   - **const** (`float`): Constant value used when fill_method is 'constant'.
   - **filter_var** (`str`): Variable name used for filtering data chunks.
   - **chunk_size** (`Tuple[int, ...]`): The size of chunks in the generated training and testing data.
   - **train_cube** (`str`): Path where training data are stored as `zarr` datasets.
   - **test_cube** (`str`): Path where test data are stored as `zarr` datasets.
   - **drop_nan** (`str`): If not `None`, specifies the method for handling areas with missing values:
     - **auto**: Drops the entire sample if any part contains a `NaN`.
     - **if_all_nan** (`List[str]`): Drops the sample only if it is entirely composed of `NaN`s.
     - **masked** (`List[str]`): Drops valid regions (as defined by `filter_var`) containing any `NaN`s. Requires `filter_var` to be defined.
   - **array_dims** (`Tuple[str, ...]`): Dimension names of the resulting `zarr`s with train and test data. 
   - **data_split** (`float`): Proportion of data allocated to training; remainder goes to testing.
   - **chunk_batch** (`int`): Number of chunks to process in each batch during parallel execution.
   - **callback** (`Callable`): Optional function applied to each chunk after initial processing.
   - **block_size** (`List[Tuple[str, int]]`): Size of the chunks to process, which can define memory usage and performance. If `None` the chunk size of ds is utilized
   - **sample_size** (`List[Tuple[str, int]]`): List of tuples specifying the dimensions and their respective sizes.
   - **overlap** (`List[Tuple[str, float]]`): List of tuples specifying the dimensions and their respective overlap proportion.
   - **scale_fn** (`str`): Feature scaling function to apply (`standardize`, `normalize`, or `None`).

### get_datasets
This method retrieves the processed training and testing datasets, ensuring all data is ready for analysis or machine learning model training.

```python
def get_datasets(self) -> Tuple[xr.Dataset, xr.Dataset]
```
#### Parameters
- `None`: This method has no input parameters.

#### Returns
- `Tuple[xarray.Dataset, xarray.Dataset]`: Tuple containing the training and testing dataset, each in the `xarray.Dataset` format


### Example

```python
import numpy as np
import xarray as xr
from ml4xcube.datasets.multiproc_sampler import MultiProcSampler

# Example dataset with chunking
data = np.random.rand(100, 200, 300)
dataset = xr.Dataset({
    'temperature': (('time', 'lat', 'lon'), data),
    'precipitation': (('time', 'lat', 'lon'), data)
}).chunk({'time': 10, 'lat': 50, 'lon': 50})

# Create an instance of MultiProcSampler
sampler = MultiProcSampler(
    ds=dataset, rand_chunk=True, nproc=4, apply_mask=True, 
    drop_sample=True, fill_method='constant', const=0.0,
    filter_var='land_mask', chunk_size=(100, 100, 10), 
    data_split=0.75, sample_size=[('time', 1),('lat', 5), ('lon', 5)], 
    overlap=[('time', 0.),('lat', 0.5), ('lon', 0.5)]
)

# Process the dataset and retrieve the 7-training and testing sets
train_ds, test_ds = sampler.get_datasets()
```
This documentation reflects the updated functionality and parameters of the `MultiProcSampler` class, providing a 
comprehensive guide for users to utilize its capabilities in data processing workflows.
