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


class IdentityReqDTO(object):
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
        'dob': 'date',
        'mobile': 'str',
        'ssn': 'str',
        'street1': 'str',
        'street2': 'str',
        'city': 'str',
        'state': 'str',
        'zip': 'str',
        'country': 'str'
    }

    attribute_map = {
        'dob': 'dob',
        'mobile': 'mobile',
        'ssn': 'ssn',
        'street1': 'street1',
        'street2': 'street2',
        'city': 'city',
        'state': 'state',
        'zip': 'zip',
        'country': 'country'
    }

    def __init__(self, dob=None, mobile=None, ssn=None, street1=None, street2=None, city=None, state=None, zip=None, country=None, local_vars_configuration=None):  # noqa: E501
        """IdentityReqDTO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dob = None
        self._mobile = None
        self._ssn = None
        self._street1 = None
        self._street2 = None
        self._city = None
        self._state = None
        self._zip = None
        self._country = None
        self.discriminator = None

        if dob is not None:
            self.dob = dob
        if mobile is not None:
            self.mobile = mobile
        self.ssn = ssn
        self.street1 = street1
        if street2 is not None:
            self.street2 = street2
        self.city = city
        self.state = state
        self.zip = zip
        if country is not None:
            self.country = country

    @property
    def dob(self):
        """Gets the dob of this IdentityReqDTO.  # noqa: E501


        :return: The dob of this IdentityReqDTO.  # noqa: E501
        :rtype: date
        """
        return self._dob

    @dob.setter
    def dob(self, dob):
        """Sets the dob of this IdentityReqDTO.


        :param dob: The dob of this IdentityReqDTO.  # noqa: E501
        :type: date
        """

        self._dob = dob

    @property
    def mobile(self):
        """Gets the mobile of this IdentityReqDTO.  # noqa: E501


        :return: The mobile of this IdentityReqDTO.  # noqa: E501
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this IdentityReqDTO.


        :param mobile: The mobile of this IdentityReqDTO.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                mobile is not None and len(mobile) > 10):
            raise ValueError("Invalid value for `mobile`, length must be less than or equal to `10`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                mobile is not None and len(mobile) < 10):
            raise ValueError("Invalid value for `mobile`, length must be greater than or equal to `10`")  # noqa: E501

        self._mobile = mobile

    @property
    def ssn(self):
        """Gets the ssn of this IdentityReqDTO.  # noqa: E501


        :return: The ssn of this IdentityReqDTO.  # noqa: E501
        :rtype: str
        """
        return self._ssn

    @ssn.setter
    def ssn(self, ssn):
        """Sets the ssn of this IdentityReqDTO.


        :param ssn: The ssn of this IdentityReqDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ssn is None:  # noqa: E501
            raise ValueError("Invalid value for `ssn`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                ssn is not None and len(ssn) > 9):
            raise ValueError("Invalid value for `ssn`, length must be less than or equal to `9`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                ssn is not None and len(ssn) < 9):
            raise ValueError("Invalid value for `ssn`, length must be greater than or equal to `9`")  # noqa: E501

        self._ssn = ssn

    @property
    def street1(self):
        """Gets the street1 of this IdentityReqDTO.  # noqa: E501


        :return: The street1 of this IdentityReqDTO.  # noqa: E501
        :rtype: str
        """
        return self._street1

    @street1.setter
    def street1(self, street1):
        """Sets the street1 of this IdentityReqDTO.


        :param street1: The street1 of this IdentityReqDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and street1 is None:  # noqa: E501
            raise ValueError("Invalid value for `street1`, must not be `None`")  # noqa: E501

        self._street1 = street1

    @property
    def street2(self):
        """Gets the street2 of this IdentityReqDTO.  # noqa: E501


        :return: The street2 of this IdentityReqDTO.  # noqa: E501
        :rtype: str
        """
        return self._street2

    @street2.setter
    def street2(self, street2):
        """Sets the street2 of this IdentityReqDTO.


        :param street2: The street2 of this IdentityReqDTO.  # noqa: E501
        :type: str
        """

        self._street2 = street2

    @property
    def city(self):
        """Gets the city of this IdentityReqDTO.  # noqa: E501


        :return: The city of this IdentityReqDTO.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this IdentityReqDTO.


        :param city: The city of this IdentityReqDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and city is None:  # noqa: E501
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def state(self):
        """Gets the state of this IdentityReqDTO.  # noqa: E501


        :return: The state of this IdentityReqDTO.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this IdentityReqDTO.


        :param state: The state of this IdentityReqDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                state is not None and len(state) > 2):
            raise ValueError("Invalid value for `state`, length must be less than or equal to `2`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                state is not None and len(state) < 2):
            raise ValueError("Invalid value for `state`, length must be greater than or equal to `2`")  # noqa: E501

        self._state = state

    @property
    def zip(self):
        """Gets the zip of this IdentityReqDTO.  # noqa: E501


        :return: The zip of this IdentityReqDTO.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this IdentityReqDTO.


        :param zip: The zip of this IdentityReqDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and zip is None:  # noqa: E501
            raise ValueError("Invalid value for `zip`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                zip is not None and len(zip) > 5):
            raise ValueError("Invalid value for `zip`, length must be less than or equal to `5`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                zip is not None and len(zip) < 5):
            raise ValueError("Invalid value for `zip`, length must be greater than or equal to `5`")  # noqa: E501

        self._zip = zip

    @property
    def country(self):
        """Gets the country of this IdentityReqDTO.  # noqa: E501


        :return: The country of this IdentityReqDTO.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this IdentityReqDTO.


        :param country: The country of this IdentityReqDTO.  # noqa: E501
        :type: str
        """

        self._country = country

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
        if not isinstance(other, IdentityReqDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IdentityReqDTO):
            return True

        return self.to_dict() != other.to_dict()
