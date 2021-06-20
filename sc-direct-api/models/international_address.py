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


class InternationalAddress(object):
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
        'country': 'Country',
        'line1': 'str',
        'line2': 'str',
        'line3': 'str',
        'line4': 'str',
        'line5': 'str',
        'first_reported_date': 'datetime',
        'last_reported_date': 'datetime',
        'phone': 'InternationalPhone'
    }

    attribute_map = {
        'country': 'country',
        'line1': 'line1',
        'line2': 'line2',
        'line3': 'line3',
        'line4': 'line4',
        'line5': 'line5',
        'first_reported_date': 'firstReportedDate',
        'last_reported_date': 'lastReportedDate',
        'phone': 'phone'
    }

    def __init__(self, country=None, line1=None, line2=None, line3=None, line4=None, line5=None, first_reported_date=None, last_reported_date=None, phone=None, local_vars_configuration=None):  # noqa: E501
        """InternationalAddress - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._country = None
        self._line1 = None
        self._line2 = None
        self._line3 = None
        self._line4 = None
        self._line5 = None
        self._first_reported_date = None
        self._last_reported_date = None
        self._phone = None
        self.discriminator = None

        if country is not None:
            self.country = country
        if line1 is not None:
            self.line1 = line1
        if line2 is not None:
            self.line2 = line2
        if line3 is not None:
            self.line3 = line3
        if line4 is not None:
            self.line4 = line4
        if line5 is not None:
            self.line5 = line5
        if first_reported_date is not None:
            self.first_reported_date = first_reported_date
        if last_reported_date is not None:
            self.last_reported_date = last_reported_date
        if phone is not None:
            self.phone = phone

    @property
    def country(self):
        """Gets the country of this InternationalAddress.  # noqa: E501


        :return: The country of this InternationalAddress.  # noqa: E501
        :rtype: Country
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this InternationalAddress.


        :param country: The country of this InternationalAddress.  # noqa: E501
        :type: Country
        """

        self._country = country

    @property
    def line1(self):
        """Gets the line1 of this InternationalAddress.  # noqa: E501


        :return: The line1 of this InternationalAddress.  # noqa: E501
        :rtype: str
        """
        return self._line1

    @line1.setter
    def line1(self, line1):
        """Sets the line1 of this InternationalAddress.


        :param line1: The line1 of this InternationalAddress.  # noqa: E501
        :type: str
        """

        self._line1 = line1

    @property
    def line2(self):
        """Gets the line2 of this InternationalAddress.  # noqa: E501


        :return: The line2 of this InternationalAddress.  # noqa: E501
        :rtype: str
        """
        return self._line2

    @line2.setter
    def line2(self, line2):
        """Sets the line2 of this InternationalAddress.


        :param line2: The line2 of this InternationalAddress.  # noqa: E501
        :type: str
        """

        self._line2 = line2

    @property
    def line3(self):
        """Gets the line3 of this InternationalAddress.  # noqa: E501


        :return: The line3 of this InternationalAddress.  # noqa: E501
        :rtype: str
        """
        return self._line3

    @line3.setter
    def line3(self, line3):
        """Sets the line3 of this InternationalAddress.


        :param line3: The line3 of this InternationalAddress.  # noqa: E501
        :type: str
        """

        self._line3 = line3

    @property
    def line4(self):
        """Gets the line4 of this InternationalAddress.  # noqa: E501


        :return: The line4 of this InternationalAddress.  # noqa: E501
        :rtype: str
        """
        return self._line4

    @line4.setter
    def line4(self, line4):
        """Sets the line4 of this InternationalAddress.


        :param line4: The line4 of this InternationalAddress.  # noqa: E501
        :type: str
        """

        self._line4 = line4

    @property
    def line5(self):
        """Gets the line5 of this InternationalAddress.  # noqa: E501


        :return: The line5 of this InternationalAddress.  # noqa: E501
        :rtype: str
        """
        return self._line5

    @line5.setter
    def line5(self, line5):
        """Sets the line5 of this InternationalAddress.


        :param line5: The line5 of this InternationalAddress.  # noqa: E501
        :type: str
        """

        self._line5 = line5

    @property
    def first_reported_date(self):
        """Gets the first_reported_date of this InternationalAddress.  # noqa: E501


        :return: The first_reported_date of this InternationalAddress.  # noqa: E501
        :rtype: datetime
        """
        return self._first_reported_date

    @first_reported_date.setter
    def first_reported_date(self, first_reported_date):
        """Sets the first_reported_date of this InternationalAddress.


        :param first_reported_date: The first_reported_date of this InternationalAddress.  # noqa: E501
        :type: datetime
        """

        self._first_reported_date = first_reported_date

    @property
    def last_reported_date(self):
        """Gets the last_reported_date of this InternationalAddress.  # noqa: E501


        :return: The last_reported_date of this InternationalAddress.  # noqa: E501
        :rtype: datetime
        """
        return self._last_reported_date

    @last_reported_date.setter
    def last_reported_date(self, last_reported_date):
        """Sets the last_reported_date of this InternationalAddress.


        :param last_reported_date: The last_reported_date of this InternationalAddress.  # noqa: E501
        :type: datetime
        """

        self._last_reported_date = last_reported_date

    @property
    def phone(self):
        """Gets the phone of this InternationalAddress.  # noqa: E501


        :return: The phone of this InternationalAddress.  # noqa: E501
        :rtype: InternationalPhone
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this InternationalAddress.


        :param phone: The phone of this InternationalAddress.  # noqa: E501
        :type: InternationalPhone
        """

        self._phone = phone

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
        if not isinstance(other, InternationalAddress):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InternationalAddress):
            return True

        return self.to_dict() != other.to_dict()