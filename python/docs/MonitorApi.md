# seldon_deploy_sdk.MonitorApi

All URIs are relative to *http://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**seldon_deployment_feature_distributions**](MonitorApi.md#seldon_deployment_feature_distributions) | **POST** /namespaces/{namespace}/seldondeployments/{name}/monitor/featuredistributions | 
[**seldon_deployment_feature_statistics**](MonitorApi.md#seldon_deployment_feature_statistics) | **POST** /namespaces/{namespace}/seldondeployments/{name}/monitor/featurestatistics | 
[**seldon_pipeline_feature_distributions**](MonitorApi.md#seldon_pipeline_feature_distributions) | **POST** /namespaces/{namespace}/pipelines/{name}/monitor/featuredistributions | 
[**seldon_pipeline_feature_statistics**](MonitorApi.md#seldon_pipeline_feature_statistics) | **POST** /namespaces/{namespace}/pipelines/{name}/monitor/featurestatistics | 


# **seldon_deployment_feature_distributions**
> FeatureDistributionResponse seldon_deployment_feature_distributions(name, namespace, feature_data)



Get the specified Seldon Deployment predictions feature distribution

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
api_instance = seldon_deploy_sdk.MonitorApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
feature_data = seldon_deploy_sdk.DeploymentFeatureData() # DeploymentFeatureData | Deployment Feature Data

try:
    api_response = api_instance.seldon_deployment_feature_distributions(name, namespace, feature_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorApi->seldon_deployment_feature_distributions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **feature_data** | [**DeploymentFeatureData**](DeploymentFeatureData.md)| Deployment Feature Data | 

### Return type

[**FeatureDistributionResponse**](FeatureDistributionResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **seldon_deployment_feature_statistics**
> FeatureStatisticsResponse seldon_deployment_feature_statistics(name, namespace, feature_data)



Get the specified Seldon Deployment predictions feature statistics

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
api_instance = seldon_deploy_sdk.MonitorApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
feature_data = seldon_deploy_sdk.DeploymentFeatureData() # DeploymentFeatureData | Deployment Feature Data

try:
    api_response = api_instance.seldon_deployment_feature_statistics(name, namespace, feature_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorApi->seldon_deployment_feature_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **feature_data** | [**DeploymentFeatureData**](DeploymentFeatureData.md)| Deployment Feature Data | 

### Return type

[**FeatureStatisticsResponse**](FeatureStatisticsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **seldon_pipeline_feature_distributions**
> FeatureDistributionResponse seldon_pipeline_feature_distributions(name, namespace, feature_data)



Get the specified Seldon Deployment predictions feature distribution

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
api_instance = seldon_deploy_sdk.MonitorApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
feature_data = seldon_deploy_sdk.DeploymentFeatureData() # DeploymentFeatureData | Deployment Feature Data

try:
    api_response = api_instance.seldon_pipeline_feature_distributions(name, namespace, feature_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorApi->seldon_pipeline_feature_distributions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **feature_data** | [**DeploymentFeatureData**](DeploymentFeatureData.md)| Deployment Feature Data | 

### Return type

[**FeatureDistributionResponse**](FeatureDistributionResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **seldon_pipeline_feature_statistics**
> FeatureStatisticsResponse seldon_pipeline_feature_statistics(name, namespace, feature_data)



Get the specified Seldon Deployment predictions feature statistics

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
api_instance = seldon_deploy_sdk.MonitorApi(seldon_deploy_sdk.ApiClient(configuration))
name = 'name_example' # str | Name identifies a resource
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources
feature_data = seldon_deploy_sdk.DeploymentFeatureData() # DeploymentFeatureData | Deployment Feature Data

try:
    api_response = api_instance.seldon_pipeline_feature_statistics(name, namespace, feature_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorApi->seldon_pipeline_feature_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name identifies a resource | 
 **namespace** | **str**| Namespace provides a logical grouping of resources | 
 **feature_data** | [**DeploymentFeatureData**](DeploymentFeatureData.md)| Deployment Feature Data | 

### Return type

[**FeatureStatisticsResponse**](FeatureStatisticsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

