# ResourceRequirements

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claims** | [**list[ResourceClaim]**](ResourceClaim.md) | Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.  This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.  This field is immutable. It can only be set for containers.  +listType&#x3D;map +listMapKey&#x3D;name +featureGate&#x3D;DynamicResourceAllocation +optional | [optional] 
**limits** | [**ResourceList**](ResourceList.md) |  | [optional] 
**requests** | [**ResourceList**](ResourceList.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


