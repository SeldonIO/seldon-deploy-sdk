# DetectorDeploymentConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_source** | **str** |  | [optional] 
**event_type** | **str** |  | [optional] 
**http_port** | **str** |  | [optional] 
**memory_requirement** | **str** |  | [optional] 
**model_name** | **str** |  | [optional] 
**prom_scraping** | **bool** |  | [optional] 
**protocol** | **str** | For model inference, Seldon recommends using the industry-standard Open Inference Protocol (OIP) as the preferred protocol over others.&lt;br&gt;The corresponding protocol OIP value for Seldon Deployment detectors is &#39;kfserving.http&#39;. For Seldon ML Pipelines, this is the only supported protocol.&lt;br&gt;For more information, please refer to the Seldon documentation: https://docs.seldon.ai/seldon-core-2/apis/inference/v2 | [optional] 
**reply_url** | **str** |  | [optional] 
**user_permission** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


