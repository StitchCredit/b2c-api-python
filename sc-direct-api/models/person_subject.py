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


class PersonSubject(object):
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
        'current_name': 'PersonName',
        'aliases': 'list[PersonName]',
        'current_address': 'InternationalAddress',
        'previous_addresses': 'list[InternationalAddress]',
        'home_phone': 'InternationalPhone',
        'mobile_phone': 'InternationalPhone',
        'national_identifier': 'str',
        'date_of_birth': 'datetime',
        'date_of_death': 'datetime',
        'employment_history': 'list[Employer]'
    }

    attribute_map = {
        'provider': 'provider',
        'current_name': 'currentName',
        'aliases': 'aliases',
        'current_address': 'currentAddress',
        'previous_addresses': 'previousAddresses',
        'home_phone': 'homePhone',
        'mobile_phone': 'mobilePhone',
        'national_identifier': 'nationalIdentifier',
        'date_of_birth': 'dateOfBirth',
        'date_of_death': 'dateOfDeath',
        'employment_history': 'employmentHistory'
    }

    def __init__(self, provider=None, current_name=None, aliases=None, current_address=None, previous_addresses=None, home_phone=None, mobile_phone=None, national_identifier=None, date_of_birth=None, date_of_death=None, employment_history=None, local_vars_configuration=None):  # noqa: E501
        """PersonSubject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._provider = None
        self._current_name = None
        self._aliases = None
        self._current_address = None
        self._previous_addresses = None
        self._home_phone = None
        self._mobile_phone = None
        self._national_identifier = None
        self._date_of_birth = None
        self._date_of_death = None
        self._employment_history = None
        self.discriminator = None

        if provider is not None:
            self.provider = provider
        if current_name is not None:
            self.current_name = current_name
        if aliases is not None:
            self.aliases = aliases
        if current_address is not None:
            self.current_address = current_address
        if previous_addresses is not None:
            self.previous_addresses = previous_addresses
        if home_phone is not None:
            self.home_phone = home_phone
        if mobile_phone is not None:
            self.mobile_phone = mobile_phone
        if national_identifier is not None:
            self.national_identifier = national_identifier
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if date_of_death is not None:
            self.date_of_death = date_of_death
        if employment_history is not None:
            self.employment_history = employment_history

    @property
    def provider(self):
        """Gets the provider of this PersonSubject.  # noqa: E501


        :return: The provider of this PersonSubject.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this PersonSubject.


        :param provider: The provider of this PersonSubject.  # noqa: E501
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
    def current_name(self):
        """Gets the current_name of this PersonSubject.  # noqa: E501


        :return: The current_name of this PersonSubject.  # noqa: E501
        :rtype: PersonName
        """
        return self._current_name

    @current_name.setter
    def current_name(self, current_name):
        """Sets the current_name of this PersonSubject.


        :param current_name: The current_name of this PersonSubject.  # noqa: E501
        :type: PersonName
        """

        self._current_name = current_name

    @property
    def aliases(self):
        """Gets the aliases of this PersonSubject.  # noqa: E501


        :return: The aliases of this PersonSubject.  # noqa: E501
        :rtype: list[PersonName]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this PersonSubject.


        :param aliases: The aliases of this PersonSubject.  # noqa: E501
        :type: list[PersonName]
        """

        self._aliases = aliases

    @property
    def current_address(self):
        """Gets the current_address of this PersonSubject.  # noqa: E501


        :return: The current_address of this PersonSubject.  # noqa: E501
        :rtype: InternationalAddress
        """
        return self._current_address

    @current_address.setter
    def current_address(self, current_address):
        """Sets the current_address of this PersonSubject.


        :param current_address: The current_address of this PersonSubject.  # noqa: E501
        :type: InternationalAddress
        """

        self._current_address = current_address

    @property
    def previous_addresses(self):
        """Gets the previous_addresses of this PersonSubject.  # noqa: E501


        :return: The previous_addresses of this PersonSubject.  # noqa: E501
        :rtype: list[InternationalAddress]
        """
        return self._previous_addresses

    @previous_addresses.setter
    def previous_addresses(self, previous_addresses):
        """Sets the previous_addresses of this PersonSubject.


        :param previous_addresses: The previous_addresses of this PersonSubject.  # noqa: E501
        :type: list[InternationalAddress]
        """

        self._previous_addresses = previous_addresses

    @property
    def home_phone(self):
        """Gets the home_phone of this PersonSubject.  # noqa: E501


        :return: The home_phone of this PersonSubject.  # noqa: E501
        :rtype: InternationalPhone
        """
        return self._home_phone

    @home_phone.setter
    def home_phone(self, home_phone):
        """Sets the home_phone of this PersonSubject.


        :param home_phone: The home_phone of this PersonSubject.  # noqa: E501
        :type: InternationalPhone
        """

        self._home_phone = home_phone

    @property
    def mobile_phone(self):
        """Gets the mobile_phone of this PersonSubject.  # noqa: E501


        :return: The mobile_phone of this PersonSubject.  # noqa: E501
        :rtype: InternationalPhone
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        """Sets the mobile_phone of this PersonSubject.


        :param mobile_phone: The mobile_phone of this PersonSubject.  # noqa: E501
        :type: InternationalPhone
        """

        self._mobile_phone = mobile_phone

    @property
    def national_identifier(self):
        """Gets the national_identifier of this PersonSubject.  # noqa: E501


        :return: The national_identifier of this PersonSubject.  # noqa: E501
        :rtype: str
        """
        return self._national_identifier

    @national_identifier.setter
    def national_identifier(self, national_identifier):
        """Sets the national_identifier of this PersonSubject.


        :param national_identifier: The national_identifier of this PersonSubject.  # noqa: E501
        :type: str
        """

        self._national_identifier = national_identifier

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this PersonSubject.  # noqa: E501


        :return: The date_of_birth of this PersonSubject.  # noqa: E501
        :rtype: datetime
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this PersonSubject.


        :param date_of_birth: The date_of_birth of this PersonSubject.  # noqa: E501
        :type: datetime
        """

        self._date_of_birth = date_of_birth

    @property
    def date_of_death(self):
        """Gets the date_of_death of this PersonSubject.  # noqa: E501


        :return: The date_of_death of this PersonSubject.  # noqa: E501
        :rtype: datetime
        """
        return self._date_of_death

    @date_of_death.setter
    def date_of_death(self, date_of_death):
        """Sets the date_of_death of this PersonSubject.


        :param date_of_death: The date_of_death of this PersonSubject.  # noqa: E501
        :type: datetime
        """

        self._date_of_death = date_of_death

    @property
    def employment_history(self):
        """Gets the employment_history of this PersonSubject.  # noqa: E501


        :return: The employment_history of this PersonSubject.  # noqa: E501
        :rtype: list[Employer]
        """
        return self._employment_history

    @employment_history.setter
    def employment_history(self, employment_history):
        """Sets the employment_history of this PersonSubject.


        :param employment_history: The employment_history of this PersonSubject.  # noqa: E501
        :type: list[Employer]
        """

        self._employment_history = employment_history

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
        if not isinstance(other, PersonSubject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PersonSubject):
            return True

        return self.to_dict() != other.to_dict()