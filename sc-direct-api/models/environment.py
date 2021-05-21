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


class Environment(object):
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
        'default_profiles': 'list[str]',
        'active_profiles': 'list[str]'
    }

    attribute_map = {
        'default_profiles': 'defaultProfiles',
        'active_profiles': 'activeProfiles'
    }

    def __init__(self, default_profiles=None, active_profiles=None, local_vars_configuration=None):  # noqa: E501
        """Environment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._default_profiles = None
        self._active_profiles = None
        self.discriminator = None

        if default_profiles is not None:
            self.default_profiles = default_profiles
        if active_profiles is not None:
            self.active_profiles = active_profiles

    @property
    def default_profiles(self):
        """Gets the default_profiles of this Environment.  # noqa: E501


        :return: The default_profiles of this Environment.  # noqa: E501
        :rtype: list[str]
        """
        return self._default_profiles

    @default_profiles.setter
    def default_profiles(self, default_profiles):
        """Sets the default_profiles of this Environment.


        :param default_profiles: The default_profiles of this Environment.  # noqa: E501
        :type: list[str]
        """

        self._default_profiles = default_profiles

    @property
    def active_profiles(self):
        """Gets the active_profiles of this Environment.  # noqa: E501


        :return: The active_profiles of this Environment.  # noqa: E501
        :rtype: list[str]
        """
        return self._active_profiles

    @active_profiles.setter
    def active_profiles(self, active_profiles):
        """Sets the active_profiles of this Environment.


        :param active_profiles: The active_profiles of this Environment.  # noqa: E501
        :type: list[str]
        """

        self._active_profiles = active_profiles

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
        if not isinstance(other, Environment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Environment):
            return True

        return self.to_dict() != other.to_dict()
