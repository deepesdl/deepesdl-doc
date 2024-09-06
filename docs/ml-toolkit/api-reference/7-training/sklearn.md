## Class: Trainer
The Trainer class is designed for training scikit-learn models using versatile data inputs, such as PyTorch DataLoaders or numpy arrays. 
This class is particularly useful for handling large datasets that may not fit into memory, as well as for leveraging the speed of batch training.
### Constructor

```python
def __init__(
        self,
        model: BaseEstimator, train_data: Union[Any, Tuple[np.ndarray, np.ndarray]],
        test_data: Union[Any, Tuple[np.ndarray, np.ndarray]] = None, metrics: Dict[str, Callable] = None,
        model_path: str = None, batch_training: bool = False, mlflow_run=None, task_type: str = 'supervised'
    )
```

#### Parameters
- **model** (`sklearn.base.BaseEstimator`): A scikit-learn estimator capable of partial_fit for incremental learning or fit for standard full-batch training.
- **train_data** (`Union[DataLoader, Tuple[numpy.ndarray, numpy.ndarray]]`):  Training data can be provided as a PyTorch DataLoader for batch training or a tuple of numpy arrays (X_train, y_train).
- **test_data** (`Union[DataLoader, Tuple[numpy.ndarray, numpy.ndarray]]`): Similar to train_data, validation/testing data can also be provided either as a DataLoader or a tuple of numpy arrays (X_test, y_test).
- **metrics** (`Dict[str, Callable]`): Dictionary containing metric functions that compute a performance score between predictions and true labels.
- **model_path** (`str`): File path to save the trained model.
- **batch_training** (`bool`): : Specifies whether to train the model using batches (if True) or on the complete dataset at once (if False).
- **mlflow_run** (optional): Optional MLflow run instance to log training parameters, metrics, and models. Default is `None`.
- **task_type** (`str`):  Specifies whether the training is 'supervised' or 'unsupervised'. Default is 'supervised'.


### train
Conducts the training process, using batched training or on the complete dataset at once and returns the model.
```python
train(self) -> BaseEstimator:
```
#### Parameters
- `None`: This method has no input parameters.

#### Returns
- `sklearn.base.BaseEstimator`: The trained model.

### Example

```python
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.linear_model import SGDClassifier
from ml4xcube.training.sklearn import Trainer

# Define a simple model and metrics
model = SGDClassifier()
metrics = {'Accuracy': accuracy_score}

# Dummy data
X_train = np.random.rand(100, 10)
y_train = np.random.randint(0, 2, 100)
X_test = np.random.rand(20, 10)
y_test = np.random.randint(0, 2, 20)

# Initialize trainer
trainer = Trainer(
    model=model,
    train_data=(X_train, y_train),
    test_data=(X_test, y_test),
    metrics=[("Accuracy", accuracy_score)],
    model_path="best_model.pkl",
    batch_training=False
)

# Train the model
trained_model = trainer.train()

# Evaluate the model
predictions = trained_model.predict(X_test)
print("Test Accuracy:", accuracy_score(y_test, predictions))

```
This setup offers an approach to train scikit-learn models, accommodating both large-scale and in-memory datasets effectively. The Trainer class not only facilitates extensive training configurations but also integrates model evaluation and saving mechanisms, making it a robust tool for machine learning training in diverse data-intensive environments.