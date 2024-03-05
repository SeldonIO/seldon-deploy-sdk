# HPAScalingRules

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**list[HPAScalingPolicy]**](HPAScalingPolicy.md) | policies is a list of potential scaling polices which can be used during scaling. At least one policy must be specified, otherwise the HPAScalingRules will be discarded as invalid +optional | [optional] 
**select_policy** | [**ScalingPolicySelect**](ScalingPolicySelect.md) |  | [optional] 
**stabilization_window_seconds** | **int** | stabilizationWindowSeconds is the number of seconds for which past recommendations should be considered while scaling up or scaling down. StabilizationWindowSeconds must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: For scale up: 0 (i.e. no stabilization is done). For scale down: 300 (i.e. the stabilization window is 300 seconds long). +optional | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


