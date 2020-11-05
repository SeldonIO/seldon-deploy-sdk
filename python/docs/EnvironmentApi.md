# seldon_deploy_client.EnvironmentApi

All URIs are relative to *http://localhost:8000/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_user**](EnvironmentApi.md#read_user) | **GET** /user | 
[**read_version**](EnvironmentApi.md#read_version) | **GET** /version | 


# **read_user**
> UserInfo read_user()



Read the request user

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_client
from seldon_deploy_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = seldon_deploy_client.EnvironmentApi()

try:
    api_response = api_instance.read_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->read_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_version**
> VersionInfo read_version()



Read the version

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_client
from seldon_deploy_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = seldon_deploy_client.EnvironmentApi()

try:
    api_response = api_instance.read_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->read_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VersionInfo**](VersionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

