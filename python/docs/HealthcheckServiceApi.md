# seldon_deploy_sdk.HealthcheckServiceApi

All URIs are relative to *http://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthcheck_service_get_dependency_health**](HealthcheckServiceApi.md#healthcheck_service_get_dependency_health) | **GET** /healthcheck/{dependency} | List the current health of a specific Seldon Deploy dependency or all of them


# **healthcheck_service_get_dependency_health**
> V1DependencyHealthResponse healthcheck_service_get_dependency_health(dependency)

List the current health of a specific Seldon Deploy dependency or all of them

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
api_instance = seldon_deploy_sdk.HealthcheckServiceApi(seldon_deploy_sdk.ApiClient(configuration))
dependency = 'dependency_example' # str | 

try:
    # List the current health of a specific Seldon Deploy dependency or all of them
    api_response = api_instance.healthcheck_service_get_dependency_health(dependency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthcheckServiceApi->healthcheck_service_get_dependency_health: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dependency** | **str**|  | 

### Return type

[**V1DependencyHealthResponse**](V1DependencyHealthResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

