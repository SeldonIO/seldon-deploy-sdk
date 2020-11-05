# InferenceServiceStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Addressable**](Addressable.md) |  | [optional] 
**canary** | [**ComponentStatusMap**](ComponentStatusMap.md) |  | [optional] 
**canary_traffic** | **int** | Traffic percentage that goes to canary services | [optional] 
**conditions** | [**Conditions**](Conditions.md) |  | [optional] 
**default** | [**ComponentStatusMap**](ComponentStatusMap.md) |  | [optional] 
**observed_generation** | **int** | ObservedGeneration is the &#39;Generation&#39; of the Service that was last processed by the controller. +optional | [optional] 
**traffic** | **int** | Traffic percentage that goes to default services | [optional] 
**url** | **str** | URL of the InferenceService | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


