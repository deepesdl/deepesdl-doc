# ML Toolkits - Introduction

AI is becoming increasingly important in Earth observations as most parts 
of the Earth system are continuously monitored by sensors and AI is able to 
cope  with both the volume of data and the heterogeneous data 
characteristics. For instance, satellites monitor the atmosphere, land, and 
ocean with unprecedented accuracy. In course of DeepESDL, the Earth System 
Data Lab (ESDL) capabilities have been extended to support the application of 
machine learning (ML) methods on Earth System Data Cubes (ESDC). 

We provide three Python-based best practice Jupyter Notebooks based on a 
generic use case to showcase the implementation of state-of-the-art machine 
learning libraries on ESDCs in the DeepESDL Hub environment. 
Each Jupyter Notebook involves a self-contained workflow, markdown cells, 
comments and plots for user-friendly application and guidance and is based 
on one of the three well established open source ML libraries respectively:

1.    [scikit-learn](https://scikit-learn.org/stable/)<br>
      For classical machine learning such as support vector machines, decision trees, regressions or clustering, scikit-learn provides a broad set of features that fulfils many basic requirements.
2.    [PyTorch](https://pytorch.org/)<br>
      For larger neural networks and support for Deep Learning additional ML toolchains are necessary, for example the python-based ML stack PyTorch. With PyTorch, experienced users are supported. It
      provides low-level API and allows for flexibility to develop and customize deep learning models. It allows for GPU computation and supports transfer learning, domain adaptation, or diverse methods
      for fine tuning of models.
3.    [TensorFlow](https://www.tensorflow.org/overview)<br>
      Keras provides a high-level API that can be run on the popular execution backend TensorFlow. Due to its simplicity, it fits well to the requirements of those Earth system scientist that do not           require to newly develop neuronal network architectures. As PyTorch, TensorFlow is python-based, allows for GPU computation and it supports Deep Learning applications including transfer learning         or domain adaptation.

Model evaluation is realized through the implementation of [TensorBoard](https://www.tensorflow.org/tensorboard) and 
[mlflow](https://mlflow.org/).

![ML Toolkit Scheme](https://github.com/deepesdl/deepesdl-doc/blob/anja-xxx-ml_toolkit/docs/img/mltoolkit_scheme.png)
*Machine Learning workflow on Analysis Ready Data Cubes*

One may also want to reuse information gained during model training for a 
second related task, especially when it comes to a lack of data. A PyTorch 
based Jupyter Notebook provides the implementation of 
[Transfer Learning](https://github.com/deepesdl/ML-Toolkit/blob/master/src/transfer_learning.ipynb). 

## Overview
1. [Getting Started](getting-started.md)    
2. [Example Use Case and Juypter Notebooks](example.md)
   
