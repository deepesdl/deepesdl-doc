## Class: Gapfiller


### Constructor

```python
def __init__(self, ds_name: str = "Test123", hyperparameters: str = "RandomGridSearch", predictor: str = "RandomPoints")
```

#### Parameters
   - **ds_name** (`str`): The name used to identify and reference the dataset throughout the gap filling process. This name is utilized for directory naming, which helps in organizing output results such as filled datasets or models.
   - **hyperparameters** (`str`): Defines the approach for hyperparameter optimization, with options such as `RandomGridSearch`, `FullGridSearch`, or `Custom`. The selection influences how the underlying machine learning model, such as SVR, will tune its parameters to best fit the data.
     - `RandomGridSearch`:  Utilizes a randomized search over a predefined grid of hyperparameters. This method is faster but might miss the optimal point, suitable for large datasets or when a good-enough solution is acceptable.
     - `FullGridSearch`: Performs an exhaustive search over the specified grid of hyperparameters. While comprehensive, it can be computationally intensive.
     - `Custom`: Allows for manual specification of hyperparameters, providing full control over the learning process, ideal for use cases where domain knowledge can guide specific settings.
   - **predictor** (`str`): Strategy for selecting predictors used in model training, options include `AllPoints`, `RandomPoints`, `lccs_class`, or any specified extra matrix predictors.
     - `AllPoints`: Uses all available data points as predictors, maximizing the information available for model training.
     - `RandomPoints`: Randomly selects a subset of data points to be used as predictors, useful for reducing computational load or when data is too large.
     - `lccs_class`: Specifies the use of land cover value estimation, focusing on leveraging spatial or categorical similarities.
     - `Custom`: Utilizes different types of external or derived predictors.


### gapfill
Main method to execute the gap filling process. It orchestrates data retrieval, directory management, model training, and result processing.
Prints the directory containing the application results when the processes is completed.

```python
def gapfill(self) -> None
```
#### Parameters
- `None`: This method has no input parameters.

#### Returns
- `None`: This method does not return any value.


### Example

```python
import datetime
import xarray as xr
from ml4xcube.gapfilling.gap_filler import Gapfiller

# Example of using the Gapfiller class to fill data gaps
gap_filler = Gapfiller(
    ds_name='ExampleDataset', 
    hyperparameters="RandomGridSearch", 
    predictor="lccs_class"
)
gap_filler.gapfill()
```
