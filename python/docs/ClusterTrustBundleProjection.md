# ClusterTrustBundleProjection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_selector** | [**LabelSelector**](LabelSelector.md) |  | [optional] 
**name** | **str** | Select a single ClusterTrustBundle by object name.  Mutually-exclusive with signerName and labelSelector. +optional | [optional] 
**optional** | **bool** | If true, don&#39;t block pod startup if the referenced ClusterTrustBundle(s) aren&#39;t available.  If using name, then the named ClusterTrustBundle is allowed not to exist.  If using signerName, then the combination of signerName and labelSelector is allowed to match zero ClusterTrustBundles. +optional | [optional] 
**path** | **str** | Relative path from the volume root to write the bundle. | [optional] 
**signer_name** | **str** | Select all ClusterTrustBundles that match this signer name. Mutually-exclusive with name.  The contents of all selected ClusterTrustBundles will be unified and deduplicated. +optional | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


