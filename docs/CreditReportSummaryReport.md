# CreditReportSummaryReport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**report_generated** | **datetime** |  | [optional] 
**credit_file_security_freeze_flag** | **bool** |  | [optional] 
**report_type** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**subject** | [**PersonSubjectReport**](PersonSubjectReport.md) |  | [optional] 
**credit_score** | [**CreditScoreReport**](CreditScoreReport.md) |  | [optional] 
**revolving_accounts** | [**CreditReportSummaryAccountsReport**](CreditReportSummaryAccountsReport.md) |  | [optional] 
**mortgage_accounts** | [**CreditReportSummaryAccountsReport**](CreditReportSummaryAccountsReport.md) |  | [optional] 
**installment_accounts** | [**CreditReportSummaryAccountsReport**](CreditReportSummaryAccountsReport.md) |  | [optional] 
**other_accounts** | [**CreditReportSummaryAccountsReport**](CreditReportSummaryAccountsReport.md) |  | [optional] 
**total_open_accounts** | [**CreditReportSummaryAccountsReport**](CreditReportSummaryAccountsReport.md) |  | [optional] 
**length_of_credit_history_months** | **int** |  | [optional] 
**total_negative_accounts** | **int** |  | [optional] 
**average_account_age_months** | **int** |  | [optional] 
**oldest_account_open_date** | **datetime** |  | [optional] 
**oldest_account_name** | **str** |  | [optional] 
**most_recent_account_open_date** | **datetime** |  | [optional] 
**most_recent_account_name** | **str** |  | [optional] 
**total_consumer_statements** | **int** |  | [optional] 
**most_recent_inquiry_date** | **datetime** |  | [optional] 
**most_recent_inquiry_name** | **str** |  | [optional] 
**total_personal_information** | **int** |  | [optional] 
**total_inquires** | **int** |  | [optional] 
**total_public_records** | **int** |  | [optional] 
**total_collections** | **int** |  | [optional] 
**dispute_information** | [**CreditReportProviderDisputeInformationReport**](CreditReportProviderDisputeInformationReport.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


