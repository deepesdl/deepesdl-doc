# DeepESDL ML Toolkit

The DeepESDL ML Toolkit is a small and handy 
Python package that provides useful functions for machine learning tasks
with DeepESDL data cubes.

The toolkit is made available as a DeepESDL JupyterLab environment (profile), 
and includes popular libraries such as **scikit learn**, **TensorFlow**, 
**Keras**, and **PyTorch**.

To support model evaluation during training, the ready-to-use processing
environment is also extended by a **TensorBoard** to support the tracking of
individual experiments and training runs.
This tool can be used with PyTorch and TensorFlow, and it provides 
a state-of-the-art toolset for data scientist to inspect the tuning 
and training process and compare metrics.

The toolkit offers the following:

* Adapters are provided to existing data loading and transformation 
  mechanisms from Keras and PyTorch (`DataGenerator`, `DataLoader`) 
  to be usable for the DeepESDL data cubes. 

* Implementations of sampling mechanisms and online repartitioning methods 
  suited for the data cube files which are stored in chunks. 
  This element is essential, as it enables deep learning that respects 
  the basic principles of geo data way beyond naive applications of
  machine learning in the Earth system context. 

To ease adoption by scientist we plan to also develop script templates 
for common deep learning tasks such as autoencoder on time-series data, 
in particular physics informed autoencoder, transfer learning and change 
detection on time series.

The toolkit is currently for Python only, but Julia will also be 
considered to address a small but growing community of data scientists.

Please refer to the [ML Tools Documentation](../ml-tools/index.md)
for details.

