# seldon_deploy_client.LoggerApi

All URIs are relative to *https://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_logger_data**](LoggerApi.md#create_logger_data) | **POST** /namespaces/{namespace}/logger | 
[**delete_logger_data**](LoggerApi.md#delete_logger_data) | **DELETE** /namespaces/{namespace}/logger | 
[**read_logger_data**](LoggerApi.md#read_logger_data) | **GET** /namespaces/{namespace}/logger | 


# **create_logger_data**
> Message create_logger_data(namespace, logger_data=logger_data)



Create logger data for the specified Namespace

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
api_instance = seldon_deploy_client.LoggerApi(seldon_deploy_client.ApiClient(configuration))
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
logger_data = seldon_deploy_client.LoggerDataType() # LoggerDataType | Logger Data (optional)

try:
    api_response = api_instance.create_logger_data(namespace, logger_data=logger_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoggerApi->create_logger_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **logger_data** | [**LoggerDataType**](LoggerDataType.md)| Logger Data | [optional] 

### Return type

[**Message**](Message.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_logger_data**
> Message delete_logger_data(namespace)



Delete logger data for the specified Namespace

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
api_instance = seldon_deploy_client.LoggerApi(seldon_deploy_client.ApiClient(configuration))
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.delete_logger_data(namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoggerApi->delete_logger_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**Message**](Message.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_logger_data**
> LoggerDataType read_logger_data(namespace)



Read logger data for the specified Namespace

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
api_instance = seldon_deploy_client.LoggerApi(seldon_deploy_client.ApiClient(configuration))
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.read_logger_data(namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoggerApi->read_logger_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**LoggerDataType**](LoggerDataType.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

