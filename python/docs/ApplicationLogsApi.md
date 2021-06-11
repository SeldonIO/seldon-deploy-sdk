# seldon_deploy_sdk.ApplicationLogsApi

All URIs are relative to *https://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_application_logs**](ApplicationLogsApi.md#read_application_logs) | **POST** /applicationlogs | Read application container logs from elastic search.


# **read_application_logs**
> ApplicationLogsResponse read_application_logs(body)

Read application container logs from elastic search.

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
api_instance = seldon_deploy_sdk.ApplicationLogsApi(seldon_deploy_sdk.ApiClient(configuration))
body = seldon_deploy_sdk.ApplicationLogsParams() # ApplicationLogsParams | ApplicationLogs

try:
    # Read application container logs from elastic search.
    api_response = api_instance.read_application_logs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationLogsApi->read_application_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationLogsParams**](ApplicationLogsParams.md)| ApplicationLogs | 

### Return type

[**ApplicationLogsResponse**](ApplicationLogsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

