# AzureDiskVolumeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caching_mode** | [**AzureDataDiskCachingMode**](AzureDataDiskCachingMode.md) |  | [optional] 
**disk_name** | **str** | The Name of the data disk in the blob storage | [optional] 
**disk_uri** | **str** | The URI the data disk in the blob storage | [optional] 
**fs_type** | **str** | Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Implicitly inferred to be \&quot;ext4\&quot; if unspecified. +optional | [optional] 
**kind** | [**AzureDataDiskKind**](AzureDataDiskKind.md) |  | [optional] 
**read_only** | **bool** | Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. +optional | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


