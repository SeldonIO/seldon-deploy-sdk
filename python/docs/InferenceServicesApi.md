# seldon_deploy_sdk.InferenceServicesApi

All URIs are relative to *http://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_inference_service**](InferenceServicesApi.md#create_inference_service) | **POST** /namespaces/{namespace}/inferenceservices | 
[**delete_inference_service**](InferenceServicesApi.md#delete_inference_service) | **DELETE** /namespaces/{namespace}/inferenceservices/{name} | 
[**list_inference_services**](InferenceServicesApi.md#list_inference_services) | **GET** /namespaces/{namespace}/inferenceservices | 
[**read_inference_service**](InferenceServicesApi.md#read_inference_service) | **GET** /namespaces/{namespace}/inferenceservices/{name} | 
[**update_inference_service**](InferenceServicesApi.md#update_inference_service) | **PUT** /namespaces/{namespace}/inferenceservices/{name} | 
[**validate_inference_service**](InferenceServicesApi.md#validate_inference_service) | **GET** /namespaces/{namespace}/inferenceservices/validate | 


# **create_inference_service**
> InferenceService create_inference_service(mldeployment, namespace, action=action, message=message)



Create an Inference Service

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
api_instance = seldon_deploy_sdk.InferenceServicesApi(seldon_deploy_sdk.ApiClient(configuration))
mldeployment = seldon_deploy_sdk.InferenceService() # InferenceService | Inference Service
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
action = 'action_example' # str | Action (optional)
message = 'message_example' # str | Message (optional)

try:
    api_response = api_instance.create_inference_service(mldeployment, namespace, action=action, message=message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InferenceServicesApi->create_inference_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mldeployment** | [**InferenceService**](InferenceService.md)| Inference Service | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **action** | **str**| Action | [optional] 
 **message** | **str**| Message | [optional] 

### Return type

[**InferenceService**](InferenceService.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inference_service**
> object delete_inference_service(name, namespace, action=action, message=message)



Delete the specified Inference Service

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
api_instance = seldon_deploy_sdk.InferenceServicesApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
action = 'action_example' # str | Action (optional)
message = 'message_example' # str | Message (optional)

try:
    api_response = api_instance.delete_inference_service(name, namespace, action=action, message=message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InferenceServicesApi->delete_inference_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **action** | **str**| Action | [optional] 
 **message** | **str**| Message | [optional] 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inference_services**
> InferenceServiceList list_inference_services(namespace)



list objects of kind Inference Service

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
api_instance = seldon_deploy_sdk.InferenceServicesApi(seldon_deploy_sdk.ApiClient(configuration))
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.list_inference_services(namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InferenceServicesApi->list_inference_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**InferenceServiceList**](InferenceServiceList.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_inference_service**
> InferenceService read_inference_service(name, namespace)



Read the specified Inference Service

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
api_instance = seldon_deploy_sdk.InferenceServicesApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.read_inference_service(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InferenceServicesApi->read_inference_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**InferenceService**](InferenceService.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inference_service**
> InferenceService update_inference_service(mldeployment, name, namespace, action=action, message=message)



Update the specified Inference Service

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
api_instance = seldon_deploy_sdk.InferenceServicesApi(seldon_deploy_sdk.ApiClient(configuration))
mldeployment = seldon_deploy_sdk.InferenceService() # InferenceService | Inference Service
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
action = 'action_example' # str | Action (optional)
message = 'message_example' # str | Message (optional)

try:
    api_response = api_instance.update_inference_service(mldeployment, name, namespace, action=action, message=message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InferenceServicesApi->update_inference_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mldeployment** | [**InferenceService**](InferenceService.md)| Inference Service | 
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **action** | **str**| Action | [optional] 
 **message** | **str**| Message | [optional] 

### Return type

[**InferenceService**](InferenceService.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_inference_service**
> Message validate_inference_service(namespace, mldeployment)



Validate the given Inference Service

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
api_instance = seldon_deploy_sdk.InferenceServicesApi(seldon_deploy_sdk.ApiClient(configuration))
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
mldeployment = seldon_deploy_sdk.InferenceService() # InferenceService | Inference Service

try:
    api_response = api_instance.validate_inference_service(namespace, mldeployment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InferenceServicesApi->validate_inference_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **mldeployment** | [**InferenceService**](InferenceService.md)| Inference Service | 

### Return type

[**Message**](Message.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

