# V1Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | The URI for the storage bucket containing the model, or the URI to the docker image for custom models. It must be a valid URI as defined in RFC 3986, and must not exceed 200 characters. | 
**name** | **str** | The name of the model. It must not exceed 200 characters. | [optional] 
**version** | **str** | The version of the model. It must not exceed 50 characters. | [optional] [default to '"v0.0.1"']
**artifact_type** | [**V1ArtifactType**](V1ArtifactType.md) | The artifact type of the model. This is the library used to develop the model. | [optional] 
**task_type** | **str** | The task type of the model. It must not exceed 50 characters. | [optional] 
**tags** | **dict(str, str)** | Key-value pairs of arbitrary metadata associated with the model. Each key and value must not exceed 100 and 500 characters respectively. | [optional] 
**metrics** | **dict(str, float)** | Key-value pairs of static metrics associated with the model. For dynamic metrics look into metrics https://deploy.seldon.io/docs/getting-started/production-installation/metrics/ . Keys must not exceed 100 characters. | [optional] 
**creation_time** | **datetime** | The creation timestamp for the model metadata entry. It is automatically created by the Metadata service and cannot be modified. The timestamp is using the [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format/ | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


