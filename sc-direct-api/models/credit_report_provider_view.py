# coding: utf-8

"""
    StitchCredit API

    StitchCredit API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from sc-direct-api.configuration import Configuration


class CreditReportProviderView(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'provider': 'str',
        'summary': 'CreditReportSummary',
        'revolving_accounts': 'list[CreditReportAccount]',
        'mortgage_accounts': 'list[CreditReportAccount]',
        'installment_accounts': 'list[CreditReportAccount]',
        'other_accounts': 'list[CreditReportAccount]',
        'inquiries': 'list[Inquiry]',
        'consumer_statements': 'list[ConsumerStatement]',
        'public_records': 'PublicRecords',
        'collections': 'list[CollectionItem]'
    }

    attribute_map = {
        'provider': 'provider',
        'summary': 'summary',
        'revolving_accounts': 'revolvingAccounts',
        'mortgage_accounts': 'mortgageAccounts',
        'installment_accounts': 'installmentAccounts',
        'other_accounts': 'otherAccounts',
        'inquiries': 'inquiries',
        'consumer_statements': 'consumerStatements',
        'public_records': 'publicRecords',
        'collections': 'collections'
    }

    def __init__(self, provider=None, summary=None, revolving_accounts=None, mortgage_accounts=None, installment_accounts=None, other_accounts=None, inquiries=None, consumer_statements=None, public_records=None, collections=None, local_vars_configuration=None):  # noqa: E501
        """CreditReportProviderView - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._provider = None
        self._summary = None
        self._revolving_accounts = None
        self._mortgage_accounts = None
        self._installment_accounts = None
        self._other_accounts = None
        self._inquiries = None
        self._consumer_statements = None
        self._public_records = None
        self._collections = None
        self.discriminator = None

        if provider is not None:
            self.provider = provider
        if summary is not None:
            self.summary = summary
        if revolving_accounts is not None:
            self.revolving_accounts = revolving_accounts
        if mortgage_accounts is not None:
            self.mortgage_accounts = mortgage_accounts
        if installment_accounts is not None:
            self.installment_accounts = installment_accounts
        if other_accounts is not None:
            self.other_accounts = other_accounts
        if inquiries is not None:
            self.inquiries = inquiries
        if consumer_statements is not None:
            self.consumer_statements = consumer_statements
        if public_records is not None:
            self.public_records = public_records
        if collections is not None:
            self.collections = collections

    @property
    def provider(self):
        """Gets the provider of this CreditReportProviderView.  # noqa: E501


        :return: The provider of this CreditReportProviderView.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this CreditReportProviderView.


        :param provider: The provider of this CreditReportProviderView.  # noqa: E501
        :type: str
        """
        allowed_values = ["EFX", "TU", "EXP", "UNKNOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and provider not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"  # noqa: E501
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def summary(self):
        """Gets the summary of this CreditReportProviderView.  # noqa: E501


        :return: The summary of this CreditReportProviderView.  # noqa: E501
        :rtype: CreditReportSummary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this CreditReportProviderView.


        :param summary: The summary of this CreditReportProviderView.  # noqa: E501
        :type: CreditReportSummary
        """

        self._summary = summary

    @property
    def revolving_accounts(self):
        """Gets the revolving_accounts of this CreditReportProviderView.  # noqa: E501


        :return: The revolving_accounts of this CreditReportProviderView.  # noqa: E501
        :rtype: list[CreditReportAccount]
        """
        return self._revolving_accounts

    @revolving_accounts.setter
    def revolving_accounts(self, revolving_accounts):
        """Sets the revolving_accounts of this CreditReportProviderView.


        :param revolving_accounts: The revolving_accounts of this CreditReportProviderView.  # noqa: E501
        :type: list[CreditReportAccount]
        """

        self._revolving_accounts = revolving_accounts

    @property
    def mortgage_accounts(self):
        """Gets the mortgage_accounts of this CreditReportProviderView.  # noqa: E501


        :return: The mortgage_accounts of this CreditReportProviderView.  # noqa: E501
        :rtype: list[CreditReportAccount]
        """
        return self._mortgage_accounts

    @mortgage_accounts.setter
    def mortgage_accounts(self, mortgage_accounts):
        """Sets the mortgage_accounts of this CreditReportProviderView.


        :param mortgage_accounts: The mortgage_accounts of this CreditReportProviderView.  # noqa: E501
        :type: list[CreditReportAccount]
        """

        self._mortgage_accounts = mortgage_accounts

    @property
    def installment_accounts(self):
        """Gets the installment_accounts of this CreditReportProviderView.  # noqa: E501


        :return: The installment_accounts of this CreditReportProviderView.  # noqa: E501
        :rtype: list[CreditReportAccount]
        """
        return self._installment_accounts

    @installment_accounts.setter
    def installment_accounts(self, installment_accounts):
        """Sets the installment_accounts of this CreditReportProviderView.


        :param installment_accounts: The installment_accounts of this CreditReportProviderView.  # noqa: E501
        :type: list[CreditReportAccount]
        """

        self._installment_accounts = installment_accounts

    @property
    def other_accounts(self):
        """Gets the other_accounts of this CreditReportProviderView.  # noqa: E501


        :return: The other_accounts of this CreditReportProviderView.  # noqa: E501
        :rtype: list[CreditReportAccount]
        """
        return self._other_accounts

    @other_accounts.setter
    def other_accounts(self, other_accounts):
        """Sets the other_accounts of this CreditReportProviderView.


        :param other_accounts: The other_accounts of this CreditReportProviderView.  # noqa: E501
        :type: list[CreditReportAccount]
        """

        self._other_accounts = other_accounts

    @property
    def inquiries(self):
        """Gets the inquiries of this CreditReportProviderView.  # noqa: E501


        :return: The inquiries of this CreditReportProviderView.  # noqa: E501
        :rtype: list[Inquiry]
        """
        return self._inquiries

    @inquiries.setter
    def inquiries(self, inquiries):
        """Sets the inquiries of this CreditReportProviderView.


        :param inquiries: The inquiries of this CreditReportProviderView.  # noqa: E501
        :type: list[Inquiry]
        """

        self._inquiries = inquiries

    @property
    def consumer_statements(self):
        """Gets the consumer_statements of this CreditReportProviderView.  # noqa: E501


        :return: The consumer_statements of this CreditReportProviderView.  # noqa: E501
        :rtype: list[ConsumerStatement]
        """
        return self._consumer_statements

    @consumer_statements.setter
    def consumer_statements(self, consumer_statements):
        """Sets the consumer_statements of this CreditReportProviderView.


        :param consumer_statements: The consumer_statements of this CreditReportProviderView.  # noqa: E501
        :type: list[ConsumerStatement]
        """

        self._consumer_statements = consumer_statements

    @property
    def public_records(self):
        """Gets the public_records of this CreditReportProviderView.  # noqa: E501


        :return: The public_records of this CreditReportProviderView.  # noqa: E501
        :rtype: PublicRecords
        """
        return self._public_records

    @public_records.setter
    def public_records(self, public_records):
        """Sets the public_records of this CreditReportProviderView.


        :param public_records: The public_records of this CreditReportProviderView.  # noqa: E501
        :type: PublicRecords
        """

        self._public_records = public_records

    @property
    def collections(self):
        """Gets the collections of this CreditReportProviderView.  # noqa: E501


        :return: The collections of this CreditReportProviderView.  # noqa: E501
        :rtype: list[CollectionItem]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """Sets the collections of this CreditReportProviderView.


        :param collections: The collections of this CreditReportProviderView.  # noqa: E501
        :type: list[CollectionItem]
        """

        self._collections = collections

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreditReportProviderView):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreditReportProviderView):
            return True

        return self.to_dict() != other.to_dict()
