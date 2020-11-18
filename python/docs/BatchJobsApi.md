# seldon_deploy_client.BatchJobsApi

All URIs are relative to *https://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_seldon_deployment_batch_job**](BatchJobsApi.md#create_seldon_deployment_batch_job) | **POST** /namespaces/{namespace}/seldondeployments/{name}/batchjobs | 
[**get_deployment_batch_job**](BatchJobsApi.md#get_deployment_batch_job) | **GET** /namespaces/{namespace}/seldondeployments/{name}/batchjobs/{jobName} | 
[**list_seldon_deployment_batch_jobs**](BatchJobsApi.md#list_seldon_deployment_batch_jobs) | **GET** /namespaces/{namespace}/seldondeployments/{name}/batchjobs | 


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

# Configure OAuth2 access token for authorization: OAuth2
configuration = seldon_deploy_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = seldon_deploy_client.BatchJobsApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
workflow = seldon_deploy_client.BatchDefinition() # BatchDefinition | WorkflowName

try:
    api_response = api_instance.create_seldon_deployment_batch_job(name, namespace, workflow)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchJobsApi->create_seldon_deployment_batch_job: %s\n" % e)
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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_batch_job**
> BatchJob get_deployment_batch_job(name, namespace, job_name)



Get details on the seldondeployment's batch job

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_client
from seldon_deploy_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = seldon_deploy_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = seldon_deploy_client.BatchJobsApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
job_name = 'job_name_example' # str | JobName identifies a job name

try:
    api_response = api_instance.get_deployment_batch_job(name, namespace, job_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchJobsApi->get_deployment_batch_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **job_name** | **str**| JobName identifies a job name | 

### Return type

[**BatchJob**](BatchJob.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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

# Configure OAuth2 access token for authorization: OAuth2
configuration = seldon_deploy_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = seldon_deploy_client.BatchJobsApi(seldon_deploy_client.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
limit = 'limit_example' # str | Limit of items returned in one response (optional)
page = 'page_example' # str | Requested page (optional)

try:
    api_response = api_instance.list_seldon_deployment_batch_jobs(name, namespace, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchJobsApi->list_seldon_deployment_batch_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **limit** | **str**| Limit of items returned in one response | [optional] 
 **page** | **str**| Requested page | [optional] 

### Return type

[**BatchDescriptionList**](BatchDescriptionList.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

