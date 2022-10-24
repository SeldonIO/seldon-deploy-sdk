# PipelineStep

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch** | [**PipelineBatch**](PipelineBatch.md) |  | [optional] 
**inputs** | **list[str]** | Previous step to receive data from | [optional] 
**inputs_join_type** | [**JoinType**](JoinType.md) |  | [optional] 
**join_window_ms** | **int** | msecs to wait for messages from multiple inputs to arrive before joining the inputs | [optional] 
**name** | **str** | Name of the step | [optional] 
**tensor_map** | **dict(str, str)** | Map of tensor name conversions to use e.g. output1 -&gt; input1 | [optional] 
**triggers** | **list[str]** | Triggers required to activate step | [optional] 
**triggers_join_type** | [**JoinType**](JoinType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


