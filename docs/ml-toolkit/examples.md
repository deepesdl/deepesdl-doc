# ML Toolkit Examples

Our generic use case aims at the prediction of land surface temperature values based on air temperature values derived from the ESDC 
(Sentinel 3 SLSTR and Terra MODIS sensor, s3 store). 
Satellite monitoring is highly sensitive to atmospheric conditions, in particular to cloud cover, leading to the loss of a significant 
part of data, especially at high latitudes. This may even affect some pixels of an image which are not cloudy, but strongly influenced 
by cloud cover, usually because they were cloudy shortly before the moment of sensing or because of cloud shadows (Sarafanov et al. 2020).
Therefore, remotely sensed land surface temperature images are patchy and gaps need to be filled in to complete the data set. 
Here, we propose a shallow neural network (Linear Regression) to predict missing values of land surface temperature from consistent air 
temperature values.