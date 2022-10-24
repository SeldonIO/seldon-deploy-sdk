# seldon_deploy_sdk.PredictApi

All URIs are relative to *http://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**predict_file_seldon_deployment**](PredictApi.md#predict_file_seldon_deployment) | **POST** /namespaces/{namespace}/seldondeployments/{name}/predictfile | 
[**predict_file_seldon_pipeline**](PredictApi.md#predict_file_seldon_pipeline) | **POST** /namespaces/{namespace}/pipelines/{name}/predictfile | 
[**predict_seldon_deployment**](PredictApi.md#predict_seldon_deployment) | **POST** /namespaces/{namespace}/seldondeployments/{name}/predict | 
[**read_predict_curl_seldon_deployment**](PredictApi.md#read_predict_curl_seldon_deployment) | **PUT** /namespaces/{namespace}/seldondeployments/{name}/predictcurl | 
[**read_predict_curl_seldon_pipeline**](PredictApi.md#read_predict_curl_seldon_pipeline) | **PUT** /namespaces/{namespace}/pipelines/{name}/predictcurl | 


# **predict_file_seldon_deployment**
> object predict_file_seldon_deployment(name, namespace, predict_file)



Create Seldon Deployment prediction

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
api_instance = seldon_deploy_sdk.PredictApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
predict_file = '/path/to/file.txt' # file | PredictionFile

try:
    api_response = api_instance.predict_file_seldon_deployment(name, namespace, predict_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PredictApi->predict_file_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **predict_file** | **file**| PredictionFile | 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **predict_file_seldon_pipeline**
> object predict_file_seldon_pipeline(name, namespace, predict_file)



Create Seldon Pipeline prediction

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
api_instance = seldon_deploy_sdk.PredictApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
predict_file = '/path/to/file.txt' # file | PredictionFile

try:
    api_response = api_instance.predict_file_seldon_pipeline(name, namespace, predict_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PredictApi->predict_file_seldon_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **predict_file** | **file**| PredictionFile | 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **predict_seldon_deployment**
> object predict_seldon_deployment(name, namespace, prediction)



Create Seldon Deployment prediction

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
api_instance = seldon_deploy_sdk.PredictApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
prediction = NULL # object | Prediction

try:
    api_response = api_instance.predict_seldon_deployment(name, namespace, prediction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PredictApi->predict_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **prediction** | **object**| Prediction | 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_predict_curl_seldon_deployment**
> object read_predict_curl_seldon_deployment(name, namespace, prediction)



Read the specified Seldon Deployment predict curl

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
api_instance = seldon_deploy_sdk.PredictApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
prediction = NULL # object | Prediction

try:
    api_response = api_instance.read_predict_curl_seldon_deployment(name, namespace, prediction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PredictApi->read_predict_curl_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **prediction** | **object**| Prediction | 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_predict_curl_seldon_pipeline**
> object read_predict_curl_seldon_pipeline(name, namespace, prediction)



Read the specified Seldon Pipeline predict curl

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
api_instance = seldon_deploy_sdk.PredictApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
prediction = NULL # object | Prediction

try:
    api_response = api_instance.read_predict_curl_seldon_pipeline(name, namespace, prediction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PredictApi->read_predict_curl_seldon_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **prediction** | **object**| Prediction | 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

