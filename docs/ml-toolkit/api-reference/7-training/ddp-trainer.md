## Trainer
The `Trainer` class in the `training.pytorch_distributed` module is meticulously crafted to optimize the distributed training of PyTorch models on systems equipped with multiple GPUs. 
It supports a range of functionalities such as distributed data parallel processing, early stopping, metrics evaluation, snapshot saving, and optional loss plotting in a distributed environment.

### Constructor

```python
def __init__(
    self, model: torch.nn.Module, train_data: DataLoader, test_data: DataLoader,
    optimizer: torch.optim.Optimizer, save_every: int, best_model_path: str,
    snapshot_path: str = None, early_stopping: bool = True, patience: int = 10,
    loss: Callable = None, metrics: Dict[str, Callable] = None, epochs: int = 10,
    validate_parallelism: bool = False, create_loss_plot: bool = False
)
```

#### Parameters
- **model** (`torch.nn.Module`): The model to be trained, which will be wrapped within a DistributedDataParallel (DDP) container.
- **train_data** (`DataLoader`): The DataLoader for the training dataset, appropriately set up to work in a distributed manner.
- **test_data** (`DataLoader`): The DataLoader for the validation dataset, also configured for distributed usage.
- **optimizer** (`torch.optim.Optimizer`): Optimizer used for training the model.
- **save_every** (`int`): Epoch frequency at which to save training snapshots.
- **best_model_path** (`str`): Path where the best model according to validation loss is saved.
- **snapshot_path** (`str`): Path to save periodic training snapshots; helpful for long training sessions.
- **early_stopping** (`bool`): Indicates whether training should stop early if there's no improvement, with a default setting of True
- **patience** (`int`): Number of epochs to wait for improvement in validation loss before early stopping. Defaults to `10`.
- **loss** (`Callable`): Loss function used during training. Must be specified.
- **metrics** (`Dict[str, Callable]`): Dictionary containing metrics to be evaluated during validation.
- **epochs** (`int`): The number of maximum training epochs.
- **validate_parallelism** (`bool`): If set to True, prints loss information from each GPU, useful for debugging and performance tuning.
- **create_loss_plot** (`bool`): Enables the creation of a plot that displays the training and validation loss progress over epochs.

### train
Manages the distributed training process across all epochs, handles early stopping, and loads the best model state at the end.
It encapsulates the training process within a recorded session to handle potential errors and ensure proper cleanup of resources.

```python
train(self) -> torch.nn.Module
```
#### Parameters
- `None`: This method has no input parameters.

#### Returns
- `torch.nn.Module`: The trained model with the best performance on validation data after distributed training.


### Example

```python
import torch
import xarray as xr
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset
from ml4xcube.splits import assign_block_split
from ml4xcube.datasets.xr_dataset import XrDataset
from ml4xcube.datasets.pytorch import prep_dataloader
from ml4xcube.training.pytorch_distributed import ddp_init, Trainer

# Example model
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = nn.Linear(...)

    def forward(self, x):
        return self.linear(x)

# Setting up distributed 7-training environment
ddp_init()

# Load sample data
xds = xr.open_zarr('sample_data.zarr')

# Assign a train test split
xds = assign_block_split(ds=xds, block_size=[("time", 10), ("lat", 100), ("lon", 100)], split=0.8)

# Extract a subset for training and testing, 
train_data, test_data = XrDataset(ds=xds, num_chunks=5, rand_chunk=False, to_pred='variable1').get_datasets()

# Extract X_train and y_train, as well as X_test and y_test from train_data and test_data tuples and potentially reshape
# ...

# Load data and prepare it for parallel training
train_ds     = TensorDataset(torch.tensor(X_train), torch.tensor(y_train))
test_ds      = TensorDataset(torch.tensor(X_test), torch.tensor(y_test))

train_loader, test_loader = prep_dataloader(train_ds, test_ds, batch_size=64, parallel=True)

# Model, optimizer, and loss
model = SimpleModel()
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)
loss_fn = nn.CrossEntropyLoss()

# Trainer
trainer = Trainer(model, train_loader, test_loader, optimizer, model_path="best_model.pth", loss=loss_fn, epochs=10)

# Train the model
trained_model = trainer.train()
```
This setup demonstrates the workflow of the of handling a distributed training tasks within `ml4xcube`.
This module provides a tool for training with large datasets, requiring high computational resources.