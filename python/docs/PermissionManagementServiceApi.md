# seldon_deploy_sdk.PermissionManagementServiceApi

All URIs are relative to *https://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**permission_management_service_create_policy**](PermissionManagementServiceApi.md#permission_management_service_create_policy) | **POST** /iam/policy | Create an authorization policy. The user must have &#x60;grant&#x60; permissions on the resource in the policy.
[**permission_management_service_delete_policy**](PermissionManagementServiceApi.md#permission_management_service_delete_policy) | **DELETE** /iam/policy | Delete an authorization policy. The user must have &#x60;grant&#x60; permissions on the resource in the policy.
[**permission_management_service_get_permissions**](PermissionManagementServiceApi.md#permission_management_service_get_permissions) | **GET** /iam/policy/permissions | List all permissions associated with the given users and groups. A regular user will be able to see only their permissions and the permissions of their groups. A user with &#x60;read&#x60; permission on &#x60;system/iam&#x60; can see all permissions.
[**permission_management_service_get_policy_targets**](PermissionManagementServiceApi.md#permission_management_service_get_policy_targets) | **GET** /iam/policy/targets | List all users and groups who have access to the given resource/action pair. The user calling this endpoint must have &#x60;grant&#x60; access to the given resource.


# **permission_management_service_create_policy**
> V1CreatePolicyResponse permission_management_service_create_policy(body)

Create an authorization policy. The user must have `grant` permissions on the resource in the policy.

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
api_instance = seldon_deploy_sdk.PermissionManagementServiceApi(seldon_deploy_sdk.ApiClient(configuration))
body = seldon_deploy_sdk.V1Policy() # V1Policy | 

try:
    # Create an authorization policy. The user must have `grant` permissions on the resource in the policy.
    api_response = api_instance.permission_management_service_create_policy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionManagementServiceApi->permission_management_service_create_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Policy**](V1Policy.md)|  | 

### Return type

[**V1CreatePolicyResponse**](V1CreatePolicyResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_management_service_delete_policy**
> V1DeletePolicyResponse permission_management_service_delete_policy(action, resource, users=users, groups=groups)

Delete an authorization policy. The user must have `grant` permissions on the resource in the policy.

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
api_instance = seldon_deploy_sdk.PermissionManagementServiceApi(seldon_deploy_sdk.ApiClient(configuration))
action = 'action_example' # str | The action part of the resource/action permission to revoke.
resource = 'resource_example' # str | The resource part of the resource/action permission to revoke.
users = ['users_example'] # list[str] | The user IDs from which to revoke the given resource/action permission. (optional)
groups = ['groups_example'] # list[str] | The groups from which to revoke the given resource/action permission. (optional)

try:
    # Delete an authorization policy. The user must have `grant` permissions on the resource in the policy.
    api_response = api_instance.permission_management_service_delete_policy(action, resource, users=users, groups=groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionManagementServiceApi->permission_management_service_delete_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| The action part of the resource/action permission to revoke. | 
 **resource** | **str**| The resource part of the resource/action permission to revoke. | 
 **users** | [**list[str]**](str.md)| The user IDs from which to revoke the given resource/action permission. | [optional] 
 **groups** | [**list[str]**](str.md)| The groups from which to revoke the given resource/action permission. | [optional] 

### Return type

[**V1DeletePolicyResponse**](V1DeletePolicyResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_management_service_get_permissions**
> V1GetPermissionsResponse permission_management_service_get_permissions(users=users, groups=groups, caller_permissions=caller_permissions)

List all permissions associated with the given users and groups. A regular user will be able to see only their permissions and the permissions of their groups. A user with `read` permission on `system/iam` can see all permissions.

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
api_instance = seldon_deploy_sdk.PermissionManagementServiceApi(seldon_deploy_sdk.ApiClient(configuration))
users = ['users_example'] # list[str] | The user IDs for which to list permission. (optional)
groups = ['groups_example'] # list[str] | The groups for which to list permission. (optional)
caller_permissions = true # bool | If true will list the permissions of the user making the request. All users have permissions to check their permissions. (optional)

try:
    # List all permissions associated with the given users and groups. A regular user will be able to see only their permissions and the permissions of their groups. A user with `read` permission on `system/iam` can see all permissions.
    api_response = api_instance.permission_management_service_get_permissions(users=users, groups=groups, caller_permissions=caller_permissions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionManagementServiceApi->permission_management_service_get_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users** | [**list[str]**](str.md)| The user IDs for which to list permission. | [optional] 
 **groups** | [**list[str]**](str.md)| The groups for which to list permission. | [optional] 
 **caller_permissions** | **bool**| If true will list the permissions of the user making the request. All users have permissions to check their permissions. | [optional] 

### Return type

[**V1GetPermissionsResponse**](V1GetPermissionsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_management_service_get_policy_targets**
> V1GetPolicyTargetsResponse permission_management_service_get_policy_targets(action, resource)

List all users and groups who have access to the given resource/action pair. The user calling this endpoint must have `grant` access to the given resource.

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
api_instance = seldon_deploy_sdk.PermissionManagementServiceApi(seldon_deploy_sdk.ApiClient(configuration))
action = 'action_example' # str | The action a target should be able to perform on the given resource.
resource = 'resource_example' # str | The resource a target should have access to.

try:
    # List all users and groups who have access to the given resource/action pair. The user calling this endpoint must have `grant` access to the given resource.
    api_response = api_instance.permission_management_service_get_policy_targets(action, resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionManagementServiceApi->permission_management_service_get_policy_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| The action a target should be able to perform on the given resource. | 
 **resource** | **str**| The resource a target should have access to. | 

### Return type

[**V1GetPolicyTargetsResponse**](V1GetPolicyTargetsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

