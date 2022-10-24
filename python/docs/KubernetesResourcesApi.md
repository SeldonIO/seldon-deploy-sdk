# seldon_deploy_sdk.KubernetesResourcesApi

All URIs are relative to *http://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_seldon_deployment_resources**](KubernetesResourcesApi.md#list_seldon_deployment_resources) | **GET** /namespaces/{namespace}/seldondeployments/{name}/resources | 


# **list_seldon_deployment_resources**
> list[Component] list_seldon_deployment_resources(name, namespace, component=component)



list objects of kind resource for Seldon Deployment

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_sdk
from seldon_deploy_sdk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = seldon_deploy_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = seldon_deploy_sdk.KubernetesResourcesApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
component = 'component_example' # str | Component differentiates between types of model (e.g. predictor, explainer... etc) (optional)

try:
    api_response = api_instance.list_seldon_deployment_resources(name, namespace, component=component)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KubernetesResourcesApi->list_seldon_deployment_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **component** | **str**| Component differentiates between types of model (e.g. predictor, explainer... etc) | [optional] 

### Return type

[**list[Component]**](Component.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

