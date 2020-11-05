# seldon_deploy_client.MldeploymentsApi

All URIs are relative to *http://localhost:8000/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_inference_service**](MldeploymentsApi.md#create_inference_service) | **POST** /namespaces/{namespace}/inferenceservices | 
[**create_seldon_deployment**](MldeploymentsApi.md#create_seldon_deployment) | **POST** /namespaces/{namespace}/seldondeployments | 
[**delete_inference_service**](MldeploymentsApi.md#delete_inference_service) | **DELETE** /namespaces/{namespace}/inferenceservices/{name} | 
[**delete_seldon_deployment**](MldeploymentsApi.md#delete_seldon_deployment) | **DELETE** /namespaces/{namespace}/seldondeployments/{name} | 
[**list_inference_services**](MldeploymentsApi.md#list_inference_services) | **GET** /namespaces/{namespace}/inferenceservices | 
[**list_ml_deployments**](MldeploymentsApi.md#list_ml_deployments) | **GET** /namespaces/{namespace}/mldeployments | 
[**list_seldon_deployments**](MldeploymentsApi.md#list_seldon_deployments) | **GET** /namespaces/{namespace}/seldondeployments | 
[**read_inference_service**](MldeploymentsApi.md#read_inference_service) | **GET** /namespaces/{namespace}/inferenceservices/{name} | 
[**read_seldon_deployment**](MldeploymentsApi.md#read_seldon_deployment) | **GET** /namespaces/{namespace}/seldondeployments/{name} | 
[**update_inference_service**](MldeploymentsApi.md#update_inference_service) | **PUT** /namespaces/{namespace}/inferenceservices/{name} | 
[**update_seldon_deployment**](MldeploymentsApi.md#update_seldon_deployment) | **PUT** /namespaces/{namespace}/seldondeployments/{name} | 


# **create_inference_service**
> InferenceService create_inference_service(namespace, mldeployment=mldeployment, message=message, action=action)



Create an Inference Service

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_client
from seldon_deploy_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = seldon_deploy_client.MldeploymentsApi()
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
mldeployment = 'mldeployment_example' # str | Machine Learning Deployment (optional)
message = 'message_example' # str | Message (optional)
action = 'action_example' # str | Action (optional)

try:
    api_response = api_instance.create_inference_service(namespace, mldeployment=mldeployment, message=message, action=action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MldeploymentsApi->create_inference_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **mldeployment** | **str**| Machine Learning Deployment | [optional] 
 **message** | **str**| Message | [optional] 
 **action** | **str**| Action | [optional] 

### Return type

[**InferenceService**](InferenceService.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_seldon_deployment**
> SeldonDeployment create_seldon_deployment(namespace, mldeployment=mldeployment, message=message, action=action)



Create a Seldon Deployment

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_client
from seldon_deploy_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = seldon_deploy_client.MldeploymentsApi()
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
mldeployment = 'mldeployment_example' # str | Machine Learning Deployment (optional)
message = 'message_example' # str | Message (optional)
action = 'action_example' # str | Action (optional)

try:
    api_response = api_instance.create_seldon_deployment(namespace, mldeployment=mldeployment, message=message, action=action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MldeploymentsApi->create_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **mldeployment** | **str**| Machine Learning Deployment | [optional] 
 **message** | **str**| Message | [optional] 
 **action** | **str**| Action | [optional] 

### Return type

[**SeldonDeployment**](SeldonDeployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inference_service**
> delete_inference_service(namespace, name, message=message, action=action)



Delete the specified Inference Service

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_client
from seldon_deploy_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = seldon_deploy_client.MldeploymentsApi()
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
name = 'name_example' # str | Name identifies a resource
message = 'message_example' # str | Message (optional)
action = 'action_example' # str | Action (optional)

try:
    api_instance.delete_inference_service(namespace, name, message=message, action=action)
except ApiException as e:
    print("Exception when calling MldeploymentsApi->delete_inference_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **name** | **str**| Name identifies a resource | 
 **message** | **str**| Message | [optional] 
 **action** | **str**| Action | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_seldon_deployment**
> delete_seldon_deployment(namespace, name, message=message, action=action)



Delete the specified Seldon Deployment

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_client
from seldon_deploy_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = seldon_deploy_client.MldeploymentsApi()
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
name = 'name_example' # str | Name identifies a resource
message = 'message_example' # str | Message (optional)
action = 'action_example' # str | Action (optional)

try:
    api_instance.delete_seldon_deployment(namespace, name, message=message, action=action)
except ApiException as e:
    print("Exception when calling MldeploymentsApi->delete_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **name** | **str**| Name identifies a resource | 
 **message** | **str**| Message | [optional] 
 **action** | **str**| Action | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

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
import seldon_deploy_client
from seldon_deploy_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = seldon_deploy_client.MldeploymentsApi()
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.list_inference_services(namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MldeploymentsApi->list_inference_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**InferenceServiceList**](InferenceServiceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ml_deployments**
> MLDeploymentList list_ml_deployments(namespace)



list objects of kind Machine Learning Deployment (Seldon Deployment & Inference Service)

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_client
from seldon_deploy_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = seldon_deploy_client.MldeploymentsApi()
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.list_ml_deployments(namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MldeploymentsApi->list_ml_deployments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**MLDeploymentList**](MLDeploymentList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_seldon_deployments**
> SeldonDeploymentList list_seldon_deployments(namespace)



list objects of kind Seldon Deployment

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_client
from seldon_deploy_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = seldon_deploy_client.MldeploymentsApi()
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.list_seldon_deployments(namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MldeploymentsApi->list_seldon_deployments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**SeldonDeploymentList**](SeldonDeploymentList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_inference_service**
> InferenceService read_inference_service(namespace, name)



Read the specified Inference Service

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_client
from seldon_deploy_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = seldon_deploy_client.MldeploymentsApi()
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
name = 'name_example' # str | Name identifies a resource

try:
    api_response = api_instance.read_inference_service(namespace, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MldeploymentsApi->read_inference_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **name** | **str**| Name identifies a resource | 

### Return type

[**InferenceService**](InferenceService.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_seldon_deployment**
> SeldonDeployment read_seldon_deployment(namespace, name)



Read the specified Seldon Deployment

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_client
from seldon_deploy_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = seldon_deploy_client.MldeploymentsApi()
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
name = 'name_example' # str | Name identifies a resource

try:
    api_response = api_instance.read_seldon_deployment(namespace, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MldeploymentsApi->read_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **name** | **str**| Name identifies a resource | 

### Return type

[**SeldonDeployment**](SeldonDeployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inference_service**
> InferenceService update_inference_service(namespace, name, mldeployment=mldeployment, message=message, action=action)



Update the specified Inference Service

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_client
from seldon_deploy_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = seldon_deploy_client.MldeploymentsApi()
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
name = 'name_example' # str | Name identifies a resource
mldeployment = 'mldeployment_example' # str | Machine Learning Deployment (optional)
message = 'message_example' # str | Message (optional)
action = 'action_example' # str | Action (optional)

try:
    api_response = api_instance.update_inference_service(namespace, name, mldeployment=mldeployment, message=message, action=action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MldeploymentsApi->update_inference_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **name** | **str**| Name identifies a resource | 
 **mldeployment** | **str**| Machine Learning Deployment | [optional] 
 **message** | **str**| Message | [optional] 
 **action** | **str**| Action | [optional] 

### Return type

[**InferenceService**](InferenceService.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_seldon_deployment**
> SeldonDeployment update_seldon_deployment(namespace, name, mldeployment=mldeployment, message=message, action=action)



Update the specified Seldon Deployment

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_client
from seldon_deploy_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = seldon_deploy_client.MldeploymentsApi()
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
name = 'name_example' # str | Name identifies a resource
mldeployment = 'mldeployment_example' # str | Machine Learning Deployment (optional)
message = 'message_example' # str | Message (optional)
action = 'action_example' # str | Action (optional)

try:
    api_response = api_instance.update_seldon_deployment(namespace, name, mldeployment=mldeployment, message=message, action=action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MldeploymentsApi->update_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **name** | **str**| Name identifies a resource | 
 **mldeployment** | **str**| Machine Learning Deployment | [optional] 
 **message** | **str**| Message | [optional] 
 **action** | **str**| Action | [optional] 

### Return type

[**SeldonDeployment**](SeldonDeployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

