# SeldonDeploymentStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**SeldonAddressable**](SeldonAddressable.md) |  | [optional] 
**annotations** | **dict(str, str)** | Annotations is additional Status fields for the Resource to save some additional State as well as convey more information to the user. This is roughly akin to Annotations on any k8s resource, just the reconciler conveying richer information outwards. | [optional] 
**conditions** | [**Conditions**](Conditions.md) |  | [optional] 
**deployment_status** | [**dict(str, DeploymentStatus)**](DeploymentStatus.md) |  | [optional] 
**description** | **str** |  | [optional] 
**observed_generation** | **int** | ObservedGeneration is the &#39;Generation&#39; of the Service that was last processed by the controller. +optional | [optional] 
**replicas** | **int** |  | [optional] 
**service_status** | [**dict(str, ServiceStatus)**](ServiceStatus.md) |  | [optional] 
**state** | [**StatusState**](StatusState.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


