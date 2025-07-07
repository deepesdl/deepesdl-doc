## PTXrDataset

`PTXrDataset` extends PyTorch's `Dataset` to provide specialized handling of `xarray.Dataset` for training neural 
networks in PyTorch. It supports dynamic processing and iteration over chunks of large datasets that cannot be fully 
loaded into memory, making it ideal for environments with significant data volumes. The class allows for flexible data 
manipulation including optional random chunk selection, dropping of `NaN` values, application of filtering masks, and 
data filling strategies, contained in the [preprocessing module](../index.md#5-preprocessing).

### Constructor
```python
def __init__(
   self, ds: xr.Dataset, rand_chunk: bool = True, drop_nan: str = 'auto', drop_sample: bool = False,
  chunk_indices: List[int] = None, apply_mask: bool = True, fill_method: str = None,
  const: float = None, filter_var: str = 'filter_mask', num_chunks: int = None, callback = None,
  block_sizes: List[Tuple[str, int]] = None, sample_size: List[Tuple[str, int]] = None,
  overlap: List[Tuple[str, float]] = None, process_chunks: bool = False
):
```

#### Parameters
   - **ds** (`xarray.Dataset`): The dataset from which data chunks are processed.
   - **rand_chunk** (`bool`): If True, chunks are selected randomly; otherwise, they are processed sequentially.
   - **drop_nan** (`str`): If not `None`, specifies the method for handling areas with missing values:
     - **auto**: Drops the entire sample if any part contains a `NaN`.
     - **if_all_nan** (`List[str]`): Drops the sample only if it is entirely composed of `NaN`s.
     - **masked** (`List[str]`): Drops valid regions (as defined by `filter_var`) containing any `NaN`s. Requires `filter_var` to be defined.
   - **drop_sample** (`bool`): If true, `NaN` values are dropped during filter application.
   - **chunk_indices** (`List[int]`): Specifies indices of chunks to be processed if not randomly selected.
   - **apply_mask** (`bool`): Whether to apply a filtering condition defined by the `filter_var` to the data chunks.
   - **fill_method** (`str`): Method used to fill masked or NaN data.
     - **None**: `NaN`s are not filled.
     - **mean**: `NaN`s are filled with the mean value of the non-`NaN` values
     - **sample_mean**: `NaN`s are filled with the sample mean value.
     - **noise**: `NaN` are filled with random noise within the range of the non-`NaN` values.
     - **constant**: `NaN`s are filled with the specified constant value (`const`).
   - **const** (`float`): Constant value used when `fill_method` is `constant`.
   - **filter_var** (`str`): Variable used for filtering data chunks.
   - **num_chunk** (`int`): Specifies the number of chunks to process if not processing all.
   - **block_size** (`List[Tuple[str, int]]`): Size of the chunks to process, which can define memory usage and performance. If `None` the chunk size of ds is utilized
   - **sample_size** (`List[Tuple[str, int]]`): List of tuples specifying the dimensions and their respective sizes.
   - **overlap** (`List[Tuple[str, float]]`): List of tuples specifying the dimensions and their respective overlap proportion.
   - **process_chunks** (`bool`): Whether to preprocess each chunk before returning.

### Example

```python
import xarray as xr
from ml4xcube.datasets.pytorch import PTXrDataset, prep_dataloader  

# Initializing the dataset
dataset = PTXrDataset(
    ds=my_xarray_dataset,
    rand_chunk=True,
    use_filter=True,
    filter_var='land_mask',
    sample_size=[('time', 2), ('lat', 10), ('lon', 10)],
    overlap=[('time', 0.5), ('lat', 0.5), ('lon', 0.5)]
)

# Creating a DataLoader for batch processing
data_loader = prep_dataloader(dataset, batch_size=10, shuffle=True, callback=map_fn)

# Using DataLoader in a training loop
for batch in data_loader:
    inputs, targets = batch
    outputs = model(inputs)  # Assuming 'model' is an instance of a PyTorch model
    # Continue with training steps
```
This setup demonstrates how `PTXrDataset` is integrated into a PyTorch training loop using `DataLoader`, facilitating 
efficient and scalable processing of geospatial datasets for deep learning applications. 
This functionality is critical for leveraging high-performance computing resources effectively, ensuring that large 
datasets are handled in a manner that optimizes both memory usage and computational speed.
The `map_fn` is a callback function as defined in [prep_dataloader](prepare-dataloader.md). 
It allows to define the features as well as the dependent variable for the training process and include further preprocessing steps.

### Notes
- `training.pytorch.Trainer` is able to handle empty chunks. Therefore raw data can be handed over to the `PTXrDataset` despite of gaps in the data.
- Samples obtained from a chunk serve as a batch of data. If a consistent batch size is required leverage the [XrDataset](xr-dataset.md) or the [MultiProcSampler](multiproc-sampler.md) to prepare data accordingly.
- This class efficiently handles large datasets by enabling the selective loading and processing of manageable data chunks.
- `PTXrDataset` allows for high customization in how data is processed, which is vital for training deep learning models that require specific data formats or preprocessing steps.
