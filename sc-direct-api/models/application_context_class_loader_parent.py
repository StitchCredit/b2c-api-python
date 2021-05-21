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


class ApplicationContextClassLoaderParent(object):
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
        'name': 'str',
        'unnamed_module': 'ApplicationContextClassLoaderParentUnnamedModule',
        'default_assertion_status': 'bool',
        'registered_as_parallel_capable': 'bool',
        'defined_packages': 'list[ApplicationContextClassLoaderParentUnnamedModuleClassLoaderDefinedPackages]'
    }

    attribute_map = {
        'name': 'name',
        'unnamed_module': 'unnamedModule',
        'default_assertion_status': 'defaultAssertionStatus',
        'registered_as_parallel_capable': 'registeredAsParallelCapable',
        'defined_packages': 'definedPackages'
    }

    def __init__(self, name=None, unnamed_module=None, default_assertion_status=None, registered_as_parallel_capable=None, defined_packages=None, local_vars_configuration=None):  # noqa: E501
        """ApplicationContextClassLoaderParent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._unnamed_module = None
        self._default_assertion_status = None
        self._registered_as_parallel_capable = None
        self._defined_packages = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if unnamed_module is not None:
            self.unnamed_module = unnamed_module
        if default_assertion_status is not None:
            self.default_assertion_status = default_assertion_status
        if registered_as_parallel_capable is not None:
            self.registered_as_parallel_capable = registered_as_parallel_capable
        if defined_packages is not None:
            self.defined_packages = defined_packages

    @property
    def name(self):
        """Gets the name of this ApplicationContextClassLoaderParent.  # noqa: E501


        :return: The name of this ApplicationContextClassLoaderParent.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApplicationContextClassLoaderParent.


        :param name: The name of this ApplicationContextClassLoaderParent.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def unnamed_module(self):
        """Gets the unnamed_module of this ApplicationContextClassLoaderParent.  # noqa: E501


        :return: The unnamed_module of this ApplicationContextClassLoaderParent.  # noqa: E501
        :rtype: ApplicationContextClassLoaderParentUnnamedModule
        """
        return self._unnamed_module

    @unnamed_module.setter
    def unnamed_module(self, unnamed_module):
        """Sets the unnamed_module of this ApplicationContextClassLoaderParent.


        :param unnamed_module: The unnamed_module of this ApplicationContextClassLoaderParent.  # noqa: E501
        :type: ApplicationContextClassLoaderParentUnnamedModule
        """

        self._unnamed_module = unnamed_module

    @property
    def default_assertion_status(self):
        """Gets the default_assertion_status of this ApplicationContextClassLoaderParent.  # noqa: E501


        :return: The default_assertion_status of this ApplicationContextClassLoaderParent.  # noqa: E501
        :rtype: bool
        """
        return self._default_assertion_status

    @default_assertion_status.setter
    def default_assertion_status(self, default_assertion_status):
        """Sets the default_assertion_status of this ApplicationContextClassLoaderParent.


        :param default_assertion_status: The default_assertion_status of this ApplicationContextClassLoaderParent.  # noqa: E501
        :type: bool
        """

        self._default_assertion_status = default_assertion_status

    @property
    def registered_as_parallel_capable(self):
        """Gets the registered_as_parallel_capable of this ApplicationContextClassLoaderParent.  # noqa: E501


        :return: The registered_as_parallel_capable of this ApplicationContextClassLoaderParent.  # noqa: E501
        :rtype: bool
        """
        return self._registered_as_parallel_capable

    @registered_as_parallel_capable.setter
    def registered_as_parallel_capable(self, registered_as_parallel_capable):
        """Sets the registered_as_parallel_capable of this ApplicationContextClassLoaderParent.


        :param registered_as_parallel_capable: The registered_as_parallel_capable of this ApplicationContextClassLoaderParent.  # noqa: E501
        :type: bool
        """

        self._registered_as_parallel_capable = registered_as_parallel_capable

    @property
    def defined_packages(self):
        """Gets the defined_packages of this ApplicationContextClassLoaderParent.  # noqa: E501


        :return: The defined_packages of this ApplicationContextClassLoaderParent.  # noqa: E501
        :rtype: list[ApplicationContextClassLoaderParentUnnamedModuleClassLoaderDefinedPackages]
        """
        return self._defined_packages

    @defined_packages.setter
    def defined_packages(self, defined_packages):
        """Sets the defined_packages of this ApplicationContextClassLoaderParent.


        :param defined_packages: The defined_packages of this ApplicationContextClassLoaderParent.  # noqa: E501
        :type: list[ApplicationContextClassLoaderParentUnnamedModuleClassLoaderDefinedPackages]
        """

        self._defined_packages = defined_packages

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
        if not isinstance(other, ApplicationContextClassLoaderParent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplicationContextClassLoaderParent):
            return True

        return self.to_dict() != other.to_dict()
