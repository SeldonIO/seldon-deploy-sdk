# seldon_deploy_client.ValidateApi

All URIs are relative to *https://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validate_inference_service**](ValidateApi.md#validate_inference_service) | **GET** /namespaces/{namespace}/inferenceservices/validate | 
[**validate_seldon_deployment**](ValidateApi.md#validate_seldon_deployment) | **GET** /namespaces/{namespace}/seldondeployments/validate | 


# **validate_inference_service**
> Message validate_inference_service(namespace, mldeployment)



Validate the given Inference Service

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
api_instance = seldon_deploy_client.ValidateApi(seldon_deploy_client.ApiClient(configuration))
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
mldeployment = seldon_deploy_client.InferenceService() # InferenceService | Inference Service

try:
    api_response = api_instance.validate_inference_service(namespace, mldeployment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValidateApi->validate_inference_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **mldeployment** | [**InferenceService**](InferenceService.md)| Inference Service | 

### Return type

[**Message**](Message.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_seldon_deployment**
> Message validate_seldon_deployment(namespace, mldeployment)



Validate the given Seldon Deployment

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
api_instance = seldon_deploy_client.ValidateApi(seldon_deploy_client.ApiClient(configuration))
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
mldeployment = seldon_deploy_client.SeldonDeployment() # SeldonDeployment | Seldon Deployment

try:
    api_response = api_instance.validate_seldon_deployment(namespace, mldeployment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValidateApi->validate_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **mldeployment** | [**SeldonDeployment**](SeldonDeployment.md)| Seldon Deployment | 

### Return type

[**Message**](Message.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

