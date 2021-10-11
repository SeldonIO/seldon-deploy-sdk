# seldon_deploy_sdk.AlertingServiceApi

All URIs are relative to *https://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alerting_service_list_alerts**](AlertingServiceApi.md#alerting_service_list_alerts) | **GET** /alerting/alerts | List currently firing alerts.
[**alerting_service_trigger_test_alert**](AlertingServiceApi.md#alerting_service_trigger_test_alert) | **POST** /alerting/test | Triggers a test alert to check alerting workflow.


# **alerting_service_list_alerts**
> V1ListAlertsResponse alerting_service_list_alerts()

List currently firing alerts.

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
api_instance = seldon_deploy_sdk.AlertingServiceApi(seldon_deploy_sdk.ApiClient(configuration))

try:
    # List currently firing alerts.
    api_response = api_instance.alerting_service_list_alerts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingServiceApi->alerting_service_list_alerts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1ListAlertsResponse**](V1ListAlertsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alerting_service_trigger_test_alert**
> V1TriggerTestAlertResponse alerting_service_trigger_test_alert(body)

Triggers a test alert to check alerting workflow.

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
api_instance = seldon_deploy_sdk.AlertingServiceApi(seldon_deploy_sdk.ApiClient(configuration))
body = true # bool | Set to true if you wish to test Prometheus -> Alertmanager connection False sends an alert payload directly to Alertmanager, skipping Prometheus metrics/alert flow

try:
    # Triggers a test alert to check alerting workflow.
    api_response = api_instance.alerting_service_trigger_test_alert(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertingServiceApi->alerting_service_trigger_test_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bool**| Set to true if you wish to test Prometheus -&gt; Alertmanager connection False sends an alert payload directly to Alertmanager, skipping Prometheus metrics/alert flow | 

### Return type

[**V1TriggerTestAlertResponse**](V1TriggerTestAlertResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

