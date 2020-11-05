# InferenceServiceStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Addressable**](Addressable.md) |  | [optional] 
**annotations** | **dict(str, str)** | Annotations is additional Status fields for the Resource to save some additional State as well as convey more information to the user. This is roughly akin to Annotations on any k8s resource, just the reconciler conveying richer information outwards. | [optional] 
**canary** | **object** | Statuses for the canary endpoints of the InferenceService | [optional] 
**canary_traffic** | **int** | Traffic percentage that goes to canary services | [optional] 
**conditions** | [**Conditions**](Conditions.md) |  | [optional] 
**default** | **object** | Statuses for the default endpoints of the InferenceService | [optional] 
**observed_generation** | **int** | ObservedGeneration is the &#39;Generation&#39; of the Service that was last processed by the controller. +optional | [optional] 
**traffic** | **int** | Traffic percentage that goes to default services | [optional] 
**url** | **str** | URL of the InferenceService | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


