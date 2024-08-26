## Class: Trainer
The Trainer class in the training.tensorflow module is tailored to facilitate the efficient training of TensorFlow models, especially on systems equipped with a single GPU or none. It provides comprehensive support for training session management, including early stopping, model checkpointing, and integration with TensorBoard for monitoring.


### Constructor

```python
def __init__(
    self, model: tf.keras.Model, train_data: tf.data.Dataset, test_data: tf.data.Dataset, 
    best_model_path: str, early_stopping: bool = True, patience: int = 10, 
    tf_log_dir: str = './logs', mlflow_run=None, epochs: int = 100, 
    train_epoch_steps: int = None, val_epoch_steps: int = None, create_loss_plot: bool = False,
)

```

#### Parameters
- **model** (`tensorflow.keras.Model`): The TensorFlow model to be trained.
- **train_data** (`tensorflow.data.Dataset`): TensorFlow Dataset containing the training data.
- **test_data** (`tensorflow.data.Dataset`): TensorFlow Dataset containing the validation data.
- **best_model_path** (`str`): Path where the best model according to validation loss is saved.
- **early_stopping** (`bool`): Indicates whether training should stop early if there's no improvement, with a default setting of True
- **patience** (`int`): Number of epochs to wait for improvement in validation loss before early stopping. Defaults to `10`.
- **tf_log_dir** (`str`): Directory path for saving TensorBoard logs, defaulted to './logs'.
- **mlflow_run** (optional): Optional MLflow run instance to log training parameters, metrics, and models. Default is `None`.
- **epochs** (`int`): Total number of epochs to train. Defaults to `10`.
- **train_epoch_steps** (`int`): Number of steps to run each training epoch, calculated dynamically if not set.
- **val_epoch_steps** (`int`): Number of steps to run each validation epoch, calculated dynamically if not set.
- **create_loss_plot** (`bool`): If `True`, generates a plot for training and validation losses after training. Defaults to `False`.


### train
Conducts the training process across all epochs, handles early stopping, and loads the best model state at the end.

```python
train(self) -> tf.keras.Model
```
#### Parameters
- `None`: This method has no input parameters.

#### Returns
- `torch.nn.Module`:  The trained model, equipped with the best weights found during the training if early stopping was triggered.

### Example

```python
import tensorflow as tf
from ml4xcube.training.tensorflow import Trainer

# Define the model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(feature_size,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Prepare data
train_dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train)).batch(32)
test_dataset = tf.data.Dataset.from_tensor_slices((X_test, y_test)).batch(32)

# Create a trainer instance
trainer = Trainer(
    model=model,
    train_data=train_dataset,
    test_data=test_dataset,
    best_model_path='path/to/save/best_model.h5',
    tf_log_dir='path/to/save/logs',
    epochs=50,
    create_loss_plot=True
)

# Train the model
trained_model = trainer.train()
```
This class offers a robust solution for training complex TensorFlow models with high efficiency, providing tools necessary for handling large-scale data and optimizing computational resources.