# seldon_deploy_client.DriftDetectorApi

All URIs are relative to *https://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_drift_detector_inference_service**](DriftDetectorApi.md#create_drift_detector_inference_service) | **POST** /namespaces/{namespace}/inferenceservices/{name}/driftdetector | 
[**create_drift_detector_seldon_deployment**](DriftDetectorApi.md#create_drift_detector_seldon_deployment) | **POST** /namespaces/{namespace}/seldondeployments/{name}/driftdetector | 
[**delete_drift_detector_inference_service**](DriftDetectorApi.md#delete_drift_detector_inference_service) | **DELETE** /namespaces/{namespace}/inferenceservice/{name}/driftdetector | 
[**delete_drift_detector_seldon_deployment**](DriftDetectorApi.md#delete_drift_detector_seldon_deployment) | **DELETE** /namespaces/{namespace}/seldondeployments/{name}/driftdetector | 
[**read_drift_detector_inference_service**](DriftDetectorApi.md#read_drift_detector_inference_service) | **GET** /namespaces/{namespace}/inferenceservices/{name}/driftdetector | 
[**read_drift_detector_seldon_deployment**](DriftDetectorApi.md#read_drift_detector_seldon_deployment) | **GET** /namespaces/{namespace}/seldondeployments/{name}/driftdetector | 


# **create_drift_detector_inference_service**
> AlibiDetectorData create_drift_detector_inference_service(name, namespace, drift_detector)



Create the specified Inference Service Drift Detector

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
api_instance = seldon_deploy_client.DriftDetectorApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
drift_detector = seldon_deploy_client.AlibiDetectorData() # AlibiDetectorData | DriftDetector

try:
    api_response = api_instance.create_drift_detector_inference_service(name, namespace, drift_detector)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriftDetectorApi->create_drift_detector_inference_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **drift_detector** | [**AlibiDetectorData**](AlibiDetectorData.md)| DriftDetector | 

### Return type

[**AlibiDetectorData**](AlibiDetectorData.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_drift_detector_seldon_deployment**
> AlibiDetectorData create_drift_detector_seldon_deployment(name, namespace, drift_detector)



Create the specified Seldon Deployment Drift Detector

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
api_instance = seldon_deploy_client.DriftDetectorApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
drift_detector = seldon_deploy_client.AlibiDetectorData() # AlibiDetectorData | DriftDetector

try:
    api_response = api_instance.create_drift_detector_seldon_deployment(name, namespace, drift_detector)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriftDetectorApi->create_drift_detector_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **drift_detector** | [**AlibiDetectorData**](AlibiDetectorData.md)| DriftDetector | 

### Return type

[**AlibiDetectorData**](AlibiDetectorData.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_drift_detector_inference_service**
> Message delete_drift_detector_inference_service(name, namespace)



Delete the specified Inference Service Drift Detector

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
api_instance = seldon_deploy_client.DriftDetectorApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.delete_drift_detector_inference_service(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriftDetectorApi->delete_drift_detector_inference_service: %s\n" % e)
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

# **delete_drift_detector_seldon_deployment**
> Message delete_drift_detector_seldon_deployment(name, namespace)



Delete the specified Seldon Deployment Drift Detector

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
api_instance = seldon_deploy_client.DriftDetectorApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.delete_drift_detector_seldon_deployment(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriftDetectorApi->delete_drift_detector_seldon_deployment: %s\n" % e)
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

# **read_drift_detector_inference_service**
> AlibiDetectorData read_drift_detector_inference_service(name, namespace)



Read the specified Inference Service Drift Detector

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
api_instance = seldon_deploy_client.DriftDetectorApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.read_drift_detector_inference_service(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriftDetectorApi->read_drift_detector_inference_service: %s\n" % e)
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

# **read_drift_detector_seldon_deployment**
> AlibiDetectorData read_drift_detector_seldon_deployment(name, namespace)



Read the specified Seldon Deployment Drift Detector

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
api_instance = seldon_deploy_client.DriftDetectorApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.read_drift_detector_seldon_deployment(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriftDetectorApi->read_drift_detector_seldon_deployment: %s\n" % e)
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

