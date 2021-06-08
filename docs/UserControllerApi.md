# sc-direct-api.UserControllerApi

All URIs are relative to *https://efx-wgt.stitchcredit.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_notifications**](UserControllerApi.md#change_notifications) | **POST** /users/change-notifications | 
[**change_password**](UserControllerApi.md#change_password) | **POST** /users/change-password | 
[**change_recovery**](UserControllerApi.md#change_recovery) | **POST** /users/change-recovery | 
[**change_user_email**](UserControllerApi.md#change_user_email) | **POST** /users/change-email | 
[**close_user_account**](UserControllerApi.md#close_user_account) | **POST** /users/close-account | 
[**exchange_preauth_token**](UserControllerApi.md#exchange_preauth_token) | **GET** /users/preauth-token/{token} | 
[**get_action_token**](UserControllerApi.md#get_action_token) | **POST** /users/action-token | 
[**get_efx_config**](UserControllerApi.md#get_efx_config) | **GET** /users/efx-config | 
[**get_efx_latest_efx_score**](UserControllerApi.md#get_efx_latest_efx_score) | **GET** /users/efx-latest-efx-score | 
[**get_efx_latest_scores**](UserControllerApi.md#get_efx_latest_scores) | **GET** /users/efx-latest-scores | 
[**get_efx_score_history**](UserControllerApi.md#get_efx_score_history) | **GET** /users/efx-score-history | 
[**get_efx_scores**](UserControllerApi.md#get_efx_scores) | **GET** /users/efx-scores | 
[**get_identity_quiz**](UserControllerApi.md#get_identity_quiz) | **GET** /users/get-quiz | 
[**get_mobile_authorization**](UserControllerApi.md#get_mobile_authorization) | **GET** /users/get-mobile | 
[**get_user**](UserControllerApi.md#get_user) | **GET** /users | 
[**initialize**](UserControllerApi.md#initialize) | **GET** /users/initialize | 
[**initialize_with_key**](UserControllerApi.md#initialize_with_key) | **GET** /users/initialize/{key} | 
[**login_user**](UserControllerApi.md#login_user) | **POST** /users/login | 
[**recover_password**](UserControllerApi.md#recover_password) | **POST** /users/password-recovery | 
[**recovery_question**](UserControllerApi.md#recovery_question) | **POST** /users/recovery-token | 
[**refresh_user_token**](UserControllerApi.md#refresh_user_token) | **GET** /users/refresh-token | 
[**register_user**](UserControllerApi.md#register_user) | **POST** /users/register | 
[**renew_mobile_code**](UserControllerApi.md#renew_mobile_code) | **POST** /users/renew-code | 
[**reset_password**](UserControllerApi.md#reset_password) | **POST** /users/password-reset | 
[**send_mobile_code**](UserControllerApi.md#send_mobile_code) | **POST** /users/send-code/{token} | 
[**set_identity**](UserControllerApi.md#set_identity) | **POST** /users/identity | 
[**start_user_session**](UserControllerApi.md#start_user_session) | **GET** /users/start | 
[**verify_identity_quiz**](UserControllerApi.md#verify_identity_quiz) | **POST** /users/verify-quiz | 
[**verify_mobile_code**](UserControllerApi.md#verify_mobile_code) | **POST** /users/verify-code | 


# **change_notifications**
> UserRespDTO change_notifications(user_notifications_pref)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint
configuration = sc-direct-api.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://efx-wgt.stitchcredit.com/api
configuration.host = "https://efx-wgt.stitchcredit.com/api"
# Enter a context with an instance of the API client
with sc-direct-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    user_notifications_pref = sc-direct-api.UserNotificationsPref() # UserNotificationsPref | 

    try:
        api_response = api_instance.change_notifications(user_notifications_pref)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserControllerApi->change_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_notifications_pref** | [**UserNotificationsPref**](UserNotificationsPref.md)|  | 

### Return type

[**UserRespDTO**](UserRespDTO.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_password**
> change_password(change_password_req_dto)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint
configuration = sc-direct-api.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://efx-wgt.stitchcredit.com/api
configuration.host = "https://efx-wgt.stitchcredit.com/api"
# Enter a context with an instance of the API client
with sc-direct-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    change_password_req_dto = sc-direct-api.ChangePasswordReqDTO() # ChangePasswordReqDTO | 

    try:
        api_instance.change_password(change_password_req_dto)
    except ApiException as e:
        print("Exception when calling UserControllerApi->change_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_password_req_dto** | [**ChangePasswordReqDTO**](ChangePasswordReqDTO.md)|  | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_recovery**
> change_recovery(change_recovery_req_dto)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint
configuration = sc-direct-api.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://efx-wgt.stitchcredit.com/api
configuration.host = "https://efx-wgt.stitchcredit.com/api"
# Enter a context with an instance of the API client
with sc-direct-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    change_recovery_req_dto = sc-direct-api.ChangeRecoveryReqDTO() # ChangeRecoveryReqDTO | 

    try:
        api_instance.change_recovery(change_recovery_req_dto)
    except ApiException as e:
        print("Exception when calling UserControllerApi->change_recovery: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_recovery_req_dto** | [**ChangeRecoveryReqDTO**](ChangeRecoveryReqDTO.md)|  | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user_email**
> change_user_email(change_email_req_dto)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint
configuration = sc-direct-api.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://efx-wgt.stitchcredit.com/api
configuration.host = "https://efx-wgt.stitchcredit.com/api"
# Enter a context with an instance of the API client
with sc-direct-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    change_email_req_dto = sc-direct-api.ChangeEmailReqDTO() # ChangeEmailReqDTO | 

    try:
        api_instance.change_user_email(change_email_req_dto)
    except ApiException as e:
        print("Exception when calling UserControllerApi->change_user_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_email_req_dto** | [**ChangeEmailReqDTO**](ChangeEmailReqDTO.md)|  | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_user_account**
> close_user_account(close_account_req_dto)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint
configuration = sc-direct-api.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://efx-wgt.stitchcredit.com/api
configuration.host = "https://efx-wgt.stitchcredit.com/api"
# Enter a context with an instance of the API client
with sc-direct-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    close_account_req_dto = sc-direct-api.CloseAccountReqDTO() # CloseAccountReqDTO | 

    try:
        api_instance.close_user_account(close_account_req_dto)
    except ApiException as e:
        print("Exception when calling UserControllerApi->close_user_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **close_account_req_dto** | [**CloseAccountReqDTO**](CloseAccountReqDTO.md)|  | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchange_preauth_token**
> UserLoginRespDTO exchange_preauth_token(token)



### Example

```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with sc-direct-api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    token = 'token_example' # str | 

    try:
        api_response = api_instance.exchange_preauth_token(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserControllerApi->exchange_preauth_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**UserLoginRespDTO**](UserLoginRespDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_action_token**
> ActionTokenRespDTO get_action_token(login_req_dto)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint
configuration = sc-direct-api.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://efx-wgt.stitchcredit.com/api
configuration.host = "https://efx-wgt.stitchcredit.com/api"
# Enter a context with an instance of the API client
with sc-direct-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    login_req_dto = sc-direct-api.LoginReqDTO() # LoginReqDTO | 

    try:
        api_response = api_instance.get_action_token(login_req_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserControllerApi->get_action_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_req_dto** | [**LoginReqDTO**](LoginReqDTO.md)|  | 

### Return type

[**ActionTokenRespDTO**](ActionTokenRespDTO.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_efx_config**
> EfxConfigRespDTO get_efx_config()



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint
configuration = sc-direct-api.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://efx-wgt.stitchcredit.com/api
configuration.host = "https://efx-wgt.stitchcredit.com/api"
# Enter a context with an instance of the API client
with sc-direct-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    
    try:
        api_response = api_instance.get_efx_config()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserControllerApi->get_efx_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EfxConfigRespDTO**](EfxConfigRespDTO.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_efx_latest_efx_score**
> LatestScore get_efx_latest_efx_score()



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint
configuration = sc-direct-api.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://efx-wgt.stitchcredit.com/api
configuration.host = "https://efx-wgt.stitchcredit.com/api"
# Enter a context with an instance of the API client
with sc-direct-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    
    try:
        api_response = api_instance.get_efx_latest_efx_score()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserControllerApi->get_efx_latest_efx_score: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LatestScore**](LatestScore.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_efx_latest_scores**
> list[LatestScore] get_efx_latest_scores()



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint
configuration = sc-direct-api.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://efx-wgt.stitchcredit.com/api
configuration.host = "https://efx-wgt.stitchcredit.com/api"
# Enter a context with an instance of the API client
with sc-direct-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    
    try:
        api_response = api_instance.get_efx_latest_scores()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserControllerApi->get_efx_latest_scores: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LatestScore]**](LatestScore.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_efx_score_history**
> list[HistoricalScore] get_efx_score_history()



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint
configuration = sc-direct-api.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://efx-wgt.stitchcredit.com/api
configuration.host = "https://efx-wgt.stitchcredit.com/api"
# Enter a context with an instance of the API client
with sc-direct-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    
    try:
        api_response = api_instance.get_efx_score_history()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserControllerApi->get_efx_score_history: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[HistoricalScore]**](HistoricalScore.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_efx_scores**
> list[CreditScore] get_efx_scores()



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint
configuration = sc-direct-api.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://efx-wgt.stitchcredit.com/api
configuration.host = "https://efx-wgt.stitchcredit.com/api"
# Enter a context with an instance of the API client
with sc-direct-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    
    try:
        api_response = api_instance.get_efx_scores()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserControllerApi->get_efx_scores: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CreditScore]**](CreditScore.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_quiz**
> IdentityQuizDTO get_identity_quiz()



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint
configuration = sc-direct-api.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://efx-wgt.stitchcredit.com/api
configuration.host = "https://efx-wgt.stitchcredit.com/api"
# Enter a context with an instance of the API client
with sc-direct-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    
    try:
        api_response = api_instance.get_identity_quiz()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserControllerApi->get_identity_quiz: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IdentityQuizDTO**](IdentityQuizDTO.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mobile_authorization**
> IdentityMobileRespDTO get_mobile_authorization()



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint
configuration = sc-direct-api.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://efx-wgt.stitchcredit.com/api
configuration.host = "https://efx-wgt.stitchcredit.com/api"
# Enter a context with an instance of the API client
with sc-direct-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    
    try:
        api_response = api_instance.get_mobile_authorization()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserControllerApi->get_mobile_authorization: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IdentityMobileRespDTO**](IdentityMobileRespDTO.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserRespDTO get_user()



### Example

```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with sc-direct-api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    
    try:
        api_response = api_instance.get_user()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserControllerApi->get_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserRespDTO**](UserRespDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialize**
> UserConfigDTO initialize(referer=referer, ctoken=ctoken)



### Example

```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with sc-direct-api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    referer = 'referer_example' # str |  (optional)
ctoken = 'ctoken_example' # str |  (optional)

    try:
        api_response = api_instance.initialize(referer=referer, ctoken=ctoken)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserControllerApi->initialize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **referer** | **str**|  | [optional] 
 **ctoken** | **str**|  | [optional] 

### Return type

[**UserConfigDTO**](UserConfigDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialize_with_key**
> UserConfigDTO initialize_with_key(key)



### Example

```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with sc-direct-api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    key = 'key_example' # str | 

    try:
        api_response = api_instance.initialize_with_key(key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserControllerApi->initialize_with_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | [**str**](.md)|  | 

### Return type

[**UserConfigDTO**](UserConfigDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_user**
> UserLoginRespDTO login_user(login_req_dto, referer=referer, ctoken=ctoken)



### Example

```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with sc-direct-api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    login_req_dto = sc-direct-api.LoginReqDTO() # LoginReqDTO | 
referer = 'referer_example' # str |  (optional)
ctoken = 'ctoken_example' # str |  (optional)

    try:
        api_response = api_instance.login_user(login_req_dto, referer=referer, ctoken=ctoken)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserControllerApi->login_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_req_dto** | [**LoginReqDTO**](LoginReqDTO.md)|  | 
 **referer** | **str**|  | [optional] 
 **ctoken** | **str**|  | [optional] 

### Return type

[**UserLoginRespDTO**](UserLoginRespDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recover_password**
> recover_password(password_recovery_req_dto, referer=referer, ctoken=ctoken)



### Example

```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with sc-direct-api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    password_recovery_req_dto = sc-direct-api.PasswordRecoveryReqDTO() # PasswordRecoveryReqDTO | 
referer = 'referer_example' # str |  (optional)
ctoken = 'ctoken_example' # str |  (optional)

    try:
        api_instance.recover_password(password_recovery_req_dto, referer=referer, ctoken=ctoken)
    except ApiException as e:
        print("Exception when calling UserControllerApi->recover_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_recovery_req_dto** | [**PasswordRecoveryReqDTO**](PasswordRecoveryReqDTO.md)|  | 
 **referer** | **str**|  | [optional] 
 **ctoken** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recovery_question**
> ActionTokenRespDTO recovery_question(token_req_dto)



### Example

```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with sc-direct-api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    token_req_dto = sc-direct-api.TokenReqDTO() # TokenReqDTO | 

    try:
        api_response = api_instance.recovery_question(token_req_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserControllerApi->recovery_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_req_dto** | [**TokenReqDTO**](TokenReqDTO.md)|  | 

### Return type

[**ActionTokenRespDTO**](ActionTokenRespDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_user_token**
> LoginRespDTO refresh_user_token(token=token)



### Example

```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with sc-direct-api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    token = 'token_example' # str |  (optional)

    try:
        api_response = api_instance.refresh_user_token(token=token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserControllerApi->refresh_user_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | [optional] 

### Return type

[**LoginRespDTO**](LoginRespDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_user**
> UserLoginRespDTO register_user(user_reg_req_dto, referer=referer, ctoken=ctoken)



### Example

```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with sc-direct-api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    user_reg_req_dto = sc-direct-api.UserRegReqDTO() # UserRegReqDTO | 
referer = 'referer_example' # str |  (optional)
ctoken = 'ctoken_example' # str |  (optional)

    try:
        api_response = api_instance.register_user(user_reg_req_dto, referer=referer, ctoken=ctoken)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserControllerApi->register_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_reg_req_dto** | [**UserRegReqDTO**](UserRegReqDTO.md)|  | 
 **referer** | **str**|  | [optional] 
 **ctoken** | **str**|  | [optional] 

### Return type

[**UserLoginRespDTO**](UserLoginRespDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **renew_mobile_code**
> UserOtpRespDTO renew_mobile_code(user_renew_otp_req_dto)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint
configuration = sc-direct-api.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://efx-wgt.stitchcredit.com/api
configuration.host = "https://efx-wgt.stitchcredit.com/api"
# Enter a context with an instance of the API client
with sc-direct-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    user_renew_otp_req_dto = sc-direct-api.UserRenewOtpReqDTO() # UserRenewOtpReqDTO | 

    try:
        api_response = api_instance.renew_mobile_code(user_renew_otp_req_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserControllerApi->renew_mobile_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_renew_otp_req_dto** | [**UserRenewOtpReqDTO**](UserRenewOtpReqDTO.md)|  | 

### Return type

[**UserOtpRespDTO**](UserOtpRespDTO.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> reset_password(password_reset_req_dto)



### Example

```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with sc-direct-api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    password_reset_req_dto = sc-direct-api.PasswordResetReqDTO() # PasswordResetReqDTO | 

    try:
        api_instance.reset_password(password_reset_req_dto)
    except ApiException as e:
        print("Exception when calling UserControllerApi->reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_reset_req_dto** | [**PasswordResetReqDTO**](PasswordResetReqDTO.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_mobile_code**
> UserOtpRespDTO send_mobile_code(token)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint
configuration = sc-direct-api.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://efx-wgt.stitchcredit.com/api
configuration.host = "https://efx-wgt.stitchcredit.com/api"
# Enter a context with an instance of the API client
with sc-direct-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    token = 'token_example' # str | 

    try:
        api_response = api_instance.send_mobile_code(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserControllerApi->send_mobile_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**UserOtpRespDTO**](UserOtpRespDTO.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_identity**
> UserRespDTO set_identity(identity_req_dto)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint
configuration = sc-direct-api.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://efx-wgt.stitchcredit.com/api
configuration.host = "https://efx-wgt.stitchcredit.com/api"
# Enter a context with an instance of the API client
with sc-direct-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    identity_req_dto = sc-direct-api.IdentityReqDTO() # IdentityReqDTO | 

    try:
        api_response = api_instance.set_identity(identity_req_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserControllerApi->set_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_req_dto** | [**IdentityReqDTO**](IdentityReqDTO.md)|  | 

### Return type

[**UserRespDTO**](UserRespDTO.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_user_session**
> RedirectView start_user_session(referer=referer, key=key, ocf=ocf, oct=oct)



### Example

```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with sc-direct-api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    referer = 'referer_example' # str |  (optional)
key = 'key_example' # str |  (optional)
ocf = 'ocf_example' # str |  (optional)
oct = 'oct_example' # str |  (optional)

    try:
        api_response = api_instance.start_user_session(referer=referer, key=key, ocf=ocf, oct=oct)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserControllerApi->start_user_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **referer** | **str**|  | [optional] 
 **key** | **str**|  | [optional] 
 **ocf** | **str**|  | [optional] 
 **oct** | **str**|  | [optional] 

### Return type

[**RedirectView**](RedirectView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_identity_quiz**
> UserRespDTO verify_identity_quiz(identity_quiz_req_dto)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint
configuration = sc-direct-api.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://efx-wgt.stitchcredit.com/api
configuration.host = "https://efx-wgt.stitchcredit.com/api"
# Enter a context with an instance of the API client
with sc-direct-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    identity_quiz_req_dto = sc-direct-api.IdentityQuizReqDTO() # IdentityQuizReqDTO | 

    try:
        api_response = api_instance.verify_identity_quiz(identity_quiz_req_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserControllerApi->verify_identity_quiz: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_quiz_req_dto** | [**IdentityQuizReqDTO**](IdentityQuizReqDTO.md)|  | 

### Return type

[**UserRespDTO**](UserRespDTO.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_mobile_code**
> UserRespDTO verify_mobile_code(user_otp_req_dto)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import sc-direct-api
from sc-direct-api.rest import ApiException
from pprint import pprint
configuration = sc-direct-api.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://efx-wgt.stitchcredit.com/api
configuration.host = "https://efx-wgt.stitchcredit.com/api"
# Enter a context with an instance of the API client
with sc-direct-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sc-direct-api.UserControllerApi(api_client)
    user_otp_req_dto = sc-direct-api.UserOtpReqDTO() # UserOtpReqDTO | 

    try:
        api_response = api_instance.verify_mobile_code(user_otp_req_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserControllerApi->verify_mobile_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_otp_req_dto** | [**UserOtpReqDTO**](UserOtpReqDTO.md)|  | 

### Return type

[**UserRespDTO**](UserRespDTO.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

