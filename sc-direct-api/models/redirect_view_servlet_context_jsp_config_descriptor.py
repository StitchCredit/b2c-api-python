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


class RedirectViewServletContextJspConfigDescriptor(object):
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
        'jsp_property_groups': 'list[RedirectViewServletContextJspConfigDescriptorJspPropertyGroups]',
        'taglibs': 'list[RedirectViewServletContextJspConfigDescriptorTaglibs]'
    }

    attribute_map = {
        'jsp_property_groups': 'jspPropertyGroups',
        'taglibs': 'taglibs'
    }

    def __init__(self, jsp_property_groups=None, taglibs=None, local_vars_configuration=None):  # noqa: E501
        """RedirectViewServletContextJspConfigDescriptor - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._jsp_property_groups = None
        self._taglibs = None
        self.discriminator = None

        if jsp_property_groups is not None:
            self.jsp_property_groups = jsp_property_groups
        if taglibs is not None:
            self.taglibs = taglibs

    @property
    def jsp_property_groups(self):
        """Gets the jsp_property_groups of this RedirectViewServletContextJspConfigDescriptor.  # noqa: E501


        :return: The jsp_property_groups of this RedirectViewServletContextJspConfigDescriptor.  # noqa: E501
        :rtype: list[RedirectViewServletContextJspConfigDescriptorJspPropertyGroups]
        """
        return self._jsp_property_groups

    @jsp_property_groups.setter
    def jsp_property_groups(self, jsp_property_groups):
        """Sets the jsp_property_groups of this RedirectViewServletContextJspConfigDescriptor.


        :param jsp_property_groups: The jsp_property_groups of this RedirectViewServletContextJspConfigDescriptor.  # noqa: E501
        :type: list[RedirectViewServletContextJspConfigDescriptorJspPropertyGroups]
        """

        self._jsp_property_groups = jsp_property_groups

    @property
    def taglibs(self):
        """Gets the taglibs of this RedirectViewServletContextJspConfigDescriptor.  # noqa: E501


        :return: The taglibs of this RedirectViewServletContextJspConfigDescriptor.  # noqa: E501
        :rtype: list[RedirectViewServletContextJspConfigDescriptorTaglibs]
        """
        return self._taglibs

    @taglibs.setter
    def taglibs(self, taglibs):
        """Sets the taglibs of this RedirectViewServletContextJspConfigDescriptor.


        :param taglibs: The taglibs of this RedirectViewServletContextJspConfigDescriptor.  # noqa: E501
        :type: list[RedirectViewServletContextJspConfigDescriptorTaglibs]
        """

        self._taglibs = taglibs

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
        if not isinstance(other, RedirectViewServletContextJspConfigDescriptor):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RedirectViewServletContextJspConfigDescriptor):
            return True

        return self.to_dict() != other.to_dict()
