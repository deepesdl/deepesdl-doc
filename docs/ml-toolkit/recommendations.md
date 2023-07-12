Ideally, classical operations on the Analysis Ready Data Cubes (ARDC) could be extended by Machine Learning applications in order to sustain interoperability. 
However, there is a conflict between the nature of remotely-sensed data, the structure of the ARDCs and the requirements for meaningful Machine Learning applications which need to be addressed:

1. Sampling the Earth naturally leads to an uneven distribution of data points as a result of its spherical shape.
   This phenomenon is reinforced by data gaps due to e.g., satellite trajectories or cloud cover. Hence, there is no uniform data distribution across the chunks of the ARDC provided.

2. Remotely sensed data tends to be auto-correlated within (neighboring) chunks as data points which are in close spatio-temporal vicinity are naturally characterized by a low variance.

Therefore, it is mandatory to enable Machine Learning that respects the basic principles of geo-data way beyond naive applications of Machine Learning in the Earth system context. 
More specific, sophisticated and efficient sampling strategies need to be developed. We here propose the usage of [block sampling](https://github.com/deepesdl/deepesdl-doc/blob/anja-xxx-ml_toolkit/docs/ml-toolkit/example.md#block-sampling) instead of random sampling, which accounts for 
challenges 1. and 2. and enables efficient and more meaningful ML applications on ARDCs. However, this is strongly depentend on the data and the scientific use case and needs to be evaluated by the domain expert.
