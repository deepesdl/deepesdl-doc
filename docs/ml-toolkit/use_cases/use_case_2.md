# 2. Distributed Machine Learning

Satellites continuously monitor various Earth parameters across, generating vast amounts of data ideal for training sophisticated machine learning models.
However, preparing and training with such large datasets can be time-consuming and resource-intensive.
The `ml4xcube` package facilitates efficient handling, preparation, and distributed training of large geospatial datasets, providing tools and workflows
designed to optimize these processes.
Below are demonstrations on efficient dataset preparation (4) and distributed machine learning (5).
For simplicity the [previous setup](use_case_1.md) is leveraged to illustrate the functionality.

## Demo Scripts

- [Distributed Dataset Creation](https://github.com/deepesdl/ML-Toolkits/blob/master/Examples/distributed_dataset_creation.py)
- [Distributed Machine Learning](https://github.com/deepesdl/ML-Toolkits/blob/master/Examples/distributed_training.py)

### Data Preparation

Before training machine learning models, data must be preprocessed and organized. This snippet is crucial for understanding how data, particularly large and
complex datasets like those from satellites, is preprocessed before being used for machine learning. It demonstrates loading the data, computing statistics
necessary for normalization, and applying these statistics to standardize the data with the help of a callback function. The callback function is used to apply
transformations on-the-fly to each data chunk, ensuring that all data is processed uniformly. Further custom preprocessing steps can be added accordingly.

```python
import xarray as xr
from ml4xcube.preprocessing import get_statistics, standardize
from ml4xcube.datasets.multiproc_sampler import MultiProcSampler

# Load sample data
ds = xr.open_zarr('sample_data.zarr')
ds = ds['temperature']

# Create a train and a test set and save them as train.zarr and test.zarr
train_set, test_set = MultiProcSampler(
    ds          = ds,
    train_cube  = 'train.zarr',
    test_cube   = 'test.zarr',
    nproc       = 5,
    chunk_batch = 10,
).get_datasets()
```

In the next step, the environment for training must be prepared by converting datasets to a format compatible with PyTorch, setting up a basic neural network model, and configuring
the training process. Since in this example 1D data points are utilized for training, the dimension names assigned correspond to a 1D Tuple as well.
If the usage of multidimensional data samples is intended, please define the parameter sample_size of the `MultiProcSampler` class (e.g. `sample_size=[('time', 1), ('lat', 3), ('lon', 3)]`).
Overlapping samples are also possible (`overlap=[('time', 0.), ('lat', 0.33), ('lon', 0.33)]`). For further details check out the corresponding definition in the [ml4xcube API](../api-reference/6-datasets/multiproc-sampler.md)

```python
import zarr
import torch
import xarray as xr
import dask.array as da
from ml4xcube.datasets.pytorch import PTXrDataset

def load_train_objs():
    train_store = zarr.open('train.zarr')
    test_store = zarr.open('test.zarr')

    train_set = xr.Dataset(train_data)
    test_set  = xr.Dataset(test_data)

    # Create PyTorch data sets
    train_ds = PTXrDataset(train_set)
    test_ds  = PTXrDataset(test_set)

    # Initialize model and optimizer
    model     = torch.nn.Linear(in_features=1, out_features=1, bias=True)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
    loss      = torch.nn.MSELoss(reduction='mean')

    return train_ds, test_ds, model, optimizer, loss
```

This final snippet sets up and runs the distributed training process using PyTorch. It includes initializing the distributed data parallel training environment, preparing data
loaders with parallel processing capabilities, and defining the training loop. This approach significantly enhances the training efficiency on large-scale datasets by leveraging
multiple processing units.

```python
from ml4xcube.datasets.pytorch import prepare_dataloader
from ml4xcube.training.pytorch_distributed import ddp_init, Trainer, dist_train

# Initialize distributed data parallel training
ddp_init()

# Load training objects
train_set, test_set, model, optimizer, loss = load_train_objs()

# Prepare data loaders
train_loader, test_loader = prepare_dataloader(train_set, test_set, batch_size, num_workers=5, parallel=True)

# Initialize the trainer and start training
trainer = Trainer(
    model                = model,
    train_data           = train_loader,
    test_data            = test_loader,
    optimizer            = optimizer,
    save_every           = save_every,
    model_path           = best_model_path,
    early_stopping       = True,
    patience             = 3,
    loss                 = loss,
    validate_parallelism = True
)
```
