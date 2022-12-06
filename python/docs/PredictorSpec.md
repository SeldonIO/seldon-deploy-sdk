# PredictorSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** |  | [optional] 
**component_specs** | [**list[SeldonPodSpec]**](SeldonPodSpec.md) |  | [optional] 
**engine_resources** | [**ResourceRequirements**](ResourceRequirements.md) |  | [optional] 
**explainer** | [**Explainer**](Explainer.md) |  | [optional] 
**graph** | [**PredictiveUnit**](PredictiveUnit.md) |  | [optional] 
**labels** | **dict(str, str)** |  | [optional] 
**name** | **str** |  | [optional] 
**progress_deadline_seconds** | **int** |  | [optional] 
**replicas** | **int** |  | [optional] 
**shadow** | **bool** |  | [optional] 
**ssl** | [**SSL**](SSL.md) |  | [optional] 
**svc_orch_spec** | [**SvcOrchSpec**](SvcOrchSpec.md) |  | [optional] 
**traffic** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


