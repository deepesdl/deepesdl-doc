# ml4xcube API

## 1. plotting

The `Plotting` module provides functionality to visualize slices of data from `xarray.DataArray`.
It facilitates the analysis of multidimensional data. The primary function in this module is `plot_slice`,
which allows users to create visualizations with optional masks to highlight specific regions of interest.

**Functions:**

- [plot_slice](api-reference/1-plotting/plot-slice.md) - Renders a 2D slice of an `xarray.DataArray` with optional emphasis on specific features via masking.

## 2. insights

The `insights` module offers tools for extracting and analyzing characteristics of multidimensional data cubes from
`xarray.DataArray` objects. This module includes functions to assess the completeness and distribution of data within
the cube, helping users understand the dataset's quality and spatial-temporal coverage.
The detailed workflow in order to analyze the specifics of a data cube is demonstrated in the following
[Jupyter Notebook](example.md#demo-notebooks).

**Functions:**

- [get_insights](api-reference/2-insights/get-insights.md) - Extracts and prints detailed characteristics of a data cube, including dimensions, value ranges, and gaps in the data.
- [get_gap_heat_map](api-reference/2-insights/get-count-heat-map.md) - Generates a heat map to visualize the distribution of non-`NaN` values across selected dimensions, revealing patterns of data availability or missingness.

## 3. gapfilling

The `ml4xcube.gapfilling` module is designed to address and rectify data gaps in multidimensional geospatial datasets,
particularly those represented in `xarray.Dataset` formats. The gap filling process is divided into three main submodules,
each playing a crucial role in the preparation, processing, and application of sophisticated machine learning algorithms
to ensure accurate and efficient data imputation. he entire gapfilling process is showcased in the following
[Jupyter Notebook](example.md#5-gapfilling).

### 3.1. helper.predictors

The `HelpingPredictor` class within the `helper.predictors` submodule facilitates the preparation of predictor data for
gap filling applications. This submodule focuses on extracting and processing global predictor data, such as land
cover classifications, matching them to the corresponding dimensions (e.g., latitude and longitude) of the target data cube.
The prepared predictor is then stored in a `.zarr` dataset, ready to be used across various gap filling applications.
If not leveraged during the gap filling process, a Support Vector Machine is trained on artificial gaps within the `Gapfiller` class.

**Classes:**

- [HelpingPredictor](api-reference/3-gapfilling/helper-helpingpredictor.md) - Facilitates the preparation of predictor data for gap filling.

### 3.2. gap_dataset

The `GapDataset` class in the `gap_dataset`submodule is designed to prepare data before performing the actual gap
filling applications. This submodule focuses on slicing specific dimensions from a data cube, applying optional
artificial gaps, and managing datasets for subsequent gap filling operations.

**Classes:**

- [GapDataset](api-reference/3-gapfilling/gap-dataset.md) - Prepares data with artificial gaps optionally for training of a regressor and datasets with real gaps before gap filling can be performed.

### 3.3. gap_filling

The `Gapfiller` class within the `gap_filling` submodule is an integral part of the `ml4xcube.gapfilling` module
designed to implement and manage the gap filling process using machine learning techniques, specifically focusing
on Support Vector Regression (SVR) for now. It allows for the integration of different hyperparameters, and predictors
to optimize the gap filling process. A prerequsite before gap filling can be applied, is a specific data preparation
step, taken over by the functionalities of the `GapDataset` class.

**Classes:**

- [Gapfiller](api-reference/3-gapfilling/gap-filling.md) - Optionally trains a predictor to estimate actual values in gaps. Performs gap filling with SVR or a user-provided regressor.

## 4. Splits

The `splits` module includes functions designed to divide an `xarray.Datasets` into a train and a test set. These
functions use sampling strategies to ensure that data is split in a manner that respects the integrity of spatial
and temporal data blocks, facilitating the development of machine learning models. Functions to assign split variables
provide structured and random approaches to segmenting the dataset, which are then utilized by the `create_split`
function to generate actual train-test splits.

**Functions:**

- [assign_block_split](api-reference/4-splits/assign-block-split.md) - Determines the assignment of data blocks to train or test sets using a deterministic approach based on the Cantor pairing function. This structured random sampling respects data locality and sets up the `splits` variable used by `create_split`.
- [assign_rand_split](api-reference/4-splits/assign-rand-split.md) - Randomly assigns a split indicator to each element in the dataset based on a specified proportion. This method provides a randomized approach to setting up the `splits` variable, which is also used by `create_split`.
- [create_split](api-reference/4-splits/create-split.md) - Generates train-test splits for machine learning models by utilizing a predefined `splits` variable within the dataset. Supports `xarray.Dataset` or a dictionary of `numpy` arrays and provides flexibility in specifying feature and target variables, effectively leveraging the split defined by the previous functions.

## 5. preprocessing

The `preprocessing` module provides a collection of functions for preparing and processing data from `xarray.Datasets`,
particularly focusing on operations commonly required in data science and machine learning workflows.
These functions include filtering, filling missing data, calculating statistics, and normalizing or standardizing data.

**Functions:**

- [apply_filter](api-reference/5-preprocessing/apply-filter.md) - Applies a specified filter to the data by setting all values to NaN which do not belong to the mask or dropping the entire sample.
- [assign_mask](api-reference/5-preprocessing/assign-mask.md) - Assigns a mask to the dataset for later data division or filtering.
- [drop_nan_values](api-reference/5-preprocessing/drop-nan-values.md) - Filters out samples from a dataset if they contain any `NaN` values, with an optional mask to determine sample validity. It handles both 1D and multi-dimensional samples.
- [fill_nan_values](api-reference/5-preprocessing/fill-nan-values.md) - Fills `NaN` values in the dataset using a specified method.
- [get_range](api-reference/5-preprocessing/get-range.md) - Computes the range (min and max) of the data.
- [get_statistics](api-reference/5-preprocessing/get-statistics.md) - Computes the mean and standard deviation of a specified variable.
- [normalize](api-reference/5-preprocessing/normalize.md) - Normalizes the data to the range [0,1].
- [standardize](api-reference/5-preprocessing/standardize.md) - Standardizes the data to have a mean of 0 and variance of 1.

## 6. datasets

The datasets module is a comprehensive suite designed to handle, process, and prepare data cubes for machine learning
applications. This module supports various data scales and integrates seamlessly with major deep learning frameworks like PyTorch and TensorFlow, ensuring that data stored in `xarray` datasets is optimally formatted and ready for training deep learning models.

### 6.1. multiproc_sampler

The `MultiProcSampler` class is designed to process and sample large multidimensional training and testing datasets
efficiently using parallel processing, specifically tailored for machine learning model training in the `ml4xcube` framework.

**Classes:**

- [MultiProcSampler](api-reference/6-datasets/multiproc-sampler.md) - Samples train and test data as `.zarr` datasets.

### 6.2. pytorch

The `datasets.pytorch` module integrates with `PyTorch` to manage and process large datasets efficiently.
This module utilizes the power of `PyTorch`'s `Dataset` and `DataLoader` functionalities to prepare and iterate over
chunks of data cubes for deep learning applications, ensuring that data management is scalable and performance-optimized.

**Classes:**

- [PTXrDataset](api-reference/6-datasets/pt-large-scale-xr-dataset.md) - Corresponds to a subclass of PyTorch’s Dataset, designed specifically to handle large datasets based on a provided `xarray.Dataset`.

**Functions:**

- [prep_dataloader](api-reference/6-datasets/prepare-dataloader.md) - Sets up one or two `DataLoader`s from a PyTorch `Dataset` which was sampled from an `xarray.Dataset`. If a test set is provided, two `DataLoader`s are returned; otherwise, one.

### 6.3. tensorflow

The `datasets.tensorflow module` is specifically designed to handle and iterate over large `xarray` datasets and
efficiently prepare them for use with TensorFlow models. This module provides a seamless interface to transform
data stored in `xarray` datasets into structured TensorFlow datasets that can be directly utilized in training
and inference pipelines. The core functionality is encapsulated in the `TFXrDataset` class, which leverages
TensorFlow's capabilities to manage data flow dynamically, supporting scalable machine learning operations on large datasets.

**Classes:**

- [TFXrDataset](api-reference/6-datasets/tf-large-scale-xr-dataset.md) - TensorFlow specific implementation to handle and iterate over large `xarray` datasets.

### 6.4. xr_dataset

The `XrDataset` class within the `datasets/xr-dataset` module is tailored to efficiently manage and process smaller
datasets directly within memory, leveraging in-memory operations to enhance both speed and performance.

**Classes:**

- [XrDataset](api-reference/6-datasets/xr-dataset.md) - Creates small datasets manageable in memory.

## 7. training

The training module serves as a comprehensive suite for training machine learning models across various frameworks,
designed to accommodate the unique demands of large-scale and high-dimensional datasets typically encountered in
geospatial analysis and beyond. This module streamlines the training process, offering specialized support for PyTorch,
TensorFlow, and scikit-learn, enabling users to leverage the strengths of these popular frameworks efficiently.

### 7.1. pytorch

The `training.pytorch` module provides tools for training PyTorch models. It includes functionalities such as
early stopping, model checkpointing, and performance logging, ensuring efficient training and optimization of models.

**Classes:**

- [Trainer](api-reference/7-training/pytorch.md) - Tailored for the training of PyTorch models.

### 7.2. pytorch_distributed

The training.pytorch_distributed module is designed to facilitate efficient distributed training of PyTorch models
across multiple GPUs or nodes. This module leverages PyTorch's DistributedDataParallel (DDP) functionality, providing
tools to handle complex distributed training tasks with ease, including setup, execution, and synchronization across
multiple processes.

**Classes:**

- [Trainer](api-reference/7-training/ddp-trainer.md) - Crafted to perform distributed training for PyTorch models.

**Functions:**

- [ddp_init](api-reference/7-training/ddp-init.md) - Initializes the distributed process group for GPU-based distributed training.

### 7.3. sklearn

The `training.sklearn` module is tailored to train scikit-learn models efficiently. It supports batch training for
handling large datasets and provides tools for evaluating model performance using various metrics, catering to both
supervised and unsupervised learning tasks.

**Classes:**

- [Trainer](api-reference/7-training/sklearn.md) - Designed for training scikit-learn models.

### 7.4. tensorflow

The `training.tensorflow` module is specifically designed for training TensorFlow models.
This module provides a comprehensive suite of tools for training, evaluating, and monitoring TensorFlow models,
particularly those used in processing large datasets typically encountered in fields such as geospatial analysis.

**Classes:**

- [Trainer](api-reference/7-training/tensorflow.md) - Created to facilitate the training of TensorFlow models.

## 8. postprocessing

The `preprocessing` module provides functionalities, which are commonly required after machine learning operations
to receive the final predictions.

**Functions:**

- [undo_normalizing](api-reference/8-postprocessing/undo-normalizing.md) - Reverts the normalization process to obtain the original data range.
- [undo_standardizing](api-reference/8-postprocessing/undo-standardizing.md) - Reverts the standardization process to obtain the original data scale.

## 9. evaluation

The evaluation module in the `ml4xcube` API is designed to support comprehensive metric evaluation for machine learning
models across various frameworks including PyTorch, TensorFlow, and Scikit-learn. This module supports with
assessing model performance during validation or testing phases, providing a range of metrics to evaluate accuracy,
error rates, and other critical performance indicators. Providing a unified access to metrics from the different frameworks

### 9.1. evaluator

The `Evaluator` class is tailored to handle metric evaluations, allowing users to measure and analyze model performance
using metrics suited to their specific framework.

**Classes:**

- [Evaluator](api-reference/9-evaluation/evaluation.md) - Facilitates metric evaluation across different machine learning frameworks, enabling the assessment of various performance metrics during model validation or testing.

## 10. utils

The `utils` module provides a set of utility functions for handling and processing `xarray.Datasets`. These functions
facilitate tasks such as rechunking datasets, retrieving specific data chunks, and iterating over data blocks. They are
particularly helpful for optimizing the performance of data operations and preparing datasets for machine learning tasks.

**Functions:**

- [assign_dims](api-reference/10-utils/assign-dims.md) - Assign dimensions to each `dask.array` or `xarray.DataArray` within a dictionary.
- [calculate_total_chunks](api-reference/10-utils/calculate-total-chunks.md) - Compute the number of chunks of an `xarray.Dataset`.
- [get_chunk_by_index](api-reference/10-utils/get-chunk-by-index.md) - Retrieve a specific data chunk from an `xarray.Dataset`.
- [get_chunk_sizes](api-reference/10-utils/get-chunk-sizes.md) - Determine maximum chunk sizes of all data variables of the `xarray.Dataset`.
- [get_dim_range](api-reference/10-utils/get-dim-range.md) - Calculates the dimension range of an `xarray.DataArray` dimension.
- [iter_data_var_blocks](api-reference/10-utils/iter-data-var-blocks.md) - Create an iterator over chunks of an `xarray.Dataset`.
- [rechunk_cube](api-reference/10-utils/rechunk-cube.md) - Rechunks an `xarray.DataArray` to a new chunking scheme and stores the result at a specified path.
- [split_chunk](api-reference/10-utils/split-chunk.md) - Split a chunk into data samples for subsequent machine learning training.
