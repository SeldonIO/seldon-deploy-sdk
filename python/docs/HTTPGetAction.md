# HTTPGetAction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Host name to connect to, defaults to the pod IP. You probably want to set \&quot;Host\&quot; in httpHeaders instead. +optional | [optional] 
**http_headers** | [**list[HTTPHeader]**](HTTPHeader.md) | Custom headers to set in the request. HTTP allows repeated headers. +optional | [optional] 
**path** | **str** | Path to access on the HTTP server. +optional | [optional] 
**port** | [**IntOrString**](IntOrString.md) |  | [optional] 
**scheme** | [**URIScheme**](URIScheme.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


