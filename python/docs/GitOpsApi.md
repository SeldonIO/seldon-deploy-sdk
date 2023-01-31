# seldon_deploy_sdk.GitOpsApi

All URIs are relative to *http://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_experiment_git_diff**](GitOpsApi.md#read_experiment_git_diff) | **GET** /namespaces/{namespace}/experiments/{name}/gitdiff | 
[**read_experiment_git_logs**](GitOpsApi.md#read_experiment_git_logs) | **GET** /namespaces/{namespace}/experiments/{name}/gitlogs | 
[**read_git_ops_status**](GitOpsApi.md#read_git_ops_status) | **GET** /namespaces/{namespace}/gitops-status | 
[**read_model_git_diff**](GitOpsApi.md#read_model_git_diff) | **GET** /namespaces/{namespace}/models/{name}/gitdiff | 
[**read_model_git_logs**](GitOpsApi.md#read_model_git_logs) | **GET** /namespaces/{namespace}/models/{name}/gitlogs | 
[**read_pipeline_git_diff**](GitOpsApi.md#read_pipeline_git_diff) | **GET** /namespaces/{namespace}/pipelines/{name}/gitdiff | 
[**read_pipeline_git_logs**](GitOpsApi.md#read_pipeline_git_logs) | **GET** /namespaces/{namespace}/pipelines/{name}/gitlogs | 
[**read_seldon_deployment_git_diff**](GitOpsApi.md#read_seldon_deployment_git_diff) | **GET** /namespaces/{namespace}/seldondeployments/{name}/gitdiff | 
[**read_seldon_deployment_git_logs**](GitOpsApi.md#read_seldon_deployment_git_logs) | **GET** /namespaces/{namespace}/seldondeployments/{name}/gitlogs | 
[**seldon_deployment_git_restore**](GitOpsApi.md#seldon_deployment_git_restore) | **GET** /namespaces/{namespace}/seldondeployments/{name}/gitrestore | 
[**seldon_deployment_git_revert**](GitOpsApi.md#seldon_deployment_git_revert) | **GET** /namespaces/{namespace}/seldondeployments/{name}/gitrevert | 


# **read_experiment_git_diff**
> FileDiff read_experiment_git_diff(name, namespace, hash=hash)



Read the git diff for an experiment

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
api_instance = seldon_deploy_sdk.GitOpsApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
hash = 'hash_example' # str | Hash (optional)

try:
    api_response = api_instance.read_experiment_git_diff(name, namespace, hash=hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitOpsApi->read_experiment_git_diff: %s\n" % e)
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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_experiment_git_logs**
> list[AuditLog] read_experiment_git_logs(name, namespace)



Read the git commits for an experiment

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
api_instance = seldon_deploy_sdk.GitOpsApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.read_experiment_git_logs(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitOpsApi->read_experiment_git_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**list[AuditLog]**](AuditLog.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_git_ops_status**
> object read_git_ops_status(namespace)



Read the GitOps status

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
api_instance = seldon_deploy_sdk.GitOpsApi(seldon_deploy_sdk.ApiClient(configuration))
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.read_git_ops_status(namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitOpsApi->read_git_ops_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_model_git_diff**
> FileDiff read_model_git_diff(name, namespace, hash=hash)



Read the git diff for a model

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
api_instance = seldon_deploy_sdk.GitOpsApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
hash = 'hash_example' # str | Hash (optional)

try:
    api_response = api_instance.read_model_git_diff(name, namespace, hash=hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitOpsApi->read_model_git_diff: %s\n" % e)
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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_model_git_logs**
> list[AuditLog] read_model_git_logs(name, namespace)



Read the git commits for a model

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
api_instance = seldon_deploy_sdk.GitOpsApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.read_model_git_logs(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitOpsApi->read_model_git_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**list[AuditLog]**](AuditLog.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_pipeline_git_diff**
> FileDiff read_pipeline_git_diff(name, namespace, hash=hash)



Read the git diff for a pipeline

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
api_instance = seldon_deploy_sdk.GitOpsApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
hash = 'hash_example' # str | Hash (optional)

try:
    api_response = api_instance.read_pipeline_git_diff(name, namespace, hash=hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitOpsApi->read_pipeline_git_diff: %s\n" % e)
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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_pipeline_git_logs**
> list[AuditLog] read_pipeline_git_logs(name, namespace)



Read the git commits for a pipeline

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
api_instance = seldon_deploy_sdk.GitOpsApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.read_pipeline_git_logs(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitOpsApi->read_pipeline_git_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**list[AuditLog]**](AuditLog.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_seldon_deployment_git_diff**
> FileDiff read_seldon_deployment_git_diff(name, namespace, hash=hash)



Read the git diff for a Seldon deployment

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
api_instance = seldon_deploy_sdk.GitOpsApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
hash = 'hash_example' # str | Hash (optional)

try:
    api_response = api_instance.read_seldon_deployment_git_diff(name, namespace, hash=hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitOpsApi->read_seldon_deployment_git_diff: %s\n" % e)
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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_seldon_deployment_git_logs**
> list[AuditLog] read_seldon_deployment_git_logs(name, namespace)



Read the git commits for a Seldon deployment

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
api_instance = seldon_deploy_sdk.GitOpsApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.read_seldon_deployment_git_logs(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitOpsApi->read_seldon_deployment_git_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**list[AuditLog]**](AuditLog.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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
import seldon_deploy_sdk
from seldon_deploy_sdk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = seldon_deploy_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = seldon_deploy_sdk.GitOpsApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
hash = 'hash_example' # str | Hash (optional)
message = 'message_example' # str | Message (optional)

try:
    api_response = api_instance.seldon_deployment_git_restore(name, namespace, hash=hash, message=message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitOpsApi->seldon_deployment_git_restore: %s\n" % e)
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

[OAuth2](../README.md#OAuth2)

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
import seldon_deploy_sdk
from seldon_deploy_sdk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = seldon_deploy_sdk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = seldon_deploy_sdk.GitOpsApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
hash = 'hash_example' # str | Hash (optional)
message = 'message_example' # str | Message (optional)

try:
    api_response = api_instance.seldon_deployment_git_revert(name, namespace, hash=hash, message=message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitOpsApi->seldon_deployment_git_revert: %s\n" % e)
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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

