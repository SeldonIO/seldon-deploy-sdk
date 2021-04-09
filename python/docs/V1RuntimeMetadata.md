# V1RuntimeMetadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_uri** | **str** | The URI for the storage bucket containing the model, or the URI to the docker image for custom models. | [optional] 
**deployment_name** | **str** | The name of the Kubernetes deployment that is associated with a model. | [optional] 
**deployment_namespace** | **str** | The Kubernetes namespace in which this deployment is running in. | [optional] 
**deployment_kubernetes_uid** | **str** | The Kubernetes UID of the deployment associated with a model. See https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids for details | [optional] 
**predictor_name** | **str** | The name of the predictor inside the deployment that contains the referenced model. | [optional] 
**node_name** | **str** | The name of the node inside the predictor that contains the referenced model. This is relevant and populated only for SeldonDeployment deployment types. | [optional] 
**deployment_status** | [**V1DeploymentStatus**](V1DeploymentStatus.md) | The status of the Kubernetes deployment associated with a model. | [optional] 
**deployment_type** | [**V1DeploymentType**](V1DeploymentType.md) | The type of deployment - either SeldonDeployment or InferenceService. | [optional] 
**traffic** | **str** | The amount of traffic server by this model in the deployment. | [optional] 
**shadow** | **bool** | True if this model is a shadow in the deployment. | [optional] 
**creation_time** | **datetime** | The creation timestamp for the runtime model metadata entry. It is automatically created by the Metadata service and cannot be modified. The timestamp is using the [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format/ | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


