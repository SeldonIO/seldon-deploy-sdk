# seldon_deploy_client.MetricsServerApi

All URIs are relative to *https://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_metrics_server_seldon_deployment**](MetricsServerApi.md#create_metrics_server_seldon_deployment) | **POST** /namespaces/{namespace}/seldondeployments/{name}/metricsserver | 
[**delete_metrics_server_seldon_deployment**](MetricsServerApi.md#delete_metrics_server_seldon_deployment) | **DELETE** /namespaces/{namespace}/seldondeployments/{name}/metricsserver | 
[**read_metrics_server_seldon_deployment**](MetricsServerApi.md#read_metrics_server_seldon_deployment) | **GET** /namespaces/{namespace}/seldondeployments/{name}/metricsserver | 


# **create_metrics_server_seldon_deployment**
> AlibiDetectorData create_metrics_server_seldon_deployment(name, namespace, metrics_server)



Create the specified Seldon Deployment Metrics Server

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
api_instance = seldon_deploy_client.MetricsServerApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
metrics_server = seldon_deploy_client.AlibiDetectorData() # AlibiDetectorData | MetricsServer

try:
    api_response = api_instance.create_metrics_server_seldon_deployment(name, namespace, metrics_server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsServerApi->create_metrics_server_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **metrics_server** | [**AlibiDetectorData**](AlibiDetectorData.md)| MetricsServer | 

### Return type

[**AlibiDetectorData**](AlibiDetectorData.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_metrics_server_seldon_deployment**
> Message delete_metrics_server_seldon_deployment(name, namespace)



Delete the specified Seldon Deployment Metrics Server

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
api_instance = seldon_deploy_client.MetricsServerApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.delete_metrics_server_seldon_deployment(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsServerApi->delete_metrics_server_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**Message**](Message.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_metrics_server_seldon_deployment**
> AlibiDetectorData read_metrics_server_seldon_deployment(name, namespace)



Read the specified Seldon Deployment Metrics Server

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
api_instance = seldon_deploy_client.MetricsServerApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.read_metrics_server_seldon_deployment(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsServerApi->read_metrics_server_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**AlibiDetectorData**](AlibiDetectorData.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

