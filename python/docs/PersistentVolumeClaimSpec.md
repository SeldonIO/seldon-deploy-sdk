# PersistentVolumeClaimSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_modes** | [**list[PersistentVolumeAccessMode]**](PersistentVolumeAccessMode.md) | accessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1 +optional | [optional] 
**data_source** | [**TypedLocalObjectReference**](TypedLocalObjectReference.md) |  | [optional] 
**data_source_ref** | [**TypedObjectReference**](TypedObjectReference.md) |  | [optional] 
**resources** | [**ResourceRequirements**](ResourceRequirements.md) |  | [optional] 
**selector** | [**LabelSelector**](LabelSelector.md) |  | [optional] 
**storage_class_name** | **str** | storageClassName is the name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1 +optional | [optional] 
**volume_mode** | [**PersistentVolumeMode**](PersistentVolumeMode.md) |  | [optional] 
**volume_name** | **str** | volumeName is the binding reference to the PersistentVolume backing this claim. +optional | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


