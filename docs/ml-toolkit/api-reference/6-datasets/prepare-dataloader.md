## prep_dataloader

```python
def prep_dataloader(
    train_ds: Dataset, test_ds: Dataset = None, batch_size: int = 1, callback: Callable = None, num_workers: int = 0, 
    parallel: bool = False, shuffle = True, drop_last=True
) -> Union[DataLoader, Tuple[DataLoader, DataLoader]]
```

### Description
This function sets up one or two `DataLoader`s' for PyTorch models, facilitating efficient and configurable data loading 
for both training and optional testing phases. This function integrates best practices for data management in deep 
learning applications, supporting parallel data loading, optional shuffling, and batch handling. It can handle single 
and distributed computing environments, making it versatile for local training sessions or scalable, distributed 
training across multiple GPUs or nodes.

### Parameters
   - **train_ds** (`torch.utils.data.Dataset`): The PyTorch dataset for training data loading.
   - **test_ds** (`torch.utils.data.Dataset`): The PyTorch dataset for testing data loading. If provided, the function returns a separate `DataLoader` for testing. Defaults to `None`.
   - **batch_size** (`int`): Number of samples/chunks per batch to load.
   - **callback** (`Callable`): A function to collate data into batches, or to perform custom operations during data loading.
   - **num_workers** (`int`): Number of subprocesses used for data loading.
   - **shuffle** (`bool`):  If `True`, the dataset is shuffled at every epoch to reduce model bias. Automatically set to `False` if parallel is `True`.
   - **parallel** (`bool`): If set to True, enables distributed training mode, which is crucial for training across multiple GPUs or nodes.
   - **drop_last** (`bool`): Whether to drop the last incomplete batch if the total number of samples isn't divisible by the batch size. This is often useful during training to ensure consistent batch sizes.

### Returns
- **Union[DataLoader, Tuple[DataLoader, DataLoader]]**:  A single `DataLoader` for the training dataset if `test_ds` is `None`, or a tuple containing `DataLoader`s for both training and testing datasets if `test_ds` is provided.

### Example

```python
from datasets.pytorch import prep_dataloader

# Assuming 'MyDataset' is a custom class derived from torch.utils.data.Dataset
train_dataset = MyDataset()
test_dataset = MyDataset()  # Optional test dataset
batch_size = 32
num_workers = 4

# Prepare DataLoader for training, with an optional test DataLoader
train_loader, test_loader = prep_dataloader(
    train_ds=train_dataset,
    test_ds=test_dataset,
    batch_size=batch_size,
    num_workers=num_workers,
    parallel=False,  # Set to True for distributed training
    shuffle=True,
    drop_last=True
)

# Use the DataLoader in a training loop
for data in train_loader:
    # Training operations go here
    pass
```
In this example, the `prep_dataloader` function is used to set up `DataLoader`s for PyTorch datasets, specifying the 
batch size and the number of worker subprocesses. This setup is typical for training machine learning models where 
efficient data handling and processing are crucial. 

### Notes
The function checks if parallel processing is enabled:
- If `parallel` is `True`, a `DistributedSampler` is used, which is essential for distributed training environments. This changes the sampling behavior of the dataset to ensure that each part of the dataset is handled by a different part of the model distributed across several nodes or GPUs.
- The `DataLoader` is then configured with the specified parameters. Notably, `pin_memory` is set conditionally based on whether CUDA is available, which can enhance data transfer speeds to GPU.