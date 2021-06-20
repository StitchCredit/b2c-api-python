# ecreditapi
StitchCredit API

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.3
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import ecreditapi
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ecreditapi
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import ecreditapi
from pprint import pprint
from ecreditapi.api import direct_controller_api
from ecreditapi.model.alert_resp_dto import AlertRespDTO
from ecreditapi.model.credit_report import CreditReport
from ecreditapi.model.credit_score import CreditScore
from ecreditapi.model.credit_score_abstract import CreditScoreAbstract
from ecreditapi.model.credit_score_history import CreditScoreHistory
from ecreditapi.model.direct_change_email_req_dto import DirectChangeEmailReqDTO
from ecreditapi.model.direct_change_mobile_req_dto import DirectChangeMobileReqDTO
from ecreditapi.model.direct_login_req_dto import DirectLoginReqDTO
from ecreditapi.model.direct_user_reg_req_dto import DirectUserRegReqDTO
from ecreditapi.model.efx_config_resp_dto import EfxConfigRespDTO
from ecreditapi.model.login_resp_dto import LoginRespDTO
from ecreditapi.model.preauth_token_dto import PreauthTokenDTO
from ecreditapi.model.user_login_resp_dto import UserLoginRespDTO
from ecreditapi.model.user_resp_dto import UserRespDTO
# Defining the host is optional and defaults to http://localhost:8081/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecreditapi.Configuration(
    host = "http://localhost:8081/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): accessToken
configuration = ecreditapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)


# Enter a context with an instance of the API client
with ecreditapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = direct_controller_api.DirectControllerApi(api_client)
    id = "id_example" # str | 
