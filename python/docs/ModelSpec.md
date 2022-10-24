# ModelSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact_version** | **int** | Artifact Version A v2 version folder to select from storage bucket +optional | [optional] 
**dedicated** | **bool** | Dedicated server exclusive to this model Default false | [optional] 
**explainer** | [**ExplainerSpec**](ExplainerSpec.md) |  | [optional] 
**logger** | [**LoggingSpec**](LoggingSpec.md) |  | [optional] 
**max_replicas** | **int** | Max number of replicas - default equal to replicas | [optional] 
**memory** | [**Quantity**](Quantity.md) |  | [optional] 
**min_replicas** | **int** | Min number of replicas - default equal to replicas | [optional] 
**model_type** | **str** | Model type +optional | [optional] 
**parameters** | [**list[ParameterSpec]**](ParameterSpec.md) | Parameters to load with model | [optional] 
**preloaded** | **bool** | Model already loaded on a server. Don&#39;t schedule. Default false | [optional] 
**replicas** | **int** | Number of replicas - default 1 | [optional] 
**requirements** | **list[str]** | List of extra requirements for this model to be loaded on a compatible server | [optional] 
**schema_uri** | **str** | Schema URI +optional | [optional] 
**secret_name** | **str** | Secret name +optional | [optional] 
**server** | **str** | Name of the Server to deploy this artifact +optional | [optional] 
**storage_uri** | **str** | Storage URI for the model repository | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


