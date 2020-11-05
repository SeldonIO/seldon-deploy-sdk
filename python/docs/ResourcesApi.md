# seldon_deploy_client.ResourcesApi

All URIs are relative to *http://localhost:8000/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_inference_service_resources**](ResourcesApi.md#list_inference_service_resources) | **GET** /namespaces/{namespace}/inferenceservices/{name}/resources | 
[**list_seldon_deployment_resources**](ResourcesApi.md#list_seldon_deployment_resources) | **GET** /namespaces/{namespace}/seldondeployments/{name}/resources | 


# **list_inference_service_resources**
> list[Component] list_inference_service_resources(namespace, name, endpoint=endpoint, component=component)



list objects of kind resource for Inference Service

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_client
from seldon_deploy_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = seldon_deploy_client.ResourcesApi()
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
name = 'name_example' # str | Name identifies a machine learning model
endpoint = 'endpoint_example' # str | Endpoint differentiates between versions of model (e.g. default, canary... etc) (optional)
component = 'component_example' # str | Component differentiates between types of model (e.g. predictor, explainer... etc) (optional)

try:
    api_response = api_instance.list_inference_service_resources(namespace, name, endpoint=endpoint, component=component)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->list_inference_service_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **name** | **str**| Name identifies a machine learning model | 
 **endpoint** | **str**| Endpoint differentiates between versions of model (e.g. default, canary... etc) | [optional] 
 **component** | **str**| Component differentiates between types of model (e.g. predictor, explainer... etc) | [optional] 

### Return type

[**list[Component]**](Component.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_seldon_deployment_resources**
> list[Component] list_seldon_deployment_resources(namespace, name, endpoint=endpoint, component=component)



list objects of kind resource for Seldon Deployment

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_client
from seldon_deploy_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = seldon_deploy_client.ResourcesApi()
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
name = 'name_example' # str | Name identifies a machine learning model
endpoint = 'endpoint_example' # str | Endpoint differentiates between versions of model (e.g. default, canary... etc) (optional)
component = 'component_example' # str | Component differentiates between types of model (e.g. predictor, explainer... etc) (optional)

try:
    api_response = api_instance.list_seldon_deployment_resources(namespace, name, endpoint=endpoint, component=component)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->list_seldon_deployment_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **name** | **str**| Name identifies a machine learning model | 
 **endpoint** | **str**| Endpoint differentiates between versions of model (e.g. default, canary... etc) | [optional] 
 **component** | **str**| Component differentiates between types of model (e.g. predictor, explainer... etc) | [optional] 

### Return type

[**list[Component]**](Component.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

