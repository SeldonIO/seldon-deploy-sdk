# seldon_deploy_sdk.PermissionManagementServiceApi

All URIs are relative to *http://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**permission_management_service_add_user_to_group**](PermissionManagementServiceApi.md#permission_management_service_add_user_to_group) | **PUT** /iam/users/{username}/groups/{group} | Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. Add user to a group. The caller must have &#x60;write&#x60; permission on &#x60;system/iam&#x60;.
[**permission_management_service_create_group**](PermissionManagementServiceApi.md#permission_management_service_create_group) | **POST** /iam/groups | Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. Create a group. The caller must have &#x60;write&#x60; permission on &#x60;system/iam&#x60;.
[**permission_management_service_create_policy**](PermissionManagementServiceApi.md#permission_management_service_create_policy) | **POST** /iam/policy | Create an authorization policy. The user must have &#x60;grant&#x60; permissions on the resource in the policy.
[**permission_management_service_create_user**](PermissionManagementServiceApi.md#permission_management_service_create_user) | **POST** /iam/users | Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. Create a user. The caller must have &#x60;write&#x60; permission on &#x60;system/iam&#x60;.
[**permission_management_service_delete_group**](PermissionManagementServiceApi.md#permission_management_service_delete_group) | **DELETE** /iam/groups/{name} | Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. Delete a group. The caller must have &#x60;write&#x60; permission on &#x60;system/iam&#x60;.
[**permission_management_service_delete_policy**](PermissionManagementServiceApi.md#permission_management_service_delete_policy) | **DELETE** /iam/policy | Delete an authorization policy. The user must have &#x60;grant&#x60; permissions on the resource in the policy.
[**permission_management_service_delete_user**](PermissionManagementServiceApi.md#permission_management_service_delete_user) | **DELETE** /iam/users/{username} | Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. Delete a user. The caller must have &#x60;write&#x60; permission on &#x60;system/iam&#x60;.
[**permission_management_service_delete_user_from_group**](PermissionManagementServiceApi.md#permission_management_service_delete_user_from_group) | **DELETE** /iam/users/{username}/groups/{group} | Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. Delete user from a group. The caller must have &#x60;write&#x60; permission on &#x60;system/iam&#x60;.
[**permission_management_service_get_group_members**](PermissionManagementServiceApi.md#permission_management_service_get_group_members) | **GET** /iam/groups/{groupName}/members | Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. List all members of a group. The caller must have &#x60;read&#x60; permission on &#x60;system/iam&#x60;.
[**permission_management_service_get_groups**](PermissionManagementServiceApi.md#permission_management_service_get_groups) | **GET** /iam/groups | Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. List all groups. The caller must have &#x60;read&#x60; permission on &#x60;system/iam&#x60;.
[**permission_management_service_get_permissions**](PermissionManagementServiceApi.md#permission_management_service_get_permissions) | **GET** /iam/policy/permissions | List all permissions associated with the given users and groups. A regular user will be able to see only their permissions and the permissions of their groups. A user with &#x60;read&#x60; permission on &#x60;system/iam&#x60; can see all permissions.
[**permission_management_service_get_policy_targets**](PermissionManagementServiceApi.md#permission_management_service_get_policy_targets) | **GET** /iam/policy/targets | List all users and groups who have access to the given resource/action pair. The user calling this endpoint must have &#x60;grant&#x60; access to the given resource.
[**permission_management_service_get_user_groups**](PermissionManagementServiceApi.md#permission_management_service_get_user_groups) | **GET** /iam/users/{username}/groups | Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. List all groups of a user. The caller must have &#x60;read&#x60; permission on &#x60;system/iam&#x60;.
[**permission_management_service_get_users**](PermissionManagementServiceApi.md#permission_management_service_get_users) | **GET** /iam/users | Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. List users. The caller must have &#x60;read&#x60; permission on &#x60;system/iam&#x60;.


# **permission_management_service_add_user_to_group**
> V1AddUserToGroupResponse permission_management_service_add_user_to_group(username, group)

Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. Add user to a group. The caller must have `write` permission on `system/iam`.

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
username = 'username_example' # str | The name of the user to be added to a group.
group = 'group_example' # str | The name of the group to which to add a user.

try:
    # Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. Add user to a group. The caller must have `write` permission on `system/iam`.
    api_response = api_instance.permission_management_service_add_user_to_group(username, group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionManagementServiceApi->permission_management_service_add_user_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The name of the user to be added to a group. | 
 **group** | **str**| The name of the group to which to add a user. | 

### Return type

[**V1AddUserToGroupResponse**](V1AddUserToGroupResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_management_service_create_group**
> V1CreateGroupResponse permission_management_service_create_group(body)

Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. Create a group. The caller must have `write` permission on `system/iam`.

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
body = seldon_deploy_sdk.V1CreateGroupRequest() # V1CreateGroupRequest | 

try:
    # Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. Create a group. The caller must have `write` permission on `system/iam`.
    api_response = api_instance.permission_management_service_create_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionManagementServiceApi->permission_management_service_create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateGroupRequest**](V1CreateGroupRequest.md)|  | 

### Return type

[**V1CreateGroupResponse**](V1CreateGroupResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **permission_management_service_create_user**
> V1CreateUserResponse permission_management_service_create_user(body)

Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. Create a user. The caller must have `write` permission on `system/iam`.

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
body = seldon_deploy_sdk.V1CreateUserRequest() # V1CreateUserRequest | 

try:
    # Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. Create a user. The caller must have `write` permission on `system/iam`.
    api_response = api_instance.permission_management_service_create_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionManagementServiceApi->permission_management_service_create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateUserRequest**](V1CreateUserRequest.md)|  | 

### Return type

[**V1CreateUserResponse**](V1CreateUserResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_management_service_delete_group**
> V1DeleteGroupResponse permission_management_service_delete_group(name)

Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. Delete a group. The caller must have `write` permission on `system/iam`.

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
name = 'name_example' # str | The name of the group to be deleted.

try:
    # Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. Delete a group. The caller must have `write` permission on `system/iam`.
    api_response = api_instance.permission_management_service_delete_group(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionManagementServiceApi->permission_management_service_delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the group to be deleted. | 

### Return type

[**V1DeleteGroupResponse**](V1DeleteGroupResponse.md)

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

# **permission_management_service_delete_user**
> V1DeleteUserResponse permission_management_service_delete_user(username)

Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. Delete a user. The caller must have `write` permission on `system/iam`.

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
username = 'username_example' # str | The username of the user to be deleted.

try:
    # Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. Delete a user. The caller must have `write` permission on `system/iam`.
    api_response = api_instance.permission_management_service_delete_user(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionManagementServiceApi->permission_management_service_delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user to be deleted. | 

### Return type

[**V1DeleteUserResponse**](V1DeleteUserResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_management_service_delete_user_from_group**
> V1DeleteUserFromGroupResponse permission_management_service_delete_user_from_group(username, group)

Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. Delete user from a group. The caller must have `write` permission on `system/iam`.

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
username = 'username_example' # str | The name of the user to be removed from a group.
group = 'group_example' # str | The name of the group from which to remove a user.

try:
    # Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. Delete user from a group. The caller must have `write` permission on `system/iam`.
    api_response = api_instance.permission_management_service_delete_user_from_group(username, group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionManagementServiceApi->permission_management_service_delete_user_from_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The name of the user to be removed from a group. | 
 **group** | **str**| The name of the group from which to remove a user. | 

### Return type

[**V1DeleteUserFromGroupResponse**](V1DeleteUserFromGroupResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_management_service_get_group_members**
> V1GetGroupMembersResponse permission_management_service_get_group_members(group_name)

Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. List all members of a group. The caller must have `read` permission on `system/iam`.

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
group_name = 'group_name_example' # str | The name of the group for which to get members.

try:
    # Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. List all members of a group. The caller must have `read` permission on `system/iam`.
    api_response = api_instance.permission_management_service_get_group_members(group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionManagementServiceApi->permission_management_service_get_group_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The name of the group for which to get members. | 

### Return type

[**V1GetGroupMembersResponse**](V1GetGroupMembersResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_management_service_get_groups**
> V1GetGroupsResponse permission_management_service_get_groups()

Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. List all groups. The caller must have `read` permission on `system/iam`.

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

try:
    # Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. List all groups. The caller must have `read` permission on `system/iam`.
    api_response = api_instance.permission_management_service_get_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionManagementServiceApi->permission_management_service_get_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1GetGroupsResponse**](V1GetGroupsResponse.md)

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

# **permission_management_service_get_user_groups**
> V1GetUserGroupsResponse permission_management_service_get_user_groups(username)

Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. List all groups of a user. The caller must have `read` permission on `system/iam`.

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
username = 'username_example' # str | The name of the user for who to get groups.

try:
    # Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. List all groups of a user. The caller must have `read` permission on `system/iam`.
    api_response = api_instance.permission_management_service_get_user_groups(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionManagementServiceApi->permission_management_service_get_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The name of the user for who to get groups. | 

### Return type

[**V1GetUserGroupsResponse**](V1GetUserGroupsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_management_service_get_users**
> V1GetUsersResponse permission_management_service_get_users(username=username, email=email, first_name=first_name, last_name=last_name)

Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. List users. The caller must have `read` permission on `system/iam`.

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
username = 'username_example' # str | The username of the user to fetch. It must consist of only letters, numbers, underscores, and dashes, and be at most 30 characters. (optional)
email = 'email_example' # str | The email of the user to fetch. It must be a valid email. (optional)
first_name = 'first_name_example' # str |  (optional)
last_name = 'last_name_example' # str |  (optional)

try:
    # Endpoint is available only when user management is enabled configured - refer to the docs for how to do this. List users. The caller must have `read` permission on `system/iam`.
    api_response = api_instance.permission_management_service_get_users(username=username, email=email, first_name=first_name, last_name=last_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionManagementServiceApi->permission_management_service_get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user to fetch. It must consist of only letters, numbers, underscores, and dashes, and be at most 30 characters. | [optional] 
 **email** | **str**| The email of the user to fetch. It must be a valid email. | [optional] 
 **first_name** | **str**|  | [optional] 
 **last_name** | **str**|  | [optional] 

### Return type

[**V1GetUsersResponse**](V1GetUsersResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

