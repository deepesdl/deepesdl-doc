## LargeScaleXrDataset

`TFXrDataset` is specifically designed to integrate `xarray.Dataset`s with TensorFlow machine learning workflows. 
It efficiently processes and streams data chunks for training or inference, making it particularly well-suited for h
andling extensive datasets that exceed memory capacities. This class enables dynamic data preprocessing and chunk-based 
iteration, facilitating performance optimization and seamless integration into TensorFlow pipelines.

### Constructor

```python
def __init__(self, ds: xr.Dataset, rand_chunk: bool = True, drop_nan: str = 'auto', chunk_indices: list = None,
            apply_mask: bool = True, drop_sample: bool = False, fill_method: str = None, const: float = None,
            filter_var: str = 'filter_mask', num_chunks: int = None, callback_fn = None,
            block_size: List[Tuple[str, int]] = None, sample_size: List[Tuple[str, int]] = None,
            overlap: List[Tuple[str, float]] = None, process_chunks: bool = False):
```

#### Parameters
   - **ds** (`xarray.Dataset`): The dataset from which data chunks are processed.
   - **rand_chunk** (`bool`): If True, chunks are selected randomly; otherwise, they are processed sequentially.
   - **drop_nan** (`str`): If not `None`, specifies the method for handling areas with missing values:
     - **auto**: Drops the entire sample if any part contains a `NaN`.
     - **if_all_nan** (`List[str]`): Drops the sample only if it is entirely composed of `NaN`s.
     - **masked** (`List[str]`): Drops valid regions (as defined by `filter_var`) containing any `NaN`s. Requires `filter_var` to be defined.
   - **chunk_indices** (`List[int]`): Specifies indices of chunks to be processed if not randomly selected.
   - **apply_mask** (`bool`): Whether to apply a filtering condition defined by the `filter_var` to the data chunks.
   - **drop_sample** (`bool`): If True, drops any samples that doesn't contain relevant values according to the `filter_var` criteria completely.
   - **fill_method** (`str`): Method used to fill masked or NaN data.
     - **None**: `NaN`s are not filled.
     - **mean**: `NaN`s are filled with the mean value of the non-`NaN` values
     - **sample_mean**: `NaN`s are filled with the sample mean value.
     - **noise**: `NaN` are filled with random noise within the range of the non-`NaN` values.
     - **constant**: `NaN`s are filled with the specified constant value (`const`).
   - **const** (`float`): Constant value used when fill_method is 'constant'.
   - **filter_var** (`str`): Filter mask name used for filtering data chunks.
   - **num_chunk** (`int`): Specifies the number of chunks to process if not processing all.
   - **callback** (`int`): Optional function applied to each chunk after initial processing.
   - **block_size** (`List[Tuple[str, int]]`): Size of the chunks to process, which can define memory usage and performance. If `None` the chunk size of ds is utilized
   - **sample_size** (`List[Tuple[str, int]]`): List of tuples specifying the dimensions and their respective sizes.
   - **overlap** (`List[Tuple[str, float]]`): List of tuples specifying the dimensions and their respective overlap proportion.
   - **process_chunks** (`bool`): Whether to preprocess each chunk before returning.

### len
Returns the number of chunks, providing insights into the volume of data being processed.

```python
def __len__(self) -> int
```
#### Parameters
- `None`: This method has no input parameters.

#### Returns
- `int`: number of chunks

### get_datasets
Creates a `TensorFlow` dataset from the generator.

```python
get_dataset(self) -> tf.data.Dataset
```
#### Parameters
- `None`: This method has no input parameters.

#### Returns
- `tf.data.Dataset`: `TensorFlow` dataset object, yielding chunks of data.

### Example

```python
# Create an instance of LargeScaleXrDataset
dataset_processor = LargeScaleXrDataset(
    xr_dataset=my_xarray_dataset,
    rand_chunk=True,
    drop_nan=True,
    use_filter=True,
    filter_var='land_mask',
    sample_size=[('time', 24)],
    overlap=[('time', 1)]
)

# Use the generator to feed data into a TensorFlow model
for data_chunk in dataset_processor.generate():
    # Assuming 'model' is an instance of a TensorFlow model
    predictions = model.predict(data_chunk['input_data'])
    print("Processed predictions:", predictions)
```

This example demonstrates how to initialize the `LargeScaleXrDataset` class and use its generate method to continuously supply data to a TensorFlow model. 
The class is essential for applications where large datasets are common, and chunks must be loaded to memory and processed successively.

### Notes
- If instances of `LargeScaleXrDataset` are handed over to the `training.tensorflow.Trainer` every processed chunk must contain valid data
- If validity of data samples can not be guaranteed after preprocessing a chunk, prepare an appropriate datasets using the [XrDataset](datasets/xr-dataset.md) or the [MultiProcSampler](datasets/multiproc-sampler.md).
- Samples obtained from a chunk serve as a batch of data. If a consistent batch size is required leverage the [XrDataset](datasets/xr-dataset.md) or the [MultiProcSampler](datasets/multiproc-sampler.md) to prepare data accordingly.
