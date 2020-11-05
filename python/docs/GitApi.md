# seldon_deploy_client.GitApi

All URIs are relative to *https://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inference_service_git_restore**](GitApi.md#inference_service_git_restore) | **GET** /namespaces/{namespace}/inferenceservices/{name}/gitrestore | 
[**inference_service_git_revert**](GitApi.md#inference_service_git_revert) | **GET** /namespaces/{namespace}/inferenceservices/{name}/gitrevert | 
[**read_inference_service_git_diff**](GitApi.md#read_inference_service_git_diff) | **GET** /namespaces/{namespace}/inferenceservices/{name}/gitdiff | 
[**read_inference_service_git_logs**](GitApi.md#read_inference_service_git_logs) | **GET** /namespaces/{namespace}/inferenceservices/{name}/gitlogs | 
[**read_seldon_deployment_git_diff**](GitApi.md#read_seldon_deployment_git_diff) | **GET** /namespaces/{namespace}/seldondeployments/{name}/gitdiff | 
[**read_seldon_deployment_git_logs**](GitApi.md#read_seldon_deployment_git_logs) | **GET** /namespaces/{namespace}/seldondeployments/{name}/gitlogs | 
[**seldon_deployment_git_restore**](GitApi.md#seldon_deployment_git_restore) | **GET** /namespaces/{namespace}/seldondeployments/{name}/gitrestore | 
[**seldon_deployment_git_revert**](GitApi.md#seldon_deployment_git_revert) | **GET** /namespaces/{namespace}/seldondeployments/{name}/gitrevert | 


# **inference_service_git_restore**
> Message inference_service_git_restore(name, namespace, hash=hash, message=message)



Restore the git commit

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
api_instance = seldon_deploy_client.GitApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
hash = 'hash_example' # str | Hash (optional)
message = 'message_example' # str | Message (optional)

try:
    api_response = api_instance.inference_service_git_restore(name, namespace, hash=hash, message=message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitApi->inference_service_git_restore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **hash** | **str**| Hash | [optional] 
 **message** | **str**| Message | [optional] 

### Return type

[**Message**](Message.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inference_service_git_revert**
> Message inference_service_git_revert(name, namespace, hash=hash, message=message)



Revert the git commit

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
api_instance = seldon_deploy_client.GitApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
hash = 'hash_example' # str | Hash (optional)
message = 'message_example' # str | Message (optional)

try:
    api_response = api_instance.inference_service_git_revert(name, namespace, hash=hash, message=message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitApi->inference_service_git_revert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **hash** | **str**| Hash | [optional] 
 **message** | **str**| Message | [optional] 

### Return type

[**Message**](Message.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_inference_service_git_diff**
> FileDiff read_inference_service_git_diff(name, namespace, hash=hash)



Read the git diff

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
api_instance = seldon_deploy_client.GitApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
hash = 'hash_example' # str | Hash (optional)

try:
    api_response = api_instance.read_inference_service_git_diff(name, namespace, hash=hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitApi->read_inference_service_git_diff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **hash** | **str**| Hash | [optional] 

### Return type

[**FileDiff**](FileDiff.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_inference_service_git_logs**
> list[GitCommit] read_inference_service_git_logs(name, namespace)



Read the git commits

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
api_instance = seldon_deploy_client.GitApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.read_inference_service_git_logs(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitApi->read_inference_service_git_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**list[GitCommit]**](GitCommit.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_seldon_deployment_git_diff**
> FileDiff read_seldon_deployment_git_diff(name, namespace, hash=hash)



Read the git diff

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
api_instance = seldon_deploy_client.GitApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
hash = 'hash_example' # str | Hash (optional)

try:
    api_response = api_instance.read_seldon_deployment_git_diff(name, namespace, hash=hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitApi->read_seldon_deployment_git_diff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **hash** | **str**| Hash | [optional] 

### Return type

[**FileDiff**](FileDiff.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_seldon_deployment_git_logs**
> list[GitCommit] read_seldon_deployment_git_logs(name, namespace)



Read the git commits

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
api_instance = seldon_deploy_client.GitApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.read_seldon_deployment_git_logs(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitApi->read_seldon_deployment_git_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**list[GitCommit]**](GitCommit.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **seldon_deployment_git_restore**
> Message seldon_deployment_git_restore(name, namespace, hash=hash, message=message)



Restore the git commit

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
api_instance = seldon_deploy_client.GitApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
hash = 'hash_example' # str | Hash (optional)
message = 'message_example' # str | Message (optional)

try:
    api_response = api_instance.seldon_deployment_git_restore(name, namespace, hash=hash, message=message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitApi->seldon_deployment_git_restore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **hash** | **str**| Hash | [optional] 
 **message** | **str**| Message | [optional] 

### Return type

[**Message**](Message.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **seldon_deployment_git_revert**
> Message seldon_deployment_git_revert(name, namespace, hash=hash, message=message)



Revert the git commit

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
api_instance = seldon_deploy_client.GitApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
hash = 'hash_example' # str | Hash (optional)
message = 'message_example' # str | Message (optional)

try:
    api_response = api_instance.seldon_deployment_git_revert(name, namespace, hash=hash, message=message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitApi->seldon_deployment_git_revert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **hash** | **str**| Hash | [optional] 
 **message** | **str**| Message | [optional] 

### Return type

[**Message**](Message.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

