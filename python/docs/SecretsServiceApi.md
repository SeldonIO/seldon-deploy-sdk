# seldon_deploy_sdk.SecretsServiceApi

All URIs are relative to *http://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secrets_service_create_gcs_bucket_secret**](SecretsServiceApi.md#secrets_service_create_gcs_bucket_secret) | **POST** /secrets/{namespace}/bucket/gcs/{remote} | Creates a GCS bucket secret according to specified parameters.
[**secrets_service_create_rclone_bucket_secret**](SecretsServiceApi.md#secrets_service_create_rclone_bucket_secret) | **POST** /secrets/{namespace}/bucket/rclone/{remote} | Creates a generic rclone bucket secret according to specified parameters.
[**secrets_service_create_registry_secret**](SecretsServiceApi.md#secrets_service_create_registry_secret) | **POST** /secrets/{namespace}/registry/{name} | Creates a registry secret according to specified parameters.
[**secrets_service_create_s3_bucket_secret**](SecretsServiceApi.md#secrets_service_create_s3_bucket_secret) | **POST** /secrets/{namespace}/bucket/s3/{remote} | Creates a S3 bucket secret according to specified parameters.
[**secrets_service_delete_secret**](SecretsServiceApi.md#secrets_service_delete_secret) | **DELETE** /secrets/{namespace}/{secretType}/{name} | Deletes the specified secret.
[**secrets_service_list_secrets**](SecretsServiceApi.md#secrets_service_list_secrets) | **GET** /secrets/{namespace}/{secretType} | Lists the names and metadata of secrets used by Seldon Deploy.


# **secrets_service_create_gcs_bucket_secret**
> V1CreateGCSBucketSecretResponse secrets_service_create_gcs_bucket_secret(namespace, remote, account_credentials, secret_version=secret_version)

Creates a GCS bucket secret according to specified parameters.

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
api_instance = seldon_deploy_sdk.SecretsServiceApi(seldon_deploy_sdk.ApiClient(configuration))
namespace = 'namespace_example' # str | The namespace to create secret in.
remote = 'remote_example' # str | The remote name must contain only lowercase letters, digits or dashes, must start and end with a lowercase letter or digit and must be no more than 30 characters in length. The created secret will be named {remote}-bucket-envvars or {remote}-bucket-params, for Core 1 or Core 2, respectively.
account_credentials = NULL # object | 
secret_version = 'CORE_1' # str | The version of the secret to use (CORE_V1 or CORE_V2). Default value is CORE_V1 (optional) (default to CORE_1)

try:
    # Creates a GCS bucket secret according to specified parameters.
    api_response = api_instance.secrets_service_create_gcs_bucket_secret(namespace, remote, account_credentials, secret_version=secret_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsServiceApi->secrets_service_create_gcs_bucket_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The namespace to create secret in. | 
 **remote** | **str**| The remote name must contain only lowercase letters, digits or dashes, must start and end with a lowercase letter or digit and must be no more than 30 characters in length. The created secret will be named {remote}-bucket-envvars or {remote}-bucket-params, for Core 1 or Core 2, respectively. | 
 **account_credentials** | **object**|  | 
 **secret_version** | **str**| The version of the secret to use (CORE_V1 or CORE_V2). Default value is CORE_V1 | [optional] [default to CORE_1]

### Return type

[**V1CreateGCSBucketSecretResponse**](V1CreateGCSBucketSecretResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_create_rclone_bucket_secret**
> V1CreateRcloneBucketSecretResponse secrets_service_create_rclone_bucket_secret(namespace, remote, rclone_config, format=format)

Creates a generic rclone bucket secret according to specified parameters.

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
api_instance = seldon_deploy_sdk.SecretsServiceApi(seldon_deploy_sdk.ApiClient(configuration))
namespace = 'namespace_example' # str | The namespace to create secret in.
remote = 'remote_example' # str | The remote name must contain only lowercase letters, digits or dashes, must start and end with a lowercase letter or digit and must be no more than 30 characters in length. The created secret will be named {remote}-bucket-envvars or {remote}-bucket-params, for Core 1 or Core 2, respectively.
rclone_config = seldon_deploy_sdk.V1RcloneConfig() # V1RcloneConfig | 
format = 'env_var' # str | The format for the secret. Must be one of (env_var, config_param). env_var formats the secret as environment variables, each with a key and a value. env_var is suitable for Seldon Core v1 and Argo Workflows. config_param formats the secret to be compatible with Rclone's HTTP API. config_param is suitable for Seldon Core v2. (optional) (default to env_var)

try:
    # Creates a generic rclone bucket secret according to specified parameters.
    api_response = api_instance.secrets_service_create_rclone_bucket_secret(namespace, remote, rclone_config, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsServiceApi->secrets_service_create_rclone_bucket_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The namespace to create secret in. | 
 **remote** | **str**| The remote name must contain only lowercase letters, digits or dashes, must start and end with a lowercase letter or digit and must be no more than 30 characters in length. The created secret will be named {remote}-bucket-envvars or {remote}-bucket-params, for Core 1 or Core 2, respectively. | 
 **rclone_config** | [**V1RcloneConfig**](V1RcloneConfig.md)|  | 
 **format** | **str**| The format for the secret. Must be one of (env_var, config_param). env_var formats the secret as environment variables, each with a key and a value. env_var is suitable for Seldon Core v1 and Argo Workflows. config_param formats the secret to be compatible with Rclone&#39;s HTTP API. config_param is suitable for Seldon Core v2. | [optional] [default to env_var]

### Return type

[**V1CreateRcloneBucketSecretResponse**](V1CreateRcloneBucketSecretResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_create_registry_secret**
> V1CreateRegistrySecretResponse secrets_service_create_registry_secret(namespace, name, credentials_config)

Creates a registry secret according to specified parameters.

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
api_instance = seldon_deploy_sdk.SecretsServiceApi(seldon_deploy_sdk.ApiClient(configuration))
namespace = 'namespace_example' # str | The namespace to create secret in.
name = 'name_example' # str | The secret name must contain only lowercase letters, digits or dashes, must start and end with a lowercase letter or digit and must be no more than 30 characters in length.
credentials_config = NULL # object | 

try:
    # Creates a registry secret according to specified parameters.
    api_response = api_instance.secrets_service_create_registry_secret(namespace, name, credentials_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsServiceApi->secrets_service_create_registry_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The namespace to create secret in. | 
 **name** | **str**| The secret name must contain only lowercase letters, digits or dashes, must start and end with a lowercase letter or digit and must be no more than 30 characters in length. | 
 **credentials_config** | **object**|  | 

### Return type

[**V1CreateRegistrySecretResponse**](V1CreateRegistrySecretResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_create_s3_bucket_secret**
> V1CreateS3BucketSecretResponse secrets_service_create_s3_bucket_secret(namespace, remote, s3_credentials, secret_version=secret_version)

Creates a S3 bucket secret according to specified parameters.

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
api_instance = seldon_deploy_sdk.SecretsServiceApi(seldon_deploy_sdk.ApiClient(configuration))
namespace = 'namespace_example' # str | The namespace to create secret in.
remote = 'remote_example' # str | The remote name must contain only lowercase letters, digits or dashes, must start and end with a lowercase letter or digit and must be no more than 30 characters in length. The created secret will be named {remote}-bucket-envvars or {remote}-bucket-params, for Core 1 or Core 2, respectively.
s3_credentials = seldon_deploy_sdk.V1S3Credentials() # V1S3Credentials | 
secret_version = 'CORE_1' # str | The version of the secret to use (CORE_1 or CORE_2). Default value is CORE_1 (optional) (default to CORE_1)

try:
    # Creates a S3 bucket secret according to specified parameters.
    api_response = api_instance.secrets_service_create_s3_bucket_secret(namespace, remote, s3_credentials, secret_version=secret_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsServiceApi->secrets_service_create_s3_bucket_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The namespace to create secret in. | 
 **remote** | **str**| The remote name must contain only lowercase letters, digits or dashes, must start and end with a lowercase letter or digit and must be no more than 30 characters in length. The created secret will be named {remote}-bucket-envvars or {remote}-bucket-params, for Core 1 or Core 2, respectively. | 
 **s3_credentials** | [**V1S3Credentials**](V1S3Credentials.md)|  | 
 **secret_version** | **str**| The version of the secret to use (CORE_1 or CORE_2). Default value is CORE_1 | [optional] [default to CORE_1]

### Return type

[**V1CreateS3BucketSecretResponse**](V1CreateS3BucketSecretResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_delete_secret**
> V1DeleteSecretResponse secrets_service_delete_secret(namespace, secret_type, name)

Deletes the specified secret.

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
api_instance = seldon_deploy_sdk.SecretsServiceApi(seldon_deploy_sdk.ApiClient(configuration))
namespace = 'namespace_example' # str | The namespace to delete secret from.
secret_type = 'secret_type_example' # str | The secret type of the secret to be deleted, can be one of (`bucket`, `registry`).
name = 'name_example' # str | The name of the secret to delete.

try:
    # Deletes the specified secret.
    api_response = api_instance.secrets_service_delete_secret(namespace, secret_type, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsServiceApi->secrets_service_delete_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The namespace to delete secret from. | 
 **secret_type** | **str**| The secret type of the secret to be deleted, can be one of (&#x60;bucket&#x60;, &#x60;registry&#x60;). | 
 **name** | **str**| The name of the secret to delete. | 

### Return type

[**V1DeleteSecretResponse**](V1DeleteSecretResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_list_secrets**
> V1ListSecretsResponse secrets_service_list_secrets(namespace, secret_type, bucket_secret_format=bucket_secret_format, page_size=page_size, page_token=page_token, search=search)

Lists the names and metadata of secrets used by Seldon Deploy.

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
api_instance = seldon_deploy_sdk.SecretsServiceApi(seldon_deploy_sdk.ApiClient(configuration))
namespace = 'namespace_example' # str | The namespace to list secrets in.
secret_type = 'secret_type_example' # str | The secret type, can be one of (`bucket`, `registry`) or `all` to list all secrets used by Seldon Deploy.
bucket_secret_format = 'env_var' # str | Optional filter for the format of bucket secrets. Only applicable when `secret_type` is `bucket.` (optional) (default to env_var)
page_size = 'page_size_example' # str | Optional The maximum number of Secrets to return in the response. (optional)
page_token = 'page_token_example' # str | Optional pagination token returned from a previous call to List that indicates where this listing should continue from. (optional)
search = 'search_example' # str | Optional search string for secrets. (optional)

try:
    # Lists the names and metadata of secrets used by Seldon Deploy.
    api_response = api_instance.secrets_service_list_secrets(namespace, secret_type, bucket_secret_format=bucket_secret_format, page_size=page_size, page_token=page_token, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsServiceApi->secrets_service_list_secrets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The namespace to list secrets in. | 
 **secret_type** | **str**| The secret type, can be one of (&#x60;bucket&#x60;, &#x60;registry&#x60;) or &#x60;all&#x60; to list all secrets used by Seldon Deploy. | 
 **bucket_secret_format** | **str**| Optional filter for the format of bucket secrets. Only applicable when &#x60;secret_type&#x60; is &#x60;bucket.&#x60; | [optional] [default to env_var]
 **page_size** | **str**| Optional The maximum number of Secrets to return in the response. | [optional] 
 **page_token** | **str**| Optional pagination token returned from a previous call to List that indicates where this listing should continue from. | [optional] 
 **search** | **str**| Optional search string for secrets. | [optional] 

### Return type

[**V1ListSecretsResponse**](V1ListSecretsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

