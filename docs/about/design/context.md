# Context

The design of DeepESDL is focused on the idea of on-boarding new 
*DeepESDL user projects* with the help of the 
*DeepESDL Hub* which can be seen as an implementation of the 
[ESA Earth Science Hub](https://www.esa.int/Applications/Observing_the_Earth/FutureEO/Boosting_Earth_science). 
Accordingly, a DeepESDL user project may support specific 
[ESA EO for Society](https://eo4society.esa.int/) 
research projects and activities that are aggregated in *Science Clusters* 
such as

* [ESA Atmosphere Science Cluster](https://eo4society.esa.int/communities/scientists/esa-atmosphere-science-cluster/).
* [ESA Carbon Science Cluster](https://eo4society.esa.int/communities/scientists/esa-carbon-science-cluster/).
* [ESA Ocean Science Cluster](https://eo4society.esa.int/communities/scientists/esa-ocean-science-cluster/).
* [ESA Polar Science Cluster](https://eo4society.esa.int/communities/scientists/esa-polar-science-cluster/).


The [DeepESDL Hub](hub.md) manages user projects and their users. 
The Hub provides for each project a workspace or tenant, 
assigns project resources, hosts project artifacts, provides a dashboard 
for result dissemination, and integrates team collaboration tools. 
It also controls visibility of results of individual user projects so 
that they can be made part of a DeepESDL public portrayal.

A DeepESDL user project comprises numerous own applications, interfaces, 
services, and data available in the provided workspace. 
Service access and application deployments are managed by the 
*Control Plane* of the DeepESDL Hub. Actual workloads are 
scaled on the *Worker Plane*.
