# seldon_deploy_sdk.MetricsServerApi

All URIs are relative to *https://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_metrics_server_seldon_deployment**](MetricsServerApi.md#create_metrics_server_seldon_deployment) | **POST** /namespaces/{namespace}/seldondeployments/{name}/metrics-server | 
[**delete_metrics_server_seldon_deployment**](MetricsServerApi.md#delete_metrics_server_seldon_deployment) | **DELETE** /namespaces/{namespace}/seldondeployments/{name}/monitor/metrics-server/{detector-name} | 
[**list_metrics_server_seldon_deployment**](MetricsServerApi.md#list_metrics_server_seldon_deployment) | **GET** /namespaces/{namespace}/seldondeployments/{name}/monitor/metrics-server | 
[**read_metrics_server_seldon_deployment**](MetricsServerApi.md#read_metrics_server_seldon_deployment) | **GET** /namespaces/{namespace}/seldondeployments/{name}/monitor/metrics-server/{detector-name} | 


# **create_metrics_server_seldon_deployment**
> DetectorData create_metrics_server_seldon_deployment(name, namespace)



Create the specified Seldon Deployment Metrics Server

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
api_instance = seldon_deploy_sdk.MetricsServerApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.create_metrics_server_seldon_deployment(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsServerApi->create_metrics_server_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**DetectorData**](DetectorData.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_metrics_server_seldon_deployment**
> Message delete_metrics_server_seldon_deployment(name, namespace, detector_name)



Read the specified Seldon Deployment Metrics Server

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
api_instance = seldon_deploy_sdk.MetricsServerApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
detector_name = 'detector_name_example' # str | Detector Name

try:
    api_response = api_instance.delete_metrics_server_seldon_deployment(name, namespace, detector_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsServerApi->delete_metrics_server_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **detector_name** | **str**| Detector Name | 

### Return type

[**Message**](Message.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_metrics_server_seldon_deployment**
> list[DetectorData] list_metrics_server_seldon_deployment(name, namespace)



Read the specified Seldon Deployment Metrics Server

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
api_instance = seldon_deploy_sdk.MetricsServerApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.list_metrics_server_seldon_deployment(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsServerApi->list_metrics_server_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**list[DetectorData]**](DetectorData.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_metrics_server_seldon_deployment**
> DetectorData read_metrics_server_seldon_deployment(name, namespace, detector_name)



Read the specified Seldon Deployment Metrics Server

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
api_instance = seldon_deploy_sdk.MetricsServerApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
detector_name = 'detector_name_example' # str | Detector Name

try:
    api_response = api_instance.read_metrics_server_seldon_deployment(name, namespace, detector_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsServerApi->read_metrics_server_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **detector_name** | **str**| Detector Name | 

### Return type

[**DetectorData**](DetectorData.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

