# ManagedFieldsEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the version of this resource that this field set applies to. The format is \&quot;group/version\&quot; just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted. | [optional] 
**fields_type** | **str** | FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: \&quot;FieldsV1\&quot; | [optional] 
**fields_v1** | [**FieldsV1**](FieldsV1.md) |  | [optional] 
**manager** | **str** | Manager is an identifier of the workflow managing these fields. | [optional] 
**operation** | [**ManagedFieldsOperationType**](ManagedFieldsOperationType.md) |  | [optional] 
**time** | **str** | Time is timestamp of when these fields were set. It should always be empty if Operation is &#39;Apply&#39; +optional | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


