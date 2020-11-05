# seldon_deploy_client.SeldonDeploymentsApi

All URIs are relative to *https://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_seldon_deployment**](SeldonDeploymentsApi.md#create_seldon_deployment) | **POST** /namespaces/{namespace}/seldondeployments | 
[**delete_seldon_deployment**](SeldonDeploymentsApi.md#delete_seldon_deployment) | **DELETE** /namespaces/{namespace}/seldondeployments/{name} | 
[**list_seldon_deployments**](SeldonDeploymentsApi.md#list_seldon_deployments) | **GET** /namespaces/{namespace}/seldondeployments | 
[**read_seldon_deployment**](SeldonDeploymentsApi.md#read_seldon_deployment) | **GET** /namespaces/{namespace}/seldondeployments/{name} | 
[**update_seldon_deployment**](SeldonDeploymentsApi.md#update_seldon_deployment) | **PUT** /namespaces/{namespace}/seldondeployments/{name} | 


# **create_seldon_deployment**
> SeldonDeployment create_seldon_deployment(namespace, mldeployment, action=action, message=message)



Create a Seldon Deployment

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_client
from seldon_deploy_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = seldon_deploy_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = seldon_deploy_client.SeldonDeploymentsApi(seldon_deploy_client.ApiClient(configuration))
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
mldeployment = seldon_deploy_client.SeldonDeployment() # SeldonDeployment | Seldon Deployment
action = 'action_example' # str | Action (optional)
message = 'message_example' # str | Message (optional)

try:
    api_response = api_instance.create_seldon_deployment(namespace, mldeployment, action=action, message=message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SeldonDeploymentsApi->create_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **mldeployment** | [**SeldonDeployment**](SeldonDeployment.md)| Seldon Deployment | 
 **action** | **str**| Action | [optional] 
 **message** | **str**| Message | [optional] 

### Return type

[**SeldonDeployment**](SeldonDeployment.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_seldon_deployment**
> object delete_seldon_deployment(name, namespace, action=action, message=message)



Delete the specified Seldon Deployment

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_client
from seldon_deploy_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = seldon_deploy_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = seldon_deploy_client.SeldonDeploymentsApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
action = 'action_example' # str | Action (optional)
message = 'message_example' # str | Message (optional)

try:
    api_response = api_instance.delete_seldon_deployment(name, namespace, action=action, message=message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SeldonDeploymentsApi->delete_seldon_deployment: %s\n" % e)
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

[APIKeyHeader](../README.md#APIKeyHeader)

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

# Configure API key authorization: APIKeyHeader
configuration = seldon_deploy_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = seldon_deploy_client.SeldonDeploymentsApi(seldon_deploy_client.ApiClient(configuration))
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.list_seldon_deployments(namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SeldonDeploymentsApi->list_seldon_deployments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**SeldonDeploymentList**](SeldonDeploymentList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_seldon_deployment**
> SeldonDeployment read_seldon_deployment(name, namespace)



Read the specified Seldon Deployment

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_client
from seldon_deploy_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = seldon_deploy_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = seldon_deploy_client.SeldonDeploymentsApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.read_seldon_deployment(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SeldonDeploymentsApi->read_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**SeldonDeployment**](SeldonDeployment.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_seldon_deployment**
> SeldonDeployment update_seldon_deployment(name, namespace, mldeployment, action=action, message=message)



Update the specified Seldon Deployment

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_client
from seldon_deploy_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = seldon_deploy_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = seldon_deploy_client.SeldonDeploymentsApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
mldeployment = seldon_deploy_client.SeldonDeployment() # SeldonDeployment | Seldon Deployment
action = 'action_example' # str | Action (optional)
message = 'message_example' # str | Message (optional)

try:
    api_response = api_instance.update_seldon_deployment(name, namespace, mldeployment, action=action, message=message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SeldonDeploymentsApi->update_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **mldeployment** | [**SeldonDeployment**](SeldonDeployment.md)| Seldon Deployment | 
 **action** | **str**| Action | [optional] 
 **message** | **str**| Message | [optional] 

### Return type

[**SeldonDeployment**](SeldonDeployment.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

