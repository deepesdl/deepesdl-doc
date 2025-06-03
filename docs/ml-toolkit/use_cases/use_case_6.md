# 6. Predictions for Multidimensional Samples

An alternative to [gap filling](use_case_5.md) can be using simpler methods. For example, missing values can be imputed
by replacing them with the mean or a constant placeholder. After exploring the data, it might be evident that gaps
are not frequent. In some cases, in environmental modeling for specific regions, missing values may be intentional.
For instance, values may appear only in terrestrial regions.

In such scenarios, data imputation can enable the effective use of the entire dataset, allowing for model training and analysis without the complications of incomplete data.

The following notebooks demonstrate the workflow for land surface temperature prediction using multidimensional data with missing values.

## Demo Notebooks

- [Machine Learning for Multidimensional Samples (PyTorch)](https://github.com/deepesdl/ML-Toolkits/blob/master/Examples/use_case_lst_pytorch_nd.ipynb)
- [Machine Learning for Multidimensional Samples (TensorFlow)](https://github.com/deepesdl/ML-Toolkits/blob/master/Examples/use_case_lst_tensorflow_nd.ipynb)

<p align="center">
<img src="../../img/replace_gaps.png" width="60%" height="60%">
</p>
<p align = "center"><i>
Filling areas outside the continent with constant value</i>
</p>
