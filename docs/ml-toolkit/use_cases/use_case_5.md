# 5. Gapfilling

The gapfilling module provides a method for filling gaps in ESDCs, particularly tailored for remote sensing datasets
(Sarafanov et al. 2020). This approach utilizes a support vector regression model to predict missing values based
on available data.

After examining the amount of missing values in the cube, the module can be applied to fill the corresponding
areas in the cube as showcased in the following example:

## Demo Notebook

- [Gap Filling Process](https://github.com/deepesdl/ML-Toolkits/blob/master/Examples/gapfilling_process.ipynb)