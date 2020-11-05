# Toleration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effect** | [**TaintEffect**](TaintEffect.md) |  | [optional] 
**key** | **str** | Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. +optional | [optional] 
**operator** | [**TolerationOperator**](TolerationOperator.md) |  | [optional] 
**toleration_seconds** | **int** | TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. +optional | [optional] 
**value** | **str** | Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string. +optional | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


