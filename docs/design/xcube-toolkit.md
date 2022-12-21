# xcube Toolkit

The xcube Toolkit plays a core role in the DeepESDL’s system design. 
Here we briefly introduce the key components of xcube to provide an overview.
More details on specific components are given in the descriptions of 
Tasks 2 and Task 6 below where the specific tools are utilized and extended.

The **xcube ARDC Generator** is a request-driven tool and service used 
to generate analysis-ready data cubes (ARDC) with inputs from one or 
more data stores. 

The **xcube Server** provides a web service that offers several RESTful APIs. 
It publishes collections of ARDCs which are provided by configurable data 
stores but also provides an OGC WMTS and time-series service. 

The **xcube Viewer** is a simple and very easy-to-use single-page web 
application that fully exploits the APIs offered by xcube Server. 

The *data stores* used by the xcube Generator and the xcube Server 
represent different ARDC sources. Data store implementations are 
dynamically registered in the **xcube Data Store Framework**. 
The following data stores are already available

* ESA CCI Open Data Portal (from xcube plugin `xcube-cci`).
* C3S Climate Data Store (from xcube plugin `xcube-cds`).
* CMEMS Data Store (from xcube plugin `xcube-cmems`).
* Sentinel Hub (from xcube plugin `xcube-sh`).
* Generic data stores such as S3-compatible object storage (`s3`), 
  local file system (`file`), and in-memory (`memory`).

Its is planned to develop data stores for the **geoDB** service, 
so users can retrieve vector datasets and rasterized vector data 
sources as gridded ARDCs. 
Other data stores that are needed by DeepESDL Projects will be added 
as required by specific use cases during the project.

The **xcube Python API** provides various high-level functions for 
data analysis that operate on ARDCs and comprises programmatical 
access to all other xcube Components mentioned above. 
Users call the Python API from their own programs, scripts, JNBs, 
or from user code executed in the xcube ARDC Generator. 
During the project, generic functions will be added to the Python API 
to support ML using the ARDCs (see [ML Toolkit](ml-toolkit.md)), 
as well as new use case specific functions as desired in the 
different DeepESDL Projects. 
