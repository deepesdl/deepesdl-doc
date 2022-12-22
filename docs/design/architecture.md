# DeepESDL Architecture

The DeepESDL system comprises numerous distributed services and 
applications as introduced in the [DeepESDL Context](./concept.md). 
All of them are containerized and are executed in a common cloud 
environment. 
To orchestrate, monitor, maintain, and scale the variety of 
DeepESDL services and applications, we use today’s most popular 
container orchestrator Kubernetes (K8s). This supports the idea 
that the DeepESDL system is deployable on any Cloud environment that 
can run a K8s service (this is, AWS, Google, Microsoft Azure, and 
many others including all DIAS instances). The 
initial system is deployed on Amazon Web Services (AWS) in the EU-Central-1 
region, 
which is physically located in Frankfurt, Germany, Europe using the 
managed K8s service EKS, which is critical for cost-efficiency and 
reliability of DeepESDL. 

To be able to meet the ambitious requirements for the service, 
we must base the solution mainly on existing technologies. 
Many of the DeepESDL system components have been developed in former 
(mostly ESA) projects and are thus reused, adapted, extended, and branded 
for DeepESDL. Examples are

* **DeepESDL Hub** is based on EOxHub developed by EOX and used for
  example in the ESA EuroDataCube project;
* **xcube ARDC Generator**, **xcube Server**, **xcube Viewer** 
  are derived from already available components in the
  [xcube Toolkit](./xcube-toolkit.md) 
  developed and used in several activities by the development team;
* The **Cube 4D Viewer** is an adopted version of Earthwave’s 4D Viewer.

