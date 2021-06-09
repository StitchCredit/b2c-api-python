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

from ecreditapi.configuration import Configuration


class ConsumerStatement(object):
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
        'id': 'str',
        'reported_date': 'int',
        'statement': 'str'
    }

    attribute_map = {
        'provider': 'provider',
        'id': 'id',
        'reported_date': 'reportedDate',
        'statement': 'statement'
    }

    def __init__(self, provider=None, id=None, reported_date=None, statement=None, local_vars_configuration=None):  # noqa: E501
        """ConsumerStatement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._provider = None
        self._id = None
        self._reported_date = None
        self._statement = None
        self.discriminator = None

        if provider is not None:
            self.provider = provider
        if id is not None:
            self.id = id
        if reported_date is not None:
            self.reported_date = reported_date
        if statement is not None:
            self.statement = statement

    @property
    def provider(self):
        """Gets the provider of this ConsumerStatement.  # noqa: E501


        :return: The provider of this ConsumerStatement.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ConsumerStatement.


        :param provider: The provider of this ConsumerStatement.  # noqa: E501
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
    def id(self):
        """Gets the id of this ConsumerStatement.  # noqa: E501


        :return: The id of this ConsumerStatement.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConsumerStatement.


        :param id: The id of this ConsumerStatement.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def reported_date(self):
        """Gets the reported_date of this ConsumerStatement.  # noqa: E501


        :return: The reported_date of this ConsumerStatement.  # noqa: E501
        :rtype: int
        """
        return self._reported_date

    @reported_date.setter
    def reported_date(self, reported_date):
        """Sets the reported_date of this ConsumerStatement.


        :param reported_date: The reported_date of this ConsumerStatement.  # noqa: E501
        :type: int
        """

        self._reported_date = reported_date

    @property
    def statement(self):
        """Gets the statement of this ConsumerStatement.  # noqa: E501


        :return: The statement of this ConsumerStatement.  # noqa: E501
        :rtype: str
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        """Sets the statement of this ConsumerStatement.


        :param statement: The statement of this ConsumerStatement.  # noqa: E501
        :type: str
        """

        self._statement = statement

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
        if not isinstance(other, ConsumerStatement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConsumerStatement):
            return True

        return self.to_dict() != other.to_dict()
