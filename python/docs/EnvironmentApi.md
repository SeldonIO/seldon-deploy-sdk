# seldon_deploy_client.EnvironmentApi

All URIs are relative to *https://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_cluster**](EnvironmentApi.md#read_cluster) | **GET** /cluster | 
[**read_user**](EnvironmentApi.md#read_user) | **GET** /user | 
[**read_version**](EnvironmentApi.md#read_version) | **GET** /version | 


# **read_cluster**
> ClusterInfo read_cluster()



Read the cluster info

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
api_instance = seldon_deploy_client.EnvironmentApi(seldon_deploy_client.ApiClient(configuration))

try:
    api_response = api_instance.read_cluster()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->read_cluster: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterInfo**](ClusterInfo.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# Configure OAuth2 access token for authorization: OAuth2
configuration = seldon_deploy_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = seldon_deploy_client.EnvironmentApi(seldon_deploy_client.ApiClient(configuration))

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

[OAuth2](../README.md#OAuth2)

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

# Configure OAuth2 access token for authorization: OAuth2
configuration = seldon_deploy_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = seldon_deploy_client.EnvironmentApi(seldon_deploy_client.ApiClient(configuration))

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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

