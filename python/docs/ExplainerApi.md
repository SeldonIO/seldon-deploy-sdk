# seldon_deploy_client.ExplainerApi

All URIs are relative to *https://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**explain_inference_service**](ExplainerApi.md#explain_inference_service) | **POST** /namespaces/{namespace}/inferenceservices/{name}/explain | 
[**explain_seldon_deployment**](ExplainerApi.md#explain_seldon_deployment) | **POST** /namespaces/{namespace}/seldondeployments/{name}/explain | 


# **explain_inference_service**
> object explain_inference_service(namespace, name, explaindata=explaindata)



Create Inference Service explanation

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
api_instance = seldon_deploy_client.ExplainerApi(seldon_deploy_client.ApiClient(configuration))
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
name = 'name_example' # str | Name identifies a resource
explaindata = NULL # object | Prediction contains predict payload (optional)

try:
    api_response = api_instance.explain_inference_service(namespace, name, explaindata=explaindata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExplainerApi->explain_inference_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **name** | **str**| Name identifies a resource | 
 **explaindata** | **object**| Prediction contains predict payload | [optional] 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **explain_seldon_deployment**
> object explain_seldon_deployment(namespace, name, explaindata=explaindata)



Create Seldon Deployment explanation

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
api_instance = seldon_deploy_client.ExplainerApi(seldon_deploy_client.ApiClient(configuration))
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
name = 'name_example' # str | Name identifies a resource
explaindata = NULL # object | Prediction contains predict payload (optional)

try:
    api_response = api_instance.explain_seldon_deployment(namespace, name, explaindata=explaindata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExplainerApi->explain_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **name** | **str**| Name identifies a resource | 
 **explaindata** | **object**| Prediction contains predict payload | [optional] 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

