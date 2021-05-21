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


class IdentityQuizDTO(object):
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
        'key': 'str',
        'id': 'int',
        'questions': 'list[Question]'
    }

    attribute_map = {
        'key': 'key',
        'id': 'id',
        'questions': 'questions'
    }

    def __init__(self, key=None, id=None, questions=None, local_vars_configuration=None):  # noqa: E501
        """IdentityQuizDTO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._key = None
        self._id = None
        self._questions = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if id is not None:
            self.id = id
        if questions is not None:
            self.questions = questions

    @property
    def key(self):
        """Gets the key of this IdentityQuizDTO.  # noqa: E501


        :return: The key of this IdentityQuizDTO.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this IdentityQuizDTO.


        :param key: The key of this IdentityQuizDTO.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def id(self):
        """Gets the id of this IdentityQuizDTO.  # noqa: E501


        :return: The id of this IdentityQuizDTO.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IdentityQuizDTO.


        :param id: The id of this IdentityQuizDTO.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def questions(self):
        """Gets the questions of this IdentityQuizDTO.  # noqa: E501


        :return: The questions of this IdentityQuizDTO.  # noqa: E501
        :rtype: list[Question]
        """
        return self._questions

    @questions.setter
    def questions(self, questions):
        """Sets the questions of this IdentityQuizDTO.


        :param questions: The questions of this IdentityQuizDTO.  # noqa: E501
        :type: list[Question]
        """

        self._questions = questions

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
        if not isinstance(other, IdentityQuizDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IdentityQuizDTO):
            return True

        return self.to_dict() != other.to_dict()
