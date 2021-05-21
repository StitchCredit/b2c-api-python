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


class DirectUserRegReqDTO(object):
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
        'email': 'str',
        'mobile': 'str',
        'fname': 'str',
        'lname': 'str',
        'sms_msg': 'bool',
        'email_msg': 'bool',
        'push_msg': 'bool'
    }

    attribute_map = {
        'email': 'email',
        'mobile': 'mobile',
        'fname': 'fname',
        'lname': 'lname',
        'sms_msg': 'smsMsg',
        'email_msg': 'emailMsg',
        'push_msg': 'pushMsg'
    }

    def __init__(self, email=None, mobile=None, fname=None, lname=None, sms_msg=None, email_msg=None, push_msg=None, local_vars_configuration=None):  # noqa: E501
        """DirectUserRegReqDTO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._email = None
        self._mobile = None
        self._fname = None
        self._lname = None
        self._sms_msg = None
        self._email_msg = None
        self._push_msg = None
        self.discriminator = None

        self.email = email
        if mobile is not None:
            self.mobile = mobile
        self.fname = fname
        self.lname = lname
        if sms_msg is not None:
            self.sms_msg = sms_msg
        if email_msg is not None:
            self.email_msg = email_msg
        if push_msg is not None:
            self.push_msg = push_msg

    @property
    def email(self):
        """Gets the email of this DirectUserRegReqDTO.  # noqa: E501


        :return: The email of this DirectUserRegReqDTO.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this DirectUserRegReqDTO.


        :param email: The email of this DirectUserRegReqDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def mobile(self):
        """Gets the mobile of this DirectUserRegReqDTO.  # noqa: E501


        :return: The mobile of this DirectUserRegReqDTO.  # noqa: E501
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this DirectUserRegReqDTO.


        :param mobile: The mobile of this DirectUserRegReqDTO.  # noqa: E501
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
    def fname(self):
        """Gets the fname of this DirectUserRegReqDTO.  # noqa: E501


        :return: The fname of this DirectUserRegReqDTO.  # noqa: E501
        :rtype: str
        """
        return self._fname

    @fname.setter
    def fname(self, fname):
        """Sets the fname of this DirectUserRegReqDTO.


        :param fname: The fname of this DirectUserRegReqDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and fname is None:  # noqa: E501
            raise ValueError("Invalid value for `fname`, must not be `None`")  # noqa: E501

        self._fname = fname

    @property
    def lname(self):
        """Gets the lname of this DirectUserRegReqDTO.  # noqa: E501


        :return: The lname of this DirectUserRegReqDTO.  # noqa: E501
        :rtype: str
        """
        return self._lname

    @lname.setter
    def lname(self, lname):
        """Sets the lname of this DirectUserRegReqDTO.


        :param lname: The lname of this DirectUserRegReqDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and lname is None:  # noqa: E501
            raise ValueError("Invalid value for `lname`, must not be `None`")  # noqa: E501

        self._lname = lname

    @property
    def sms_msg(self):
        """Gets the sms_msg of this DirectUserRegReqDTO.  # noqa: E501


        :return: The sms_msg of this DirectUserRegReqDTO.  # noqa: E501
        :rtype: bool
        """
        return self._sms_msg

    @sms_msg.setter
    def sms_msg(self, sms_msg):
        """Sets the sms_msg of this DirectUserRegReqDTO.


        :param sms_msg: The sms_msg of this DirectUserRegReqDTO.  # noqa: E501
        :type: bool
        """

        self._sms_msg = sms_msg

    @property
    def email_msg(self):
        """Gets the email_msg of this DirectUserRegReqDTO.  # noqa: E501


        :return: The email_msg of this DirectUserRegReqDTO.  # noqa: E501
        :rtype: bool
        """
        return self._email_msg

    @email_msg.setter
    def email_msg(self, email_msg):
        """Sets the email_msg of this DirectUserRegReqDTO.


        :param email_msg: The email_msg of this DirectUserRegReqDTO.  # noqa: E501
        :type: bool
        """

        self._email_msg = email_msg

    @property
    def push_msg(self):
        """Gets the push_msg of this DirectUserRegReqDTO.  # noqa: E501


        :return: The push_msg of this DirectUserRegReqDTO.  # noqa: E501
        :rtype: bool
        """
        return self._push_msg

    @push_msg.setter
    def push_msg(self, push_msg):
        """Sets the push_msg of this DirectUserRegReqDTO.


        :param push_msg: The push_msg of this DirectUserRegReqDTO.  # noqa: E501
        :type: bool
        """

        self._push_msg = push_msg

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
        if not isinstance(other, DirectUserRegReqDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DirectUserRegReqDTO):
            return True

        return self.to_dict() != other.to_dict()
