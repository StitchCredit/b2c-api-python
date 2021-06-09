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


class UserLoginRespDTO(object):
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
        'id': 'str',
        'email': 'str',
        'fname': 'str',
        'lname': 'str',
        'idpass': 'bool',
        'created_at': 'int',
        'updated_at': 'int',
        'sms_msg': 'bool',
        'email_msg': 'bool',
        'push_msg': 'bool',
        'flags': 'int',
        'token': 'str',
        'expires': 'int',
        'refresh': 'str'
    }

    attribute_map = {
        'id': 'id',
        'email': 'email',
        'fname': 'fname',
        'lname': 'lname',
        'idpass': 'idpass',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'sms_msg': 'smsMsg',
        'email_msg': 'emailMsg',
        'push_msg': 'pushMsg',
        'flags': 'flags',
        'token': 'token',
        'expires': 'expires',
        'refresh': 'refresh'
    }

    def __init__(self, id=None, email=None, fname=None, lname=None, idpass=None, created_at=None, updated_at=None, sms_msg=None, email_msg=None, push_msg=None, flags=None, token=None, expires=None, refresh=None, local_vars_configuration=None):  # noqa: E501
        """UserLoginRespDTO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._email = None
        self._fname = None
        self._lname = None
        self._idpass = None
        self._created_at = None
        self._updated_at = None
        self._sms_msg = None
        self._email_msg = None
        self._push_msg = None
        self._flags = None
        self._token = None
        self._expires = None
        self._refresh = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if email is not None:
            self.email = email
        if fname is not None:
            self.fname = fname
        if lname is not None:
            self.lname = lname
        if idpass is not None:
            self.idpass = idpass
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if sms_msg is not None:
            self.sms_msg = sms_msg
        if email_msg is not None:
            self.email_msg = email_msg
        if push_msg is not None:
            self.push_msg = push_msg
        if flags is not None:
            self.flags = flags
        if token is not None:
            self.token = token
        if expires is not None:
            self.expires = expires
        if refresh is not None:
            self.refresh = refresh

    @property
    def id(self):
        """Gets the id of this UserLoginRespDTO.  # noqa: E501


        :return: The id of this UserLoginRespDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserLoginRespDTO.


        :param id: The id of this UserLoginRespDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def email(self):
        """Gets the email of this UserLoginRespDTO.  # noqa: E501


        :return: The email of this UserLoginRespDTO.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserLoginRespDTO.


        :param email: The email of this UserLoginRespDTO.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def fname(self):
        """Gets the fname of this UserLoginRespDTO.  # noqa: E501


        :return: The fname of this UserLoginRespDTO.  # noqa: E501
        :rtype: str
        """
        return self._fname

    @fname.setter
    def fname(self, fname):
        """Sets the fname of this UserLoginRespDTO.


        :param fname: The fname of this UserLoginRespDTO.  # noqa: E501
        :type: str
        """

        self._fname = fname

    @property
    def lname(self):
        """Gets the lname of this UserLoginRespDTO.  # noqa: E501


        :return: The lname of this UserLoginRespDTO.  # noqa: E501
        :rtype: str
        """
        return self._lname

    @lname.setter
    def lname(self, lname):
        """Sets the lname of this UserLoginRespDTO.


        :param lname: The lname of this UserLoginRespDTO.  # noqa: E501
        :type: str
        """

        self._lname = lname

    @property
    def idpass(self):
        """Gets the idpass of this UserLoginRespDTO.  # noqa: E501


        :return: The idpass of this UserLoginRespDTO.  # noqa: E501
        :rtype: bool
        """
        return self._idpass

    @idpass.setter
    def idpass(self, idpass):
        """Sets the idpass of this UserLoginRespDTO.


        :param idpass: The idpass of this UserLoginRespDTO.  # noqa: E501
        :type: bool
        """

        self._idpass = idpass

    @property
    def created_at(self):
        """Gets the created_at of this UserLoginRespDTO.  # noqa: E501


        :return: The created_at of this UserLoginRespDTO.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UserLoginRespDTO.


        :param created_at: The created_at of this UserLoginRespDTO.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this UserLoginRespDTO.  # noqa: E501


        :return: The updated_at of this UserLoginRespDTO.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this UserLoginRespDTO.


        :param updated_at: The updated_at of this UserLoginRespDTO.  # noqa: E501
        :type: int
        """

        self._updated_at = updated_at

    @property
    def sms_msg(self):
        """Gets the sms_msg of this UserLoginRespDTO.  # noqa: E501


        :return: The sms_msg of this UserLoginRespDTO.  # noqa: E501
        :rtype: bool
        """
        return self._sms_msg

    @sms_msg.setter
    def sms_msg(self, sms_msg):
        """Sets the sms_msg of this UserLoginRespDTO.


        :param sms_msg: The sms_msg of this UserLoginRespDTO.  # noqa: E501
        :type: bool
        """

        self._sms_msg = sms_msg

    @property
    def email_msg(self):
        """Gets the email_msg of this UserLoginRespDTO.  # noqa: E501


        :return: The email_msg of this UserLoginRespDTO.  # noqa: E501
        :rtype: bool
        """
        return self._email_msg

    @email_msg.setter
    def email_msg(self, email_msg):
        """Sets the email_msg of this UserLoginRespDTO.


        :param email_msg: The email_msg of this UserLoginRespDTO.  # noqa: E501
        :type: bool
        """

        self._email_msg = email_msg

    @property
    def push_msg(self):
        """Gets the push_msg of this UserLoginRespDTO.  # noqa: E501


        :return: The push_msg of this UserLoginRespDTO.  # noqa: E501
        :rtype: bool
        """
        return self._push_msg

    @push_msg.setter
    def push_msg(self, push_msg):
        """Sets the push_msg of this UserLoginRespDTO.


        :param push_msg: The push_msg of this UserLoginRespDTO.  # noqa: E501
        :type: bool
        """

        self._push_msg = push_msg

    @property
    def flags(self):
        """Gets the flags of this UserLoginRespDTO.  # noqa: E501


        :return: The flags of this UserLoginRespDTO.  # noqa: E501
        :rtype: int
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """Sets the flags of this UserLoginRespDTO.


        :param flags: The flags of this UserLoginRespDTO.  # noqa: E501
        :type: int
        """

        self._flags = flags

    @property
    def token(self):
        """Gets the token of this UserLoginRespDTO.  # noqa: E501


        :return: The token of this UserLoginRespDTO.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UserLoginRespDTO.


        :param token: The token of this UserLoginRespDTO.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def expires(self):
        """Gets the expires of this UserLoginRespDTO.  # noqa: E501


        :return: The expires of this UserLoginRespDTO.  # noqa: E501
        :rtype: int
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this UserLoginRespDTO.


        :param expires: The expires of this UserLoginRespDTO.  # noqa: E501
        :type: int
        """

        self._expires = expires

    @property
    def refresh(self):
        """Gets the refresh of this UserLoginRespDTO.  # noqa: E501


        :return: The refresh of this UserLoginRespDTO.  # noqa: E501
        :rtype: str
        """
        return self._refresh

    @refresh.setter
    def refresh(self, refresh):
        """Sets the refresh of this UserLoginRespDTO.


        :param refresh: The refresh of this UserLoginRespDTO.  # noqa: E501
        :type: str
        """

        self._refresh = refresh

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
        if not isinstance(other, UserLoginRespDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserLoginRespDTO):
            return True

        return self.to_dict() != other.to_dict()
