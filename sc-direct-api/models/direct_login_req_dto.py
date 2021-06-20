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


class DirectLoginReqDTO(object):
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
        'apikey': 'str',
        'secret': 'str'
    }

    attribute_map = {
        'apikey': 'apikey',
        'secret': 'secret'
    }

    def __init__(self, apikey=None, secret=None, local_vars_configuration=None):  # noqa: E501
        """DirectLoginReqDTO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._apikey = None
        self._secret = None
        self.discriminator = None

        self.apikey = apikey
        self.secret = secret

    @property
    def apikey(self):
        """Gets the apikey of this DirectLoginReqDTO.  # noqa: E501


        :return: The apikey of this DirectLoginReqDTO.  # noqa: E501
        :rtype: str
        """
        return self._apikey

    @apikey.setter
    def apikey(self, apikey):
        """Sets the apikey of this DirectLoginReqDTO.


        :param apikey: The apikey of this DirectLoginReqDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and apikey is None:  # noqa: E501
            raise ValueError("Invalid value for `apikey`, must not be `None`")  # noqa: E501

        self._apikey = apikey

    @property
    def secret(self):
        """Gets the secret of this DirectLoginReqDTO.  # noqa: E501


        :return: The secret of this DirectLoginReqDTO.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this DirectLoginReqDTO.


        :param secret: The secret of this DirectLoginReqDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and secret is None:  # noqa: E501
            raise ValueError("Invalid value for `secret`, must not be `None`")  # noqa: E501

        self._secret = secret

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
        if not isinstance(other, DirectLoginReqDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DirectLoginReqDTO):
            return True

        return self.to_dict() != other.to_dict()