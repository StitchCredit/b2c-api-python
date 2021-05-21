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


class LatestScore(object):
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
        'score_type': 'str',
        'score_model': 'str',
        'generated_date': 'int',
        'provider_views': 'list[ProviderView]'
    }

    attribute_map = {
        'id': 'id',
        'score_type': 'scoreType',
        'score_model': 'scoreModel',
        'generated_date': 'generatedDate',
        'provider_views': 'providerViews'
    }

    def __init__(self, id=None, score_type=None, score_model=None, generated_date=None, provider_views=None, local_vars_configuration=None):  # noqa: E501
        """LatestScore - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._score_type = None
        self._score_model = None
        self._generated_date = None
        self._provider_views = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if score_type is not None:
            self.score_type = score_type
        if score_model is not None:
            self.score_model = score_model
        if generated_date is not None:
            self.generated_date = generated_date
        if provider_views is not None:
            self.provider_views = provider_views

    @property
    def id(self):
        """Gets the id of this LatestScore.  # noqa: E501


        :return: The id of this LatestScore.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LatestScore.


        :param id: The id of this LatestScore.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def score_type(self):
        """Gets the score_type of this LatestScore.  # noqa: E501


        :return: The score_type of this LatestScore.  # noqa: E501
        :rtype: str
        """
        return self._score_type

    @score_type.setter
    def score_type(self, score_type):
        """Sets the score_type of this LatestScore.


        :param score_type: The score_type of this LatestScore.  # noqa: E501
        :type: str
        """

        self._score_type = score_type

    @property
    def score_model(self):
        """Gets the score_model of this LatestScore.  # noqa: E501


        :return: The score_model of this LatestScore.  # noqa: E501
        :rtype: str
        """
        return self._score_model

    @score_model.setter
    def score_model(self, score_model):
        """Sets the score_model of this LatestScore.


        :param score_model: The score_model of this LatestScore.  # noqa: E501
        :type: str
        """

        self._score_model = score_model

    @property
    def generated_date(self):
        """Gets the generated_date of this LatestScore.  # noqa: E501


        :return: The generated_date of this LatestScore.  # noqa: E501
        :rtype: int
        """
        return self._generated_date

    @generated_date.setter
    def generated_date(self, generated_date):
        """Sets the generated_date of this LatestScore.


        :param generated_date: The generated_date of this LatestScore.  # noqa: E501
        :type: int
        """

        self._generated_date = generated_date

    @property
    def provider_views(self):
        """Gets the provider_views of this LatestScore.  # noqa: E501


        :return: The provider_views of this LatestScore.  # noqa: E501
        :rtype: list[ProviderView]
        """
        return self._provider_views

    @provider_views.setter
    def provider_views(self, provider_views):
        """Sets the provider_views of this LatestScore.


        :param provider_views: The provider_views of this LatestScore.  # noqa: E501
        :type: list[ProviderView]
        """

        self._provider_views = provider_views

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
        if not isinstance(other, LatestScore):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LatestScore):
            return True

        return self.to_dict() != other.to_dict()
