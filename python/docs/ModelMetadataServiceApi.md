# seldon_deploy_sdk.ModelMetadataServiceApi

All URIs are relative to *http://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**model_metadata_service_create_model_metadata**](ModelMetadataServiceApi.md#model_metadata_service_create_model_metadata) | **POST** /model/metadata | Create a Model Metadata entry.
[**model_metadata_service_delete_model_metadata**](ModelMetadataServiceApi.md#model_metadata_service_delete_model_metadata) | **DELETE** /model/metadata | Delete a Model Metadata entry.
[**model_metadata_service_list_model_metadata**](ModelMetadataServiceApi.md#model_metadata_service_list_model_metadata) | **GET** /model/metadata | List Model Metadata entries.
[**model_metadata_service_list_runtime_metadata_for_model**](ModelMetadataServiceApi.md#model_metadata_service_list_runtime_metadata_for_model) | **GET** /model/metadata/runtime | List Runtime Metadata for all deployments associated with a model.
[**model_metadata_service_update_model_metadata**](ModelMetadataServiceApi.md#model_metadata_service_update_model_metadata) | **PUT** /model/metadata | Update a Model Metadata entry.


# **model_metadata_service_create_model_metadata**
> V1ModelMetadataCreateResponse model_metadata_service_create_model_metadata(body)

Create a Model Metadata entry.

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
api_instance = seldon_deploy_sdk.ModelMetadataServiceApi(seldon_deploy_sdk.ApiClient(configuration))
body = seldon_deploy_sdk.V1Model() # V1Model | 

try:
    # Create a Model Metadata entry.
    api_response = api_instance.model_metadata_service_create_model_metadata(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelMetadataServiceApi->model_metadata_service_create_model_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Model**](V1Model.md)|  | 

### Return type

[**V1ModelMetadataCreateResponse**](V1ModelMetadataCreateResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_metadata_service_delete_model_metadata**
> V1ModelMetadataDeleteResponse model_metadata_service_delete_model_metadata(uri, project=project)

Delete a Model Metadata entry.

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
api_instance = seldon_deploy_sdk.ModelMetadataServiceApi(seldon_deploy_sdk.ApiClient(configuration))
uri = 'uri_example' # str | The URI for the storage bucket containing the model, or the URI to the docker image for custom models. It must be a valid URI as defined in RFC 3986, and must not exceed 200 characters.
project = 'project_example' # str | The project that this model belongs to. (optional)

try:
    # Delete a Model Metadata entry.
    api_response = api_instance.model_metadata_service_delete_model_metadata(uri, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelMetadataServiceApi->model_metadata_service_delete_model_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| The URI for the storage bucket containing the model, or the URI to the docker image for custom models. It must be a valid URI as defined in RFC 3986, and must not exceed 200 characters. | 
 **project** | **str**| The project that this model belongs to. | [optional] 

### Return type

[**V1ModelMetadataDeleteResponse**](V1ModelMetadataDeleteResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_metadata_service_list_model_metadata**
> V1ModelMetadataListResponse model_metadata_service_list_model_metadata(uri=uri, name=name, version=version, artifact_type=artifact_type, task_type=task_type, model_type=model_type, query=query, page_size=page_size, page_token=page_token, list_mask=list_mask, project=project, order_by=order_by)

List Model Metadata entries.

List takes several parameters that are present in the Model Metadata and tries to list all metadata entries that match all supplied fields. To filter by `tags` or `metrics` you can use a map as a query parameter. For example: `?tags[key]=value`.

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
api_instance = seldon_deploy_sdk.ModelMetadataServiceApi(seldon_deploy_sdk.ApiClient(configuration))
uri = 'uri_example' # str |  (optional)
name = 'name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
artifact_type = 'UNKNOWN' # str |  (optional) (default to UNKNOWN)
task_type = 'task_type_example' # str |  (optional)
model_type = 'model_type_example' # str |  (optional)
query = 'query_example' # str | For more complex queries where other logical operators like OR, NOT, etc. (optional)
page_size = 56 # int | Optional. The maximum number of Folders to return in the response. (optional)
page_token = 'page_token_example' # str | Optional. A pagination token returned from a previous call to `List` that indicates where this listing should continue from. (optional)
list_mask = 'list_mask_example' # str | Optional. Can be used to specify which fields of Model you wish to return in the response. If left empty all fields will be returned. (optional)
project = 'project_example' # str |  (optional)
order_by = 'order_by_example' # str | The order in which to return the model metadata. The string value should follow SQL syntax: comma separated list of fields. The default sorting order is ascending. To specify descending order for a field, a suffix \" desc\" should be appended to the field name. Valid field names include: uri, name, version, project, artifact_type, task_type. (optional)

try:
    # List Model Metadata entries.
    api_response = api_instance.model_metadata_service_list_model_metadata(uri=uri, name=name, version=version, artifact_type=artifact_type, task_type=task_type, model_type=model_type, query=query, page_size=page_size, page_token=page_token, list_mask=list_mask, project=project, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelMetadataServiceApi->model_metadata_service_list_model_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **artifact_type** | **str**|  | [optional] [default to UNKNOWN]
 **task_type** | **str**|  | [optional] 
 **model_type** | **str**|  | [optional] 
 **query** | **str**| For more complex queries where other logical operators like OR, NOT, etc. | [optional] 
 **page_size** | **int**| Optional. The maximum number of Folders to return in the response. | [optional] 
 **page_token** | **str**| Optional. A pagination token returned from a previous call to &#x60;List&#x60; that indicates where this listing should continue from. | [optional] 
 **list_mask** | **str**| Optional. Can be used to specify which fields of Model you wish to return in the response. If left empty all fields will be returned. | [optional] 
 **project** | **str**|  | [optional] 
 **order_by** | **str**| The order in which to return the model metadata. The string value should follow SQL syntax: comma separated list of fields. The default sorting order is ascending. To specify descending order for a field, a suffix \&quot; desc\&quot; should be appended to the field name. Valid field names include: uri, name, version, project, artifact_type, task_type. | [optional] 

### Return type

[**V1ModelMetadataListResponse**](V1ModelMetadataListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_metadata_service_list_runtime_metadata_for_model**
> V1RuntimeMetadataListResponse model_metadata_service_list_runtime_metadata_for_model(model_uri=model_uri, deployment_uid=deployment_uid, deployment_name=deployment_name, deployment_namespace=deployment_namespace, deployment_status=deployment_status, predictor_name=predictor_name, node_name=node_name, page_size=page_size, page_token=page_token, list_mask=list_mask, deployment_type=deployment_type)

List Runtime Metadata for all deployments associated with a model.

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
api_instance = seldon_deploy_sdk.ModelMetadataServiceApi(seldon_deploy_sdk.ApiClient(configuration))
model_uri = 'model_uri_example' # str |  (optional)
deployment_uid = 'deployment_uid_example' # str |  (optional)
deployment_name = 'deployment_name_example' # str |  (optional)
deployment_namespace = 'deployment_namespace_example' # str |  (optional)
deployment_status = 'Running' # str |  (optional) (default to Running)
predictor_name = 'predictor_name_example' # str |  (optional)
node_name = 'node_name_example' # str |  (optional)
page_size = 56 # int | Optional. The maximum number of Folders to return in the response. (optional)
page_token = 'page_token_example' # str | Optional. A pagination token returned from a previous call to `List` that indicates where this listing should continue from. (optional)
list_mask = 'list_mask_example' # str | Optional. Can be used to specify which fields of RuntimeMetadata you wish to return in the response. If left empty all fields will be returned. (optional)
deployment_type = 'UndefinedDeploymentType' # str |  (optional) (default to UndefinedDeploymentType)

try:
    # List Runtime Metadata for all deployments associated with a model.
    api_response = api_instance.model_metadata_service_list_runtime_metadata_for_model(model_uri=model_uri, deployment_uid=deployment_uid, deployment_name=deployment_name, deployment_namespace=deployment_namespace, deployment_status=deployment_status, predictor_name=predictor_name, node_name=node_name, page_size=page_size, page_token=page_token, list_mask=list_mask, deployment_type=deployment_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelMetadataServiceApi->model_metadata_service_list_runtime_metadata_for_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_uri** | **str**|  | [optional] 
 **deployment_uid** | **str**|  | [optional] 
 **deployment_name** | **str**|  | [optional] 
 **deployment_namespace** | **str**|  | [optional] 
 **deployment_status** | **str**|  | [optional] [default to Running]
 **predictor_name** | **str**|  | [optional] 
 **node_name** | **str**|  | [optional] 
 **page_size** | **int**| Optional. The maximum number of Folders to return in the response. | [optional] 
 **page_token** | **str**| Optional. A pagination token returned from a previous call to &#x60;List&#x60; that indicates where this listing should continue from. | [optional] 
 **list_mask** | **str**| Optional. Can be used to specify which fields of RuntimeMetadata you wish to return in the response. If left empty all fields will be returned. | [optional] 
 **deployment_type** | **str**|  | [optional] [default to UndefinedDeploymentType]

### Return type

[**V1RuntimeMetadataListResponse**](V1RuntimeMetadataListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_metadata_service_update_model_metadata**
> V1ModelMetadataUpdateResponse model_metadata_service_update_model_metadata(body)

Update a Model Metadata entry.

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
api_instance = seldon_deploy_sdk.ModelMetadataServiceApi(seldon_deploy_sdk.ApiClient(configuration))
body = seldon_deploy_sdk.V1Model() # V1Model | 

try:
    # Update a Model Metadata entry.
    api_response = api_instance.model_metadata_service_update_model_metadata(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelMetadataServiceApi->model_metadata_service_update_model_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Model**](V1Model.md)|  | 

### Return type

[**V1ModelMetadataUpdateResponse**](V1ModelMetadataUpdateResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

