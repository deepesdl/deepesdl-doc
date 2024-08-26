
## Evaluator

The `Evaluator` class in the `ml4xcube.evaluation.metrics` module is designed to handle metric evaluation 
for machine learning frameworks (PyTorch, TensorFlow, and Scikit-learn), allowing users to evaluate various 
metrics during model validation or testing.

### Constructor

```python
def __init__(self, framework: str):
```

#### Parameters

- **framework** (`str`): The deep learning framework being used. Supported values are:
  - `'pytorch'`
  - `'tensorflow'`
  - `'sklearn'`


### get_metrics

```python
def get_metrics(self, metric_names: List[str], average: str = 'macro', delta: float = 1.0) -> Dict[str, Callable]:
```

This method returns a dictionary of metric functions based on the selected framework, metric names, and 
optional parameters. `average` is 

#### Parameters

- **metric_names** (`List[str]`): A list of metric names to retrieve. These names should correspond to the keys in the `metric_functions` attribute.
- **average** (`str`): The averaging method for precision, recall, and F1 score. Default is `'macro'`. Other possible values include `'micro'` and `'weighted'`.
- **delta** (`float`): The delta parameter for Huber loss. Default is `1.0`.

#### Returns

- **metrics** (`Dict[str, Callable]`): A dictionary where the keys are metric names and the values are the corresponding metric functions.

#### Supported Metrics

- **'mae'**: Mean Absolute Error
- **'mse'**: Mean Squared Error
- **'rmse'**: Root Mean Squared Error
- **'r2'**: R-squared
- **'huber_loss'**: Huber Loss
- **'mape'**: Mean Absolute Percentage Error
- **'med_ae'**: Median Absolute Error
- **'explained_variance'**: Explained Variance
- **'accuracy'**: Accuracy
- **'roc_auc'**: ROC AUC score
- **'cross_entropy'**: Cross-Entropy Loss
- **'precision'**: Precision score
- **'recall'**: Recall score
- **'f1_score'**: F1 Score

### Example Usage

```python
from ml4xcube.training.sklearn import Trainer
from ml4xcube.evaluation.evaluator import Evaluator

evaluator = Evaluator(framework='sklearn')
metrics = evaluator.get_metrics(metric_names=['recall', 'accuracy', 'precision'])

# Access a specific metric function and use it
mae_fn = metrics['recall']

# Use the dictionary for model validation during training
trainer = Trainer(
  model   = model,
  ...
  metrics = metrics
)

trained_model = trainer.train()
```

