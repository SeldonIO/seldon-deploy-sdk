# ScaleIOVolumeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_type** | **str** | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Default is \&quot;xfs\&quot;. +optional | [optional] 
**gateway** | **str** | gateway is the host address of the ScaleIO API Gateway. | [optional] 
**protection_domain** | **str** | protectionDomain is the name of the ScaleIO Protection Domain for the configured storage. +optional | [optional] 
**read_only** | **bool** | readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. +optional | [optional] 
**secret_ref** | [**LocalObjectReference**](LocalObjectReference.md) |  | [optional] 
**ssl_enabled** | **bool** | sslEnabled Flag enable/disable SSL communication with Gateway, default false +optional | [optional] 
**storage_mode** | **str** | storageMode indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned. +optional | [optional] 
**storage_pool** | **str** | storagePool is the ScaleIO Storage Pool associated with the protection domain. +optional | [optional] 
**system** | **str** | system is the name of the storage system as configured in ScaleIO. | [optional] 
**volume_name** | **str** | volumeName is the name of a volume already created in the ScaleIO system that is associated with this volume source. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


