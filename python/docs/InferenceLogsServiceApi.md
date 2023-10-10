# seldon_deploy_sdk.InferenceLogsServiceApi

All URIs are relative to *http://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inference_logs_service_get_deployment_inference_logs**](InferenceLogsServiceApi.md#inference_logs_service_get_deployment_inference_logs) | **POST** /inference-logs/namespace/{namespace}/seldondeployments/{deploymentName} | Get inference logs for seldon deployments.
[**inference_logs_service_get_model_inference_logs**](InferenceLogsServiceApi.md#inference_logs_service_get_model_inference_logs) | **POST** /inference-logs/namespace/{namespace}/pipelines/{pipelineName}/models/{modelName} | Get inference logs for seldon models.
[**inference_logs_service_list_deployment_inference_logs**](InferenceLogsServiceApi.md#inference_logs_service_list_deployment_inference_logs) | **GET** /inference-logs/seldondeployments | Get inference logs metadata for seldon deployments.
[**inference_logs_service_list_model_inference_logs**](InferenceLogsServiceApi.md#inference_logs_service_list_model_inference_logs) | **GET** /inference-logs/models | Get inference logs metadata for seldon models.


# **inference_logs_service_get_deployment_inference_logs**
> V1GetDeploymentInferenceLogsResponse inference_logs_service_get_deployment_inference_logs(namespace, deployment_name, body)

Get inference logs for seldon deployments.

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
api_instance = seldon_deploy_sdk.InferenceLogsServiceApi(seldon_deploy_sdk.ApiClient(configuration))
namespace = 'namespace_example' # str | The namespace that this seldon deployment belongs to.
deployment_name = 'deployment_name_example' # str | The name of the seldon deployment to get inference logs for.
body = seldon_deploy_sdk.Body1() # Body1 | 

try:
    # Get inference logs for seldon deployments.
    api_response = api_instance.inference_logs_service_get_deployment_inference_logs(namespace, deployment_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InferenceLogsServiceApi->inference_logs_service_get_deployment_inference_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The namespace that this seldon deployment belongs to. | 
 **deployment_name** | **str**| The name of the seldon deployment to get inference logs for. | 
 **body** | [**Body1**](Body1.md)|  | 

### Return type

[**V1GetDeploymentInferenceLogsResponse**](V1GetDeploymentInferenceLogsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inference_logs_service_get_model_inference_logs**
> V1GetModelInferenceLogsResponse inference_logs_service_get_model_inference_logs(namespace, pipeline_name, model_name, body)

Get inference logs for seldon models.

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
api_instance = seldon_deploy_sdk.InferenceLogsServiceApi(seldon_deploy_sdk.ApiClient(configuration))
namespace = 'namespace_example' # str | The namespace that this seldon deployment belongs to.
pipeline_name = 'pipeline_name_example' # str | The name of the seldon pipeline to get inference logs for.
model_name = 'model_name_example' # str | The name of the seldon model to get inference logs for.
body = seldon_deploy_sdk.Body() # Body | 

try:
    # Get inference logs for seldon models.
    api_response = api_instance.inference_logs_service_get_model_inference_logs(namespace, pipeline_name, model_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InferenceLogsServiceApi->inference_logs_service_get_model_inference_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The namespace that this seldon deployment belongs to. | 
 **pipeline_name** | **str**| The name of the seldon pipeline to get inference logs for. | 
 **model_name** | **str**| The name of the seldon model to get inference logs for. | 
 **body** | [**Body**](Body.md)|  | 

### Return type

[**V1GetModelInferenceLogsResponse**](V1GetModelInferenceLogsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inference_logs_service_list_deployment_inference_logs**
> V1ListDeploymentInferenceLogsResponse inference_logs_service_list_deployment_inference_logs(namespace=namespace, deployment_name=deployment_name, predictor_name=predictor_name, container_name=container_name)

Get inference logs metadata for seldon deployments.

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
api_instance = seldon_deploy_sdk.InferenceLogsServiceApi(seldon_deploy_sdk.ApiClient(configuration))
namespace = 'namespace_example' # str | The namespace that this seldon deployment belongs to. (optional)
deployment_name = 'deployment_name_example' # str | The name of the seldon deployment to get inference logs for. (optional)
predictor_name = 'predictor_name_example' # str | The predictor name of the seldon deployment to get inference logs for. e.g. \"default\", \"canary\", \"shadow\" (optional)
container_name = 'container_name_example' # str | The container name of the seldon deployment to get inference logs for. e.g. \"my-container\", \"input-transformer\", \"output-transformer\" (optional)

try:
    # Get inference logs metadata for seldon deployments.
    api_response = api_instance.inference_logs_service_list_deployment_inference_logs(namespace=namespace, deployment_name=deployment_name, predictor_name=predictor_name, container_name=container_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InferenceLogsServiceApi->inference_logs_service_list_deployment_inference_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The namespace that this seldon deployment belongs to. | [optional] 
 **deployment_name** | **str**| The name of the seldon deployment to get inference logs for. | [optional] 
 **predictor_name** | **str**| The predictor name of the seldon deployment to get inference logs for. e.g. \&quot;default\&quot;, \&quot;canary\&quot;, \&quot;shadow\&quot; | [optional] 
 **container_name** | **str**| The container name of the seldon deployment to get inference logs for. e.g. \&quot;my-container\&quot;, \&quot;input-transformer\&quot;, \&quot;output-transformer\&quot; | [optional] 

### Return type

[**V1ListDeploymentInferenceLogsResponse**](V1ListDeploymentInferenceLogsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inference_logs_service_list_model_inference_logs**
> V1ListModelInferenceLogsResponse inference_logs_service_list_model_inference_logs(namespace, pipeline_name, model_name)

Get inference logs metadata for seldon models.

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
api_instance = seldon_deploy_sdk.InferenceLogsServiceApi(seldon_deploy_sdk.ApiClient(configuration))
namespace = 'namespace_example' # str | The namespace that this seldon deployment belongs to.
pipeline_name = 'pipeline_name_example' # str | The name of the seldon pipeline to get inference logs for.
model_name = 'model_name_example' # str | The name of the seldon model to get inference logs for.

try:
    # Get inference logs metadata for seldon models.
    api_response = api_instance.inference_logs_service_list_model_inference_logs(namespace, pipeline_name, model_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InferenceLogsServiceApi->inference_logs_service_list_model_inference_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The namespace that this seldon deployment belongs to. | 
 **pipeline_name** | **str**| The name of the seldon pipeline to get inference logs for. | 
 **model_name** | **str**| The name of the seldon model to get inference logs for. | 

### Return type

[**V1ListModelInferenceLogsResponse**](V1ListModelInferenceLogsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

