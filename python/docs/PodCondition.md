# PodCondition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_probe_time** | **str** | Last time we probed the condition. +optional | [optional] 
**last_transition_time** | **str** | Last time the condition transitioned from one status to another. +optional | [optional] 
**message** | **str** | Human-readable message indicating details about last transition. +optional | [optional] 
**reason** | **str** | Unique, one-word, CamelCase reason for the condition&#39;s last transition. +optional | [optional] 
**status** | [**ConditionStatus**](ConditionStatus.md) |  | [optional] 
**type** | [**PodConditionType**](PodConditionType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


