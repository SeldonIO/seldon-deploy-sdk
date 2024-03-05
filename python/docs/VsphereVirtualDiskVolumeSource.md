# VsphereVirtualDiskVolumeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_type** | **str** | fsType is filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Implicitly inferred to be \&quot;ext4\&quot; if unspecified. +optional | [optional] 
**storage_policy_id** | **str** | storagePolicyID is the storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName. +optional | [optional] 
**storage_policy_name** | **str** | storagePolicyName is the storage Policy Based Management (SPBM) profile name. +optional | [optional] 
**volume_path** | **str** | volumePath is the path that identifies vSphere volume vmdk | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


