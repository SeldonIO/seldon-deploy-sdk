# seldon_deploy_sdk.LoadtestJobsApi

All URIs are relative to *http://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_loadtest_pipeline**](LoadtestJobsApi.md#create_loadtest_pipeline) | **POST** /namespaces/{namespace}/pipelines/{name}/loadtestjobs | 
[**create_loadtest_seldon_deployment**](LoadtestJobsApi.md#create_loadtest_seldon_deployment) | **POST** /namespaces/{namespace}/seldondeployments/{name}/loadtestjobs | 
[**delete_loadtest_pipeline**](LoadtestJobsApi.md#delete_loadtest_pipeline) | **DELETE** /namespaces/{namespace}/pipelines/{name}/loadtestjobs/{jobName} | 
[**delete_loadtest_seldon_deployment**](LoadtestJobsApi.md#delete_loadtest_seldon_deployment) | **DELETE** /namespaces/{namespace}/seldondeployments/{name}/loadtestjobs/{jobName} | 
[**list_loadtest_pipeline**](LoadtestJobsApi.md#list_loadtest_pipeline) | **GET** /namespaces/{namespace}/pipelines/{name}/loadtestjobs | 
[**list_loadtest_seldon_deployment**](LoadtestJobsApi.md#list_loadtest_seldon_deployment) | **GET** /namespaces/{namespace}/seldondeployments/{name}/loadtestjobs | 


# **create_loadtest_pipeline**
> Message create_loadtest_pipeline(name, namespace, load_file, connections_number=connections_number, requests_number=requests_number, duration=duration)



Create Pipeline load test multipart/form-data

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
api_instance = seldon_deploy_sdk.LoadtestJobsApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
load_file = '/path/to/file.txt' # file | Prediction contains predict payload
connections_number = 'connections_number_example' # str | Connections Number provides number of allowed connections (optional)
requests_number = 'requests_number_example' # str | Requests Number provides number of allowed requests (optional)
duration = 'duration_example' # str | Duration of load test in seconds (optional)

try:
    api_response = api_instance.create_loadtest_pipeline(name, namespace, load_file, connections_number=connections_number, requests_number=requests_number, duration=duration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoadtestJobsApi->create_loadtest_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **load_file** | **file**| Prediction contains predict payload | 
 **connections_number** | **str**| Connections Number provides number of allowed connections | [optional] 
 **requests_number** | **str**| Requests Number provides number of allowed requests | [optional] 
 **duration** | **str**| Duration of load test in seconds | [optional] 

### Return type

[**Message**](Message.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_loadtest_seldon_deployment**
> Message create_loadtest_seldon_deployment(name, namespace, load_file, connections_number=connections_number, requests_number=requests_number, duration=duration)



Create Seldon Deployment load test multipart/form-data

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
api_instance = seldon_deploy_sdk.LoadtestJobsApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
load_file = '/path/to/file.txt' # file | Prediction contains predict payload
connections_number = 'connections_number_example' # str | Connections Number provides number of allowed connections (optional)
requests_number = 'requests_number_example' # str | Requests Number provides number of allowed requests (optional)
duration = 'duration_example' # str | Duration of load test in seconds (optional)

try:
    api_response = api_instance.create_loadtest_seldon_deployment(name, namespace, load_file, connections_number=connections_number, requests_number=requests_number, duration=duration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoadtestJobsApi->create_loadtest_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **load_file** | **file**| Prediction contains predict payload | 
 **connections_number** | **str**| Connections Number provides number of allowed connections | [optional] 
 **requests_number** | **str**| Requests Number provides number of allowed requests | [optional] 
 **duration** | **str**| Duration of load test in seconds | [optional] 

### Return type

[**Message**](Message.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_loadtest_pipeline**
> Message delete_loadtest_pipeline(job_name, name, namespace)



Delete Pipeline load test jobs

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
api_instance = seldon_deploy_sdk.LoadtestJobsApi(seldon_deploy_sdk.ApiClient(configuration))
job_name = 'job_name_example' # str | JobName identifies a job name
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.delete_loadtest_pipeline(job_name, name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoadtestJobsApi->delete_loadtest_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_name** | **str**| JobName identifies a job name | 
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**Message**](Message.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_loadtest_seldon_deployment**
> Message delete_loadtest_seldon_deployment(job_name, name, namespace)



Delete Seldon Deployment load test jobs

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
api_instance = seldon_deploy_sdk.LoadtestJobsApi(seldon_deploy_sdk.ApiClient(configuration))
job_name = 'job_name_example' # str | JobName identifies a job name
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.delete_loadtest_seldon_deployment(job_name, name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoadtestJobsApi->delete_loadtest_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_name** | **str**| JobName identifies a job name | 
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**Message**](Message.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_loadtest_pipeline**
> Message list_loadtest_pipeline(name, namespace)



List Pipeline load test jobs

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
api_instance = seldon_deploy_sdk.LoadtestJobsApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.list_loadtest_pipeline(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoadtestJobsApi->list_loadtest_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**Message**](Message.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_loadtest_seldon_deployment**
> Message list_loadtest_seldon_deployment(name, namespace)



List Seldon Deployment load test jobs

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
api_instance = seldon_deploy_sdk.LoadtestJobsApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.list_loadtest_seldon_deployment(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoadtestJobsApi->list_loadtest_seldon_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

[**Message**](Message.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