direct_change_email_req_dto = DirectChangeEmailReqDTO(
        email="email_example",
    ) # DirectChangeEmailReqDTO | 

    try:
        api_instance.change_email(id, direct_change_email_req_dto)
    except ecreditapi.ApiException as e:
        print("Exception when calling DirectControllerApi->change_email: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8081/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DirectControllerApi* | [**change_email**](docs/DirectControllerApi.md#change_email) | **POST** /direct/change-email/{id} | 
*DirectControllerApi* | [**change_host**](docs/DirectControllerApi.md#change_host) | **POST** /direct/change-host/{id} | 
*DirectControllerApi* | [**change_mobile**](docs/DirectControllerApi.md#change_mobile) | **POST** /direct/change-mobile/{id} | 
*DirectControllerApi* | [**close_account**](docs/DirectControllerApi.md#close_account) | **POST** /direct/close-account/{id} | 
*DirectControllerApi* | [**efx_alert**](docs/DirectControllerApi.md#efx_alert) | **GET** /direct/efx-alert/{id} | 
*DirectControllerApi* | [**efx_config**](docs/DirectControllerApi.md#efx_config) | **GET** /direct/efx-config/{id} | 
*DirectControllerApi* | [**efx_latest_efx_score**](docs/DirectControllerApi.md#efx_latest_efx_score) | **GET** /direct/efx-latest-efx-score/{id} | 
*DirectControllerApi* | [**efx_latest_report**](docs/DirectControllerApi.md#efx_latest_report) | **GET** /direct/efx-latest-report/{id} | 
*DirectControllerApi* | [**efx_latest_scores**](docs/DirectControllerApi.md#efx_latest_scores) | **GET** /direct/efx-latest-scores/{id} | 
*DirectControllerApi* | [**efx_score_history**](docs/DirectControllerApi.md#efx_score_history) | **GET** /direct/efx-score-history/{id} | 
*DirectControllerApi* | [**efx_scores**](docs/DirectControllerApi.md#efx_scores) | **GET** /direct/efx-scores/{id} | 
*DirectControllerApi* | [**get_user**](docs/DirectControllerApi.md#get_user) | **GET** /direct/user/{id} | 
*DirectControllerApi* | [**login**](docs/DirectControllerApi.md#login) | **POST** /direct/login | 
*DirectControllerApi* | [**preauth_token**](docs/DirectControllerApi.md#preauth_token) | **GET** /direct/preauth-token/{id} | 
*DirectControllerApi* | [**refresh_token**](docs/DirectControllerApi.md#refresh_token) | **GET** /direct/refresh-token | 
*DirectControllerApi* | [**register**](docs/DirectControllerApi.md#register) | **POST** /direct/user-reg | 
*DirectControllerApi* | [**register_old**](docs/DirectControllerApi.md#register_old) | **POST** /direct/register | 
*DirectControllerApi* | [**update_refresh**](docs/DirectControllerApi.md#update_refresh) | **POST** /direct/update-refresh/{id} | 
*DirectControllerApi* | [**user_token_old**](docs/DirectControllerApi.md#user_token_old) | **GET** /direct/user-token/{id} | 


## Documentation For Models

 - [AlertRespDTO](docs/AlertRespDTO.md)
 - [Bankruptcy](docs/Bankruptcy.md)
 - [CodeDescription](docs/CodeDescription.md)
 - [CollectionItem](docs/CollectionItem.md)
 - [ConsumerStatement](docs/ConsumerStatement.md)
 - [ContactInformation](docs/ContactInformation.md)
 - [Country](docs/Country.md)
 - [CreditReport](docs/CreditReport.md)
 - [CreditReportAccount](docs/CreditReportAccount.md)
 - [CreditReportProviderDisputeInformation](docs/CreditReportProviderDisputeInformation.md)
 - [CreditReportProviderView](docs/CreditReportProviderView.md)
 - [CreditReportSummary](docs/CreditReportSummary.md)
 - [CreditReportSummaryAccounts](docs/CreditReportSummaryAccounts.md)
 - [CreditScore](docs/CreditScore.md)
 - [CreditScoreAbstract](docs/CreditScoreAbstract.md)
 - [CreditScoreHistory](docs/CreditScoreHistory.md)
 - [CreditScoreHistoryProviderView](docs/CreditScoreHistoryProviderView.md)
 - [CreditScoreLoanRiskRange](docs/CreditScoreLoanRiskRange.md)
 - [CreditScoreProviderView](docs/CreditScoreProviderView.md)
 - [CreditScoreRange](docs/CreditScoreRange.md)
 - [CreditScoreReason](docs/CreditScoreReason.md)
 - [DirectChangeEmailReqDTO](docs/DirectChangeEmailReqDTO.md)
 - [DirectChangeMobileReqDTO](docs/DirectChangeMobileReqDTO.md)
 - [DirectLoginReqDTO](docs/DirectLoginReqDTO.md)
 - [DirectUserRegReqDTO](docs/DirectUserRegReqDTO.md)
 - [EfxConfigRespDTO](docs/EfxConfigRespDTO.md)
 - [Employer](docs/Employer.md)
 - [Inquiry](docs/Inquiry.md)
 - [InternationalAddress](docs/InternationalAddress.md)
 - [InternationalPhone](docs/InternationalPhone.md)
 - [Judgment](docs/Judgment.md)
 - [Lien](docs/Lien.md)
 - [LoginRespDTO](docs/LoginRespDTO.md)
 - [Money](docs/Money.md)
 - [PaymentHistoryMonth](docs/PaymentHistoryMonth.md)
 - [PaymentHistoryYear](docs/PaymentHistoryYear.md)
 - [PersonName](docs/PersonName.md)
 - [PersonSubject](docs/PersonSubject.md)
 - [PreauthTokenDTO](docs/PreauthTokenDTO.md)
 - [PublicRecords](docs/PublicRecords.md)
 - [TrendedData](docs/TrendedData.md)
 - [TrendedDataHistory](docs/TrendedDataHistory.md)
 - [TrendedDataYear](docs/TrendedDataYear.md)
 - [UserLoginRespDTO](docs/UserLoginRespDTO.md)
 - [UserRespDTO](docs/UserRespDTO.md)


## Documentation For Authorization


## accessToken

- **Type**: Bearer authentication (JWT)


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in ecreditapi.apis and ecreditapi.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from ecreditapi.api.default_api import DefaultApi`
- `from ecreditapi.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import ecreditapi
from ecreditapi.apis import *
from ecreditapi.models import *
```

