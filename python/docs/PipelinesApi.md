# seldon_deploy_sdk.PipelinesApi

All URIs are relative to *http://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pipeline**](PipelinesApi.md#create_pipeline) | **POST** /namespaces/{namespace}/pipelines | 
[**create_pipeline_explainer**](PipelinesApi.md#create_pipeline_explainer) | **POST** /namespaces/{namespace}/pipelines/{name}/explainer | 
[**delete_pipeline**](PipelinesApi.md#delete_pipeline) | **DELETE** /namespaces/{namespace}/pipelines/{name} | 
[**delete_pipeline_explainer**](PipelinesApi.md#delete_pipeline_explainer) | **DELETE** /namespaces/{namespace}/pipelines/{name}/explainer | 
[**list_pipeline_models**](PipelinesApi.md#list_pipeline_models) | **GET** /namespaces/{namespace}/pipelines/{name}/models | 
[**list_pipelines**](PipelinesApi.md#list_pipelines) | **GET** /namespaces/{namespace}/pipelines | 
[**read_pipeline**](PipelinesApi.md#read_pipeline) | **GET** /namespaces/{namespace}/pipelines/{name} | 
[**read_pipeline_explainer**](PipelinesApi.md#read_pipeline_explainer) | **GET** /namespaces/{namespace}/pipelines/{name}/explainer | 
[**update_pipeline**](PipelinesApi.md#update_pipeline) | **PUT** /namespaces/{namespace}/pipelines/{name} | 


# **create_pipeline**
> SeldonPipeline create_pipeline(namespace, mldeployment, action=action, message=message)



Create a Seldon Pipeline

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
api_instance = seldon_deploy_sdk.PipelinesApi(seldon_deploy_sdk.ApiClient(configuration))
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
mldeployment = seldon_deploy_sdk.Pipeline() # Pipeline | Seldon Pipeline
action = 'action_example' # str | Action (optional)
message = 'message_example' # str | Message (optional)

try:
    api_response = api_instance.create_pipeline(namespace, mldeployment, action=action, message=message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->create_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **mldeployment** | [**Pipeline**](Pipeline.md)| Seldon Pipeline | 
 **action** | **str**| Action | [optional] 
 **message** | **str**| Message | [optional] 

### Return type

[**SeldonPipeline**](SeldonPipeline.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pipeline_explainer**
> SeldonModel create_pipeline_explainer(name, namespace, model, action=action, message=message)



Read the specified Seldon Pipeline Explainer

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
api_instance = seldon_deploy_sdk.PipelinesApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
model = seldon_deploy_sdk.Model() # Model | Seldon Model
action = 'action_example' # str | Action (optional)
message = 'message_example' # str | Message (optional)

try:
    api_response = api_instance.create_pipeline_explainer(name, namespace, model, action=action, message=message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->create_pipeline_explainer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **model** | [**Model**](Model.md)| Seldon Model | 
 **action** | **str**| Action | [optional] 
 **message** | **str**| Message | [optional] 

### Return type

[**SeldonModel**](SeldonModel.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pipeline**
> object delete_pipeline(name, namespace, action=action, message=message)



Delete the specified Seldon Pipeline

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
api_instance = seldon_deploy_sdk.PipelinesApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
action = 'action_example' # str | Action (optional)
message = 'message_example' # str | Message (optional)

try:
    api_response = api_instance.delete_pipeline(name, namespace, action=action, message=message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->delete_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **action** | **str**| Action | [optional] 
 **message** | **str**| Message | [optional] 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pipeline_explainer**
> object delete_pipeline_explainer(name, namespace, action=action, message=message)



Read the specified Seldon Pipeline Explainer

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
api_instance = seldon_deploy_sdk.PipelinesApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
action = 'action_example' # str | Action (optional)
message = 'message_example' # str | Message (optional)

try:
    api_response = api_instance.delete_pipeline_explainer(name, namespace, action=action, message=message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->delete_pipeline_explainer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **action** | **str**| Action | [optional] 
 **message** | **str**| Message | [optional] 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pipeline_models**
> SeldonModelList list_pipeline_models(name, namespace)



List objects of kind Seldon Models within a Pipeline

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
api_instance = seldon_deploy_sdk.PipelinesApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.list_pipeline_models(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->list_pipeline_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**SeldonModelList**](SeldonModelList.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pipelines**
> SeldonPipelineList list_pipelines(namespace)



list objects of kind Seldon Pipelines

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
api_instance = seldon_deploy_sdk.PipelinesApi(seldon_deploy_sdk.ApiClient(configuration))
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.list_pipelines(namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->list_pipelines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**SeldonPipelineList**](SeldonPipelineList.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_pipeline**
> SeldonPipeline read_pipeline(name, namespace)



Read the specified Seldon Pipeline

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
api_instance = seldon_deploy_sdk.PipelinesApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.read_pipeline(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->read_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**SeldonPipeline**](SeldonPipeline.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_pipeline_explainer**
> SeldonModel read_pipeline_explainer(name, namespace)



Read the specified Seldon Pipeline Explainer

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
api_instance = seldon_deploy_sdk.PipelinesApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.read_pipeline_explainer(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->read_pipeline_explainer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**SeldonModel**](SeldonModel.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pipeline**
> SeldonPipeline update_pipeline(name, namespace, mldeployment, action=action, message=message)



Update the specified Seldon Pipeline

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
api_instance = seldon_deploy_sdk.PipelinesApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
mldeployment = seldon_deploy_sdk.Pipeline() # Pipeline | Seldon Pipeline
action = 'action_example' # str | Action (optional)
message = 'message_example' # str | Message (optional)

try:
    api_response = api_instance.update_pipeline(name, namespace, mldeployment, action=action, message=message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->update_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **mldeployment** | [**Pipeline**](Pipeline.md)| Seldon Pipeline | 
 **action** | **str**| Action | [optional] 
 **message** | **str**| Message | [optional] 

### Return type

[**SeldonPipeline**](SeldonPipeline.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

