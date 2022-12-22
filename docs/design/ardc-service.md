# DeepESDL ARDC Service

DeepESDL offers a flexible ARDC generation tool for data cube generation 
that is made available via a dedicated JupyterLab profile. 
The ARDC generation tool reads data streams from one or more data stores, 
then it resamples and combines them. The merged ARDC can then be 
manipulated by user-provided Python code 
(BYOA concept: bring-your-own-algorithm) before the resulting 
ARDC is written into another data store, for example AWS S3.

![xcube Generator schema](../img/ardc-gen.png)

The current features of the xcube generation service are:

* Read data streams from a variety of xcube data stores
  (see [xcube Toolkit](./xcube-toolkit.md)).
* Perform spatial resampling of raw and rectified data streams to 
  a common spatial grid using standard coordinate reference systems, e.g., 
  EU LAEA (EPSG:3035).
* Perform temporal resampling by aggregating observations to equally 
  sized time periods, e.g., 8-day averages. 
* Merge resampled data streams into a single cube, optionally 
  passing it to user Python code for further value adding or transformation.
* Write chunked data cube into remote object storage or the 
  local file system.
