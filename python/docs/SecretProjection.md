# SecretProjection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**list[KeyToPath]**](KeyToPath.md) | items if unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the &#39;..&#39; path or start with &#39;..&#39;. +optional | [optional] 
**name** | **str** | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid? +optional | [optional] 
**optional** | **bool** | optional field specify whether the Secret or its key must be defined +optional | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


