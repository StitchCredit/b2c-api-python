# ecreditapi.DirectControllerApi

All URIs are relative to *http://localhost:8081/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_email**](DirectControllerApi.md#change_email) | **POST** /direct/change-email/{id} | 
[**change_host**](DirectControllerApi.md#change_host) | **POST** /direct/change-host/{id} | 
[**change_mobile**](DirectControllerApi.md#change_mobile) | **POST** /direct/change-mobile/{id} | 
[**close_account**](DirectControllerApi.md#close_account) | **POST** /direct/close-account/{id} | 
[**efx_alert**](DirectControllerApi.md#efx_alert) | **GET** /direct/efx-alert/{id} | 
[**efx_config**](DirectControllerApi.md#efx_config) | **GET** /direct/efx-config/{id} | 
[**efx_latest_efx_score**](DirectControllerApi.md#efx_latest_efx_score) | **GET** /direct/efx-latest-efx-score/{id} | 
[**efx_latest_report**](DirectControllerApi.md#efx_latest_report) | **GET** /direct/efx-latest-report/{id} | 
[**efx_latest_scores**](DirectControllerApi.md#efx_latest_scores) | **GET** /direct/efx-latest-scores/{id} | 
[**efx_score_history**](DirectControllerApi.md#efx_score_history) | **GET** /direct/efx-score-history/{id} | 
[**efx_scores**](DirectControllerApi.md#efx_scores) | **GET** /direct/efx-scores/{id} | 
[**get_user**](DirectControllerApi.md#get_user) | **GET** /direct/user/{id} | 
[**login**](DirectControllerApi.md#login) | **POST** /direct/login | 
[**preauth_token**](DirectControllerApi.md#preauth_token) | **GET** /direct/preauth-token/{id} | 
[**refresh_token**](DirectControllerApi.md#refresh_token) | **GET** /direct/refresh-token | 
[**register**](DirectControllerApi.md#register) | **POST** /direct/user-reg | 
[**register_old**](DirectControllerApi.md#register_old) | **POST** /direct/register | 
[**update_refresh**](DirectControllerApi.md#update_refresh) | **POST** /direct/update-refresh/{id} | 
[**user_token_old**](DirectControllerApi.md#user_token_old) | **GET** /direct/user-token/{id} | 


# **change_email**
> change_email(id, direct_change_email_req_dto)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import ecreditapi
from ecreditapi.rest import ApiException
from pprint import pprint
configuration = ecreditapi.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to http://localhost:8081/api
configuration.host = "http://localhost:8081/api"
# Enter a context with an instance of the API client
with ecreditapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecreditapi.DirectControllerApi(api_client)
    id = 'id_example' # str | 
direct_change_email_req_dto = ecreditapi.DirectChangeEmailReqDTO() # DirectChangeEmailReqDTO | 

    try:
        api_instance.change_email(id, direct_change_email_req_dto)
    except ApiException as e:
        print("Exception when calling DirectControllerApi->change_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **direct_change_email_req_dto** | [**DirectChangeEmailReqDTO**](DirectChangeEmailReqDTO.md)|  | 

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
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_host**
> change_host(id, host)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import ecreditapi
from ecreditapi.rest import ApiException
from pprint import pprint
configuration = ecreditapi.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to http://localhost:8081/api
configuration.host = "http://localhost:8081/api"
# Enter a context with an instance of the API client
with ecreditapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecreditapi.DirectControllerApi(api_client)
    id = 'id_example' # str | 
host = 'host_example' # str | 

    try:
        api_instance.change_host(id, host)
    except ApiException as e:
        print("Exception when calling DirectControllerApi->change_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **host** | **str**|  | 

### Return type

void (empty response body)

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
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_mobile**
> change_mobile(id, direct_change_mobile_req_dto)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import ecreditapi
from ecreditapi.rest import ApiException
from pprint import pprint
configuration = ecreditapi.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to http://localhost:8081/api
configuration.host = "http://localhost:8081/api"
# Enter a context with an instance of the API client
with ecreditapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecreditapi.DirectControllerApi(api_client)
    id = 'id_example' # str | 
direct_change_mobile_req_dto = ecreditapi.DirectChangeMobileReqDTO() # DirectChangeMobileReqDTO | 

    try:
        api_instance.change_mobile(id, direct_change_mobile_req_dto)
    except ApiException as e:
        print("Exception when calling DirectControllerApi->change_mobile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **direct_change_mobile_req_dto** | [**DirectChangeMobileReqDTO**](DirectChangeMobileReqDTO.md)|  | 

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
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_account**
> close_account(id)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import ecreditapi
from ecreditapi.rest import ApiException
from pprint import pprint
configuration = ecreditapi.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to http://localhost:8081/api
configuration.host = "http://localhost:8081/api"
# Enter a context with an instance of the API client
with ecreditapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecreditapi.DirectControllerApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.close_account(id)
    except ApiException as e:
        print("Exception when calling DirectControllerApi->close_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

void (empty response body)

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
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **efx_alert**
> AlertRespDTO efx_alert(id)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import ecreditapi
from ecreditapi.rest import ApiException
from pprint import pprint
configuration = ecreditapi.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to http://localhost:8081/api
configuration.host = "http://localhost:8081/api"
# Enter a context with an instance of the API client
with ecreditapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecreditapi.DirectControllerApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.efx_alert(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DirectControllerApi->efx_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**AlertRespDTO**](AlertRespDTO.md)

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
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **efx_config**
> EfxConfigRespDTO efx_config(id)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import ecreditapi
from ecreditapi.rest import ApiException
from pprint import pprint
configuration = ecreditapi.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to http://localhost:8081/api
configuration.host = "http://localhost:8081/api"
# Enter a context with an instance of the API client
with ecreditapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecreditapi.DirectControllerApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.efx_config(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DirectControllerApi->efx_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

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
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **efx_latest_efx_score**
> LatestScore efx_latest_efx_score(id)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import ecreditapi
from ecreditapi.rest import ApiException
from pprint import pprint
configuration = ecreditapi.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to http://localhost:8081/api
configuration.host = "http://localhost:8081/api"
# Enter a context with an instance of the API client
with ecreditapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecreditapi.DirectControllerApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.efx_latest_efx_score(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DirectControllerApi->efx_latest_efx_score: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

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
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **efx_latest_report**
> CreditReport efx_latest_report(id)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import ecreditapi
from ecreditapi.rest import ApiException
from pprint import pprint
configuration = ecreditapi.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to http://localhost:8081/api
configuration.host = "http://localhost:8081/api"
# Enter a context with an instance of the API client
with ecreditapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecreditapi.DirectControllerApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.efx_latest_report(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DirectControllerApi->efx_latest_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**CreditReport**](CreditReport.md)

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
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **efx_latest_scores**
> list[LatestScore] efx_latest_scores(id)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import ecreditapi
from ecreditapi.rest import ApiException
from pprint import pprint
configuration = ecreditapi.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to http://localhost:8081/api
configuration.host = "http://localhost:8081/api"
# Enter a context with an instance of the API client
with ecreditapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecreditapi.DirectControllerApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.efx_latest_scores(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DirectControllerApi->efx_latest_scores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

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
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **efx_score_history**
> list[HistoricalScore] efx_score_history(id)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import ecreditapi
from ecreditapi.rest import ApiException
from pprint import pprint
configuration = ecreditapi.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to http://localhost:8081/api
configuration.host = "http://localhost:8081/api"
# Enter a context with an instance of the API client
with ecreditapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecreditapi.DirectControllerApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.efx_score_history(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DirectControllerApi->efx_score_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

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
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **efx_scores**
> list[CreditScore] efx_scores(id)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import ecreditapi
from ecreditapi.rest import ApiException
from pprint import pprint
configuration = ecreditapi.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to http://localhost:8081/api
configuration.host = "http://localhost:8081/api"
# Enter a context with an instance of the API client
with ecreditapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecreditapi.DirectControllerApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.efx_scores(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DirectControllerApi->efx_scores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

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
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserRespDTO get_user(id)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import ecreditapi
from ecreditapi.rest import ApiException
from pprint import pprint
configuration = ecreditapi.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to http://localhost:8081/api
configuration.host = "http://localhost:8081/api"
# Enter a context with an instance of the API client
with ecreditapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecreditapi.DirectControllerApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_user(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DirectControllerApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**UserRespDTO**](UserRespDTO.md)

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
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> LoginRespDTO login(direct_login_req_dto)



### Example

```python
from __future__ import print_function
import time
import ecreditapi
from ecreditapi.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with ecreditapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ecreditapi.DirectControllerApi(api_client)
    direct_login_req_dto = ecreditapi.DirectLoginReqDTO() # DirectLoginReqDTO | 

    try:
        api_response = api_instance.login(direct_login_req_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DirectControllerApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direct_login_req_dto** | [**DirectLoginReqDTO**](DirectLoginReqDTO.md)|  | 

### Return type

[**LoginRespDTO**](LoginRespDTO.md)

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
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preauth_token**
> PreauthTokenDTO preauth_token(id)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import ecreditapi
from ecreditapi.rest import ApiException
from pprint import pprint
configuration = ecreditapi.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to http://localhost:8081/api
configuration.host = "http://localhost:8081/api"
# Enter a context with an instance of the API client
with ecreditapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecreditapi.DirectControllerApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.preauth_token(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DirectControllerApi->preauth_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**PreauthTokenDTO**](PreauthTokenDTO.md)

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
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_token**
> LoginRespDTO refresh_token(token=token)



### Example

```python
from __future__ import print_function
import time
import ecreditapi
from ecreditapi.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with ecreditapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ecreditapi.DirectControllerApi(api_client)
    token = 'token_example' # str |  (optional)

    try:
        api_response = api_instance.refresh_token(token=token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DirectControllerApi->refresh_token: %s\n" % e)
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
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register**
> PreauthTokenDTO register(direct_user_reg_req_dto)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import ecreditapi
from ecreditapi.rest import ApiException
from pprint import pprint
configuration = ecreditapi.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to http://localhost:8081/api
configuration.host = "http://localhost:8081/api"
# Enter a context with an instance of the API client
with ecreditapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecreditapi.DirectControllerApi(api_client)
    direct_user_reg_req_dto = ecreditapi.DirectUserRegReqDTO() # DirectUserRegReqDTO | 

    try:
        api_response = api_instance.register(direct_user_reg_req_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DirectControllerApi->register: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direct_user_reg_req_dto** | [**DirectUserRegReqDTO**](DirectUserRegReqDTO.md)|  | 

### Return type

[**PreauthTokenDTO**](PreauthTokenDTO.md)

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
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_old**
> UserLoginRespDTO register_old(direct_user_reg_req_dto)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import ecreditapi
from ecreditapi.rest import ApiException
from pprint import pprint
configuration = ecreditapi.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to http://localhost:8081/api
configuration.host = "http://localhost:8081/api"
# Enter a context with an instance of the API client
with ecreditapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecreditapi.DirectControllerApi(api_client)
    direct_user_reg_req_dto = ecreditapi.DirectUserRegReqDTO() # DirectUserRegReqDTO | 

    try:
        api_response = api_instance.register_old(direct_user_reg_req_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DirectControllerApi->register_old: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direct_user_reg_req_dto** | [**DirectUserRegReqDTO**](DirectUserRegReqDTO.md)|  | 

### Return type

[**UserLoginRespDTO**](UserLoginRespDTO.md)

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
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_refresh**
> update_refresh(id, rmonly)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import ecreditapi
from ecreditapi.rest import ApiException
from pprint import pprint
configuration = ecreditapi.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to http://localhost:8081/api
configuration.host = "http://localhost:8081/api"
# Enter a context with an instance of the API client
with ecreditapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecreditapi.DirectControllerApi(api_client)
    id = 'id_example' # str | 
rmonly = True # bool | 

    try:
        api_instance.update_refresh(id, rmonly)
    except ApiException as e:
        print("Exception when calling DirectControllerApi->update_refresh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **rmonly** | **bool**|  | 

### Return type

void (empty response body)

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
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_token_old**
> UserLoginRespDTO user_token_old(id)



### Example

* Bearer (JWT) Authentication (accessToken):
```python
from __future__ import print_function
import time
import ecreditapi
from ecreditapi.rest import ApiException
from pprint import pprint
configuration = ecreditapi.Configuration()
# Configure Bearer authorization (JWT): accessToken
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to http://localhost:8081/api
configuration.host = "http://localhost:8081/api"
# Enter a context with an instance of the API client
with ecreditapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecreditapi.DirectControllerApi(api_client)
    id = 'id_example' # str | UserId to generate preauth token for

    try:
        api_response = api_instance.user_token_old(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DirectControllerApi->user_token_old: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| UserId to generate preauth token for | 

### Return type

[**UserLoginRespDTO**](UserLoginRespDTO.md)

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
**500** | Internal Server Error |  -  |
**401** | Access Denied |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

