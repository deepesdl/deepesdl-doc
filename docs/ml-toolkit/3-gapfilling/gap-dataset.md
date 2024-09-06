## Class: GapDataset

The `GapDataset` class within the `helper.predictors` submodule is designed to manage and prepare predictor data that aids in the estimation of missing values within a target dataset. It initializes with a specific variable from a dataset and aligns predictor data accordingly, handling both the extraction and storage of the processed data.

### Constructor

```python
 def __init__(self, ds: xr.DataArray, ds_name: str = 'Test123',
              dimensions: Dict[str, tuple] = None,
              artificial_gaps: List[float] = None,
              actual_matrix: Union[str, datetime.date] = 'Random',
              predictor_path: str = None, layer_dim: str = 'time'):
```

#### Parameters
   - **ds** (`xarray.DataArray`): The input dataset that contains gaps.
   - **ds_name** (`str`): The name of the dataset.
   - **dimensions** (`Dict[str, tuple]`): Dict containing dimension ranges (e.g., lat, lon, times) in order to extract the subset of `ds` relevant for the prediction.
   - **artificial_gaps** (`List[float]`):  List of artificial gap sizes (floats between 0 and 1) to create ground truth for training and subsequent gapfilling of real gaps. If None no artificial gaps are created. The predictor will estimate real gaps directly when utilizing the [Gapfilling](gap-filling.md) class. 
   - **actual_matrix** (`Union[str, datetime.date]`): Specifies the selection criterion for extracting a specific slice of the dataset based on the dimension defined by layer_dim. This parameter can be used in two ways:
     - As `str`: If set to 'Random', a random value from the available values within the specified dimension (layer_dim) is chosen. This is useful for stochastic approaches where randomness is needed for validation or testing.
     - As `datetime.date` or specific value: Allows precise specification of the slice to be selected. When a date or specific value is provided, the dataset is sliced at this exact point, or the nearest available point if the exact value is not present in the dataset. 
   - **predictor_path** (`str`): Path to the directory where predictor data is stored. If `None` a support vector regression is performed for every gap size defined in `artificial_gaps`.
   - **layer_dim** (`str`): Dimension along which to iterate. First dimension is default if not specified. 

### get_data
This method orchestrates several key operations essential for setting up the dataset for subsequent gap-filling tasks. It manages the data retrieval, processing, and preparation phases, ensuring that all necessary data transformations and setups are completed before the actual gap-filling process begins.
```python
def get_data(self) -> None
```
#### Parameters
- `None`: This method has no input parameters.

#### Returns
- `None`: This method does not return any value.





### Example

```python
import datetime
import xarray as xr
from ml4xcube.gapfilling.gap_dataset import GapDataset

# Example data and dimensions
data = xr.open_dataarray('path_to_dataarray')
dimensions = {
    'lat': (30, 45), 
    'lon': (10, 25), 
    'time': (datetime.date(2020, 1, 1), datetime.date(2020, 12, 31))
}

# Initialize the GapDataset class
gap_dataset = GapDataset(data, 'ExampleDataset', dimensions)

# Process data to create a dataset ready for gap filling
gap_dataset.get_data()
```
