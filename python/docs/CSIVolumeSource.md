# CSIVolumeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver** | **str** | driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster. | [optional] 
**fs_type** | **str** | fsType to mount. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply. +optional | [optional] 
**node_publish_secret_ref** | [**LocalObjectReference**](LocalObjectReference.md) |  | [optional] 
**read_only** | **bool** | readOnly specifies a read-only configuration for the volume. Defaults to false (read/write). +optional | [optional] 
**volume_attributes** | **dict(str, str)** | volumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver&#39;s documentation for supported values. +optional | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


