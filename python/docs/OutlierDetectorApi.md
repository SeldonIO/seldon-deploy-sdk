# seldon_deploy_sdk.OutlierDetectorApi

All URIs are relative to *http://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_outlier_detector_seldon_deployment**](OutlierDetectorApi.md#create_outlier_detector_seldon_deployment) | **POST** /namespaces/{namespace}/seldondeployments/{name}/monitor/outlier-detector | 
[**create_outlier_detector_seldon_pipeline**](OutlierDetectorApi.md#create_outlier_detector_seldon_pipeline) | **POST** /namespaces/{namespace}/pipelines/{name}/monitor/outlier-detector | 
[**delete_outlier_detector_seldon_deployment**](OutlierDetectorApi.md#delete_outlier_detector_seldon_deployment) | **DELETE** /namespaces/{namespace}/seldondeployments/{name}/monitor/outlier-detector/{detectorName} | 
[**delete_outlier_detector_seldon_pipeline**](OutlierDetectorApi.md#delete_outlier_detector_seldon_pipeline) | **DELETE** /namespaces/{namespace}/pipelines/{name}/monitor/outlier-detector/{detectorName} | 
[**list_outlier_detector_seldon_deployment**](OutlierDetectorApi.md#list_outlier_detector_seldon_deployment) | **GET** /namespaces/{namespace}/seldondeployments/{name}/monitor/outlier-detector | 
[**list_outlier_detector_seldon_pipeline**](OutlierDetectorApi.md#list_outlier_detector_seldon_pipeline) | **GET** /namespaces/{namespace}/pipelines/{name}/monitor/outlier-detector | 
[**read_outlier_detector_seldon_deployment**](OutlierDetectorApi.md#read_outlier_detector_seldon_deployment) | **GET** /namespaces/{namespace}/seldondeployments/{name}/monitor/outlier-detector/{detectorName} | 
[**read_outlier_detector_seldon_pipeline**](OutlierDetectorApi.md#read_outlier_detector_seldon_pipeline) | **GET** /namespaces/{namespace}/pipelines/{name}/monitor/outlier-detector/{detectorName} | 


# **create_outlier_detector_seldon_deployment**
> DetectorData create_outlier_detector_seldon_deployment(name, namespace, detector_data)



Create the specified Seldon Deployment Outlier Detector

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
api_instance = seldon_deploy_sdk.OutlierDetectorApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
detector_data = seldon_deploy_sdk.DetectorConfigData() # DetectorConfigData | Deployment Detector Data

try:
    api_response = api_instance.create_outlier_detector_seldon_deployment(name, namespace, detector_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutlierDetectorApi->create_outlier_detector_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **detector_data** | [**DetectorConfigData**](DetectorConfigData.md)| Deployment Detector Data | 

### Return type

[**DetectorData**](DetectorData.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_outlier_detector_seldon_pipeline**
> DetectorData create_outlier_detector_seldon_pipeline(name, namespace, detector_data)



Create the specified Seldon Pipeline Outlier Detector

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
api_instance = seldon_deploy_sdk.OutlierDetectorApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
detector_data = seldon_deploy_sdk.DetectorConfigData() # DetectorConfigData | Deployment Detector Data

try:
    api_response = api_instance.create_outlier_detector_seldon_pipeline(name, namespace, detector_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutlierDetectorApi->create_outlier_detector_seldon_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **detector_data** | [**DetectorConfigData**](DetectorConfigData.md)| Deployment Detector Data | 

### Return type

[**DetectorData**](DetectorData.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_outlier_detector_seldon_deployment**
> Message delete_outlier_detector_seldon_deployment(name, namespace, detector_name)



Read the specified Seldon Deployment Outlier Detector

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
api_instance = seldon_deploy_sdk.OutlierDetectorApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
detector_name = 'detector_name_example' # str | Detector Name

try:
    api_response = api_instance.delete_outlier_detector_seldon_deployment(name, namespace, detector_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutlierDetectorApi->delete_outlier_detector_seldon_deployment: %s\n" % e)
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

# **delete_outlier_detector_seldon_pipeline**
> Message delete_outlier_detector_seldon_pipeline(name, namespace, detector_name)



Read the specified Seldon Pipeline Outlier Detector

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
api_instance = seldon_deploy_sdk.OutlierDetectorApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
detector_name = 'detector_name_example' # str | Detector Name

try:
    api_response = api_instance.delete_outlier_detector_seldon_pipeline(name, namespace, detector_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutlierDetectorApi->delete_outlier_detector_seldon_pipeline: %s\n" % e)
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

# **list_outlier_detector_seldon_deployment**
> list[DetectorData] list_outlier_detector_seldon_deployment(name, namespace)



Read the specified Seldon Deployment Outlier Detector

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
api_instance = seldon_deploy_sdk.OutlierDetectorApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.list_outlier_detector_seldon_deployment(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutlierDetectorApi->list_outlier_detector_seldon_deployment: %s\n" % e)
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

# **list_outlier_detector_seldon_pipeline**
> list[DetectorData] list_outlier_detector_seldon_pipeline(name, namespace)



List the specified Seldon Pipeline Outlier Detector

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
api_instance = seldon_deploy_sdk.OutlierDetectorApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.list_outlier_detector_seldon_pipeline(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutlierDetectorApi->list_outlier_detector_seldon_pipeline: %s\n" % e)
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

# **read_outlier_detector_seldon_deployment**
> DetectorData read_outlier_detector_seldon_deployment(name, namespace, detector_name)



Read the specified Seldon Deployment Outlier Detector

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
api_instance = seldon_deploy_sdk.OutlierDetectorApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
detector_name = 'detector_name_example' # str | Detector Name

try:
    api_response = api_instance.read_outlier_detector_seldon_deployment(name, namespace, detector_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutlierDetectorApi->read_outlier_detector_seldon_deployment: %s\n" % e)
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

# **read_outlier_detector_seldon_pipeline**
> DetectorData read_outlier_detector_seldon_pipeline(name, namespace, detector_name)



Read the specified Seldon Pipeline Outlier Detector

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
api_instance = seldon_deploy_sdk.OutlierDetectorApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
detector_name = 'detector_name_example' # str | Detector Name

try:
    api_response = api_instance.read_outlier_detector_seldon_pipeline(name, namespace, detector_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutlierDetectorApi->read_outlier_detector_seldon_pipeline: %s\n" % e)
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

