# HPAScalingPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_seconds** | **int** | PeriodSeconds specifies the window of time for which the policy should hold true. PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min). | [optional] 
**type** | [**HPAScalingPolicyType**](HPAScalingPolicyType.md) |  | [optional] 
**value** | **int** | Value contains the amount of change which is permitted by the policy. It must be greater than zero | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


