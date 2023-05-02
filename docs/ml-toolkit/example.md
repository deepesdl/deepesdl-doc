# ML Toolkit Example Use Case

**LST prediction**

Our generic use case aims at the prediction of land surface temperature values based on air temperature values derived from the ESDC 
(Sentinel 3 SLSTR and Terra MODIS sensor, s3 store). 

Satellite monitoring is highly sensitive to atmospheric conditions, in particular to cloud cover, leading to the loss of a significant 
part of data, especially at high latitudes. This may even affect some pixels of an image which are not cloudy, but strongly influenced 
by cloud cover, usually because they were cloudy shortly before the moment of sensing or because of cloud shadows (Sarafanov et al. 2020).
Therefore, remotely sensed land surface temperature images are patchy and gaps need to be filled in to complete the data set. 
Here, we propose a shallow neural network (Linear Regression) to predict missing values of land surface temperature from consistent air 
temperature values.

_Random Sampling_

In a first step we introduce a random sampling on the ESDC, which is a straight forward procedure in classical machine learning applications. This is done by randomly assigning train and test data on cube level, followed by a random iteration through all chunks of the cube and finally, a chunk-wise model training and testing. As Fig. XX shows, this procedure of random sampling leads to a spiky model response which has mainly two reasons:

(1) Randomly assigning train and test data together with a random iteration through chunks of the ESDC can cause significant changes in the data between the iterations due to great spatio-temporal distances. For example, the model may be fed with data points of a chunk representaing equatorial temperature values followed by data of a chunk from polar regions.

(2) Within every chunk train and test data may be auto-correlated, as data points of parameters (here temperature) are likely to be similar in the Earth system context in their spatio-temporal vicinity.

_Block Sampling_

It is therefore mandatory to enable machine learning that respects the basic principles of geo-data way beyond naive applications of machine learning in the Earth system context. To avoid auto-correlation during the training phase of the model, data sampling should rather be guided by a block sampling strategy. Generally speaking, data blocks can be masks of any kind (e.g., data thresholds, temporally restricted or spatially shaped). Here we use blocks that are rectangularly shaped varying in size and amount of data points.


