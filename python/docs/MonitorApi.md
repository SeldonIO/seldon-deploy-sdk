# seldon_deploy_client.MonitorApi

All URIs are relative to *https://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**monitor_all**](MonitorApi.md#monitor_all) | **POST** /monitor | 
[**monitor_inference_service**](MonitorApi.md#monitor_inference_service) | **POST** /namespaces/{namespace}/inferenceservices/{name}/monitor | 
[**monitor_namespace**](MonitorApi.md#monitor_namespace) | **POST** /namespaces/{namespace}/monitor | 
[**monitor_seldon_deployment**](MonitorApi.md#monitor_seldon_deployment) | **POST** /namespaces/{namespace}/seldondeployments/{name}/monitor | 


# **monitor_all**
> object monitor_all(monitor_data)



Monitor

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
api_instance = seldon_deploy_client.MonitorApi(seldon_deploy_client.ApiClient(configuration))
monitor_data = seldon_deploy_client.MonitorInputData() # MonitorInputData | Monitor Data

try:
    api_response = api_instance.monitor_all(monitor_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorApi->monitor_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_data** | [**MonitorInputData**](MonitorInputData.md)| Monitor Data | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_inference_service**
> object monitor_inference_service(name, namespace, monitor_data)



Monitor the specified Inference Service

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
api_instance = seldon_deploy_client.MonitorApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
monitor_data = seldon_deploy_client.MonitorInputData() # MonitorInputData | Monitor Data

try:
    api_response = api_instance.monitor_inference_service(name, namespace, monitor_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorApi->monitor_inference_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **monitor_data** | [**MonitorInputData**](MonitorInputData.md)| Monitor Data | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_namespace**
> object monitor_namespace(namespace, monitor_data)



Monitor the specified namespace

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
api_instance = seldon_deploy_client.MonitorApi(seldon_deploy_client.ApiClient(configuration))
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
monitor_data = seldon_deploy_client.MonitorInputData() # MonitorInputData | Monitor Data

try:
    api_response = api_instance.monitor_namespace(namespace, monitor_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorApi->monitor_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **monitor_data** | [**MonitorInputData**](MonitorInputData.md)| Monitor Data | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_seldon_deployment**
> object monitor_seldon_deployment(name, namespace, monitor_data)



Monitor the specified Seldon Deployment

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
api_instance = seldon_deploy_client.MonitorApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
monitor_data = seldon_deploy_client.MonitorInputData() # MonitorInputData | Monitor Data

try:
    api_response = api_instance.monitor_seldon_deployment(name, namespace, monitor_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorApi->monitor_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **monitor_data** | [**MonitorInputData**](MonitorInputData.md)| Monitor Data | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

