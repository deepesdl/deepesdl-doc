# Getting Started 

`ml4xcube` is a comprehensive Python-based toolkit designed for researchers and developers in the field of machine learning with an emphasis on `xarray` data cubes. This toolkit is engineered to provide specialized and robust support for data cube management and analysis, operating with the state-of-the-art machine learning libraries (1) `scikit-learn`, (2) `PyTorch` and (3) `TensorFlow`. 

## Installation

Get started with `ml4xcube` effortlessly by using the newest stable `xcube` kernel in DeepESDL (e.g. `xcube-1.11.0`) .

When working with [custom team environment](../guide/jupyterlab/index.md#creating-custom-team-python-environment), 
add `ml4xcube` to the list of dependencies.


## Features

- Data preprocessing and postprocessing functions
- Filling masked data and gap filling features
- Dataset creation and train-/ test splitting techniques
- Trainer classes for `sklearn`, `TensorFlow` and `PyTorch`
- Distributed training framework compatible with `PyTorch`
- chunk utilities for working with data cubes


## Requirements

| Package        | Versions     |
|----------------|--------------|
| dask           | &ge;2023.2.0 |
| numpy          | &ge;1.24     |
| pandas         | &ge;2.2      |
| scikit-learn   | &gt;1.3.1    |
| xarray         | &gt;2023.8.0 |
| zarr           | &gt;2.11     |
| rechunker      | &ge;0.5.1    |

   
Make sure you have Python version 3.8 or higher.

If you're planning to use `ml4xcube` with TensorFlow or PyTorch, set up these frameworks properly in your conda environment. 