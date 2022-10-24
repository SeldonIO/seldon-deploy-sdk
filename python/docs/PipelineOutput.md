# PipelineOutput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**join_window_ms** | **int** | msecs to wait for messages from multiple inputs to arrive before joining the inputs | [optional] 
**steps** | **list[str]** | Previous step to receive data from | [optional] 
**steps_join** | [**JoinType**](JoinType.md) |  | [optional] 
**tensor_map** | **dict(str, str)** | Map of tensor name conversions to use e.g. output1 -&gt; input1 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


