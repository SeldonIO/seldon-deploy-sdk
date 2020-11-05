# seldon_deploy_client.LoadtestApi

All URIs are relative to *https://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loadtest_inference_service**](LoadtestApi.md#loadtest_inference_service) | **POST** /namespaces/{namespace}/inferenceservices/{name}/loadtest | 
[**loadtest_seldon_deployment**](LoadtestApi.md#loadtest_seldon_deployment) | **POST** /namespaces/{namespace}/seldondeployments/{name}/loadtest | 


# **loadtest_inference_service**
> Message loadtest_inference_service(namespace, name, load_file, connections_number=connections_number, requests_number=requests_number, duration=duration)



Create Inference Service load test

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
api_instance = seldon_deploy_client.LoadtestApi(seldon_deploy_client.ApiClient(configuration))
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
name = 'name_example' # str | Name identifies a resource
load_file = '/path/to/file.txt' # file | Prediction contains predict payload
connections_number = 'connections_number_example' # str | Connections Number provides number of allowed connections (optional)
requests_number = 'requests_number_example' # str | Requests Number provides number of allowed requests (optional)
duration = 'duration_example' # str | Duration of load test in seconds (optional)

try:
    api_response = api_instance.loadtest_inference_service(namespace, name, load_file, connections_number=connections_number, requests_number=requests_number, duration=duration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoadtestApi->loadtest_inference_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **name** | **str**| Name identifies a resource | 
 **load_file** | **file**| Prediction contains predict payload | 
 **connections_number** | **str**| Connections Number provides number of allowed connections | [optional] 
 **requests_number** | **str**| Requests Number provides number of allowed requests | [optional] 
 **duration** | **str**| Duration of load test in seconds | [optional] 

### Return type

[**Message**](Message.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loadtest_seldon_deployment**
> Message loadtest_seldon_deployment(namespace, name, load_file, connections_number=connections_number, requests_number=requests_number, duration=duration)



Create Seldon Deployment load test

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
api_instance = seldon_deploy_client.LoadtestApi(seldon_deploy_client.ApiClient(configuration))
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
name = 'name_example' # str | Name identifies a resource
load_file = '/path/to/file.txt' # file | Prediction contains predict payload
connections_number = 'connections_number_example' # str | Connections Number provides number of allowed connections (optional)
requests_number = 'requests_number_example' # str | Requests Number provides number of allowed requests (optional)
duration = 'duration_example' # str | Duration of load test in seconds (optional)

try:
    api_response = api_instance.loadtest_seldon_deployment(namespace, name, load_file, connections_number=connections_number, requests_number=requests_number, duration=duration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoadtestApi->loadtest_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **name** | **str**| Name identifies a resource | 
 **load_file** | **file**| Prediction contains predict payload | 
 **connections_number** | **str**| Connections Number provides number of allowed connections | [optional] 
 **requests_number** | **str**| Requests Number provides number of allowed requests | [optional] 
 **duration** | **str**| Duration of load test in seconds | [optional] 

### Return type

[**Message**](Message.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

