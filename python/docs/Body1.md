# Body1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**predictor_name** | **str** | The predictor name of the seldon deployment to get inference logs for. e.g. \&quot;default\&quot;, \&quot;canary\&quot;, \&quot;shadow\&quot; | 
**container_name** | **str** | The container name of the seldon deployment to get inference logs for. e.g. \&quot;my-container\&quot;, \&quot;input-transformer\&quot;, \&quot;output-transformer\&quot; | 
**start_time** | **datetime** | The start time of the inference logs to get. | [optional] 
**end_time** | **datetime** | The end time of the inference logs to get. | [optional] 
**limit** | **int** | The maximum number of inference logs to get. | [optional] 
**page_token** | **str** | The page token to use to get the next page of inference logs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


