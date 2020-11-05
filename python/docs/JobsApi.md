# seldon_deploy_client.JobsApi

All URIs are relative to *https://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_seldon_deployment_batch_job**](JobsApi.md#create_seldon_deployment_batch_job) | **POST** /namespaces/{namespace}/seldondeployments/{name}/batchjobs | 
[**get_deployment_batch_job**](JobsApi.md#get_deployment_batch_job) | **GET** /namespaces/{namespace}/seldondeployments/{name}/batchjobs/{workflowName} | 
[**list_seldon_deployment_batch_jobs**](JobsApi.md#list_seldon_deployment_batch_jobs) | **GET** /namespaces/{namespace}/seldondeployments/{name}/batchjobs | 


# **create_seldon_deployment_batch_job**
> UID create_seldon_deployment_batch_job(name, namespace, workflow)



Create the seldondeployment's batch jobs

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
api_instance = seldon_deploy_client.JobsApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
workflow = seldon_deploy_client.BatchDefinition() # BatchDefinition | WorkflowName

try:
    api_response = api_instance.create_seldon_deployment_batch_job(name, namespace, workflow)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->create_seldon_deployment_batch_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **workflow** | [**BatchDefinition**](BatchDefinition.md)| WorkflowName | 

### Return type

[**UID**](UID.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_batch_job**
> BatchJob get_deployment_batch_job(name, namespace, workflow_name)



Get details on the seldondeployment's batch job

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
api_instance = seldon_deploy_client.JobsApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
workflow_name = 'workflow_name_example' # str | WorkflowName identifies a workflow name

try:
    api_response = api_instance.get_deployment_batch_job(name, namespace, workflow_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->get_deployment_batch_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **workflow_name** | **str**| WorkflowName identifies a workflow name | 

### Return type

[**BatchJob**](BatchJob.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_seldon_deployment_batch_jobs**
> BatchDescriptionList list_seldon_deployment_batch_jobs(name, namespace, limit=limit, page=page)



Read the seldondeployment's batch jobs

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
api_instance = seldon_deploy_client.JobsApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
limit = 'limit_example' # str | Limit (optional)
page = 'page_example' # str | Page (optional)

try:
    api_response = api_instance.list_seldon_deployment_batch_jobs(name, namespace, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->list_seldon_deployment_batch_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **limit** | **str**| Limit | [optional] 
 **page** | **str**| Page | [optional] 

### Return type

[**BatchDescriptionList**](BatchDescriptionList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

