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


class RedirectView(object):
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
        'application_context': 'ApplicationContext',
        'servlet_context': 'RedirectViewServletContext',
        'content_type': 'str',
        'request_context_attribute': 'str',
        'static_attributes': 'dict(str, object)',
        'expose_path_variables': 'bool',
        'expose_context_beans_as_attributes': 'bool',
        'exposed_context_bean_names': 'list[str]',
        'bean_name': 'str',
        'url': 'str',
        'context_relative': 'bool',
        'http10_compatible': 'bool',
        'expose_model_attributes': 'bool',
        'encoding_scheme': 'str',
        'status_code': 'str',
        'expand_uri_template_variables': 'bool',
        'propagate_query_params': 'bool',
        'hosts': 'list[str]',
        'propagate_query_properties': 'bool',
        'redirect_view': 'bool',
        'attributes_map': 'dict(str, object)',
        'attributes_csv': 'str',
        'attributes': 'dict(str, str)'
    }

    attribute_map = {
        'application_context': 'applicationContext',
        'servlet_context': 'servletContext',
        'content_type': 'contentType',
        'request_context_attribute': 'requestContextAttribute',
        'static_attributes': 'staticAttributes',
        'expose_path_variables': 'exposePathVariables',
        'expose_context_beans_as_attributes': 'exposeContextBeansAsAttributes',
        'exposed_context_bean_names': 'exposedContextBeanNames',
        'bean_name': 'beanName',
        'url': 'url',
        'context_relative': 'contextRelative',
        'http10_compatible': 'http10Compatible',
        'expose_model_attributes': 'exposeModelAttributes',
        'encoding_scheme': 'encodingScheme',
        'status_code': 'statusCode',
        'expand_uri_template_variables': 'expandUriTemplateVariables',
        'propagate_query_params': 'propagateQueryParams',
        'hosts': 'hosts',
        'propagate_query_properties': 'propagateQueryProperties',
        'redirect_view': 'redirectView',
        'attributes_map': 'attributesMap',
        'attributes_csv': 'attributesCSV',
        'attributes': 'attributes'
    }

    def __init__(self, application_context=None, servlet_context=None, content_type=None, request_context_attribute=None, static_attributes=None, expose_path_variables=None, expose_context_beans_as_attributes=None, exposed_context_bean_names=None, bean_name=None, url=None, context_relative=None, http10_compatible=None, expose_model_attributes=None, encoding_scheme=None, status_code=None, expand_uri_template_variables=None, propagate_query_params=None, hosts=None, propagate_query_properties=None, redirect_view=None, attributes_map=None, attributes_csv=None, attributes=None, local_vars_configuration=None):  # noqa: E501
        """RedirectView - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._application_context = None
        self._servlet_context = None
        self._content_type = None
        self._request_context_attribute = None
        self._static_attributes = None
        self._expose_path_variables = None
        self._expose_context_beans_as_attributes = None
        self._exposed_context_bean_names = None
        self._bean_name = None
        self._url = None
        self._context_relative = None
        self._http10_compatible = None
        self._expose_model_attributes = None
        self._encoding_scheme = None
        self._status_code = None
        self._expand_uri_template_variables = None
        self._propagate_query_params = None
        self._hosts = None
        self._propagate_query_properties = None
        self._redirect_view = None
        self._attributes_map = None
        self._attributes_csv = None
        self._attributes = None
        self.discriminator = None

        if application_context is not None:
            self.application_context = application_context
        if servlet_context is not None:
            self.servlet_context = servlet_context
        if content_type is not None:
            self.content_type = content_type
        if request_context_attribute is not None:
            self.request_context_attribute = request_context_attribute
        if static_attributes is not None:
            self.static_attributes = static_attributes
        if expose_path_variables is not None:
            self.expose_path_variables = expose_path_variables
        if expose_context_beans_as_attributes is not None:
            self.expose_context_beans_as_attributes = expose_context_beans_as_attributes
        if exposed_context_bean_names is not None:
            self.exposed_context_bean_names = exposed_context_bean_names
        if bean_name is not None:
            self.bean_name = bean_name
        if url is not None:
            self.url = url
        if context_relative is not None:
            self.context_relative = context_relative
        if http10_compatible is not None:
            self.http10_compatible = http10_compatible
        if expose_model_attributes is not None:
            self.expose_model_attributes = expose_model_attributes
        if encoding_scheme is not None:
            self.encoding_scheme = encoding_scheme
        if status_code is not None:
            self.status_code = status_code
        if expand_uri_template_variables is not None:
            self.expand_uri_template_variables = expand_uri_template_variables
        if propagate_query_params is not None:
            self.propagate_query_params = propagate_query_params
        if hosts is not None:
            self.hosts = hosts
        if propagate_query_properties is not None:
            self.propagate_query_properties = propagate_query_properties
        if redirect_view is not None:
            self.redirect_view = redirect_view
        if attributes_map is not None:
            self.attributes_map = attributes_map
        if attributes_csv is not None:
            self.attributes_csv = attributes_csv
        if attributes is not None:
            self.attributes = attributes

    @property
    def application_context(self):
        """Gets the application_context of this RedirectView.  # noqa: E501


        :return: The application_context of this RedirectView.  # noqa: E501
        :rtype: ApplicationContext
        """
        return self._application_context

    @application_context.setter
    def application_context(self, application_context):
        """Sets the application_context of this RedirectView.


        :param application_context: The application_context of this RedirectView.  # noqa: E501
        :type: ApplicationContext
        """

        self._application_context = application_context

    @property
    def servlet_context(self):
        """Gets the servlet_context of this RedirectView.  # noqa: E501


        :return: The servlet_context of this RedirectView.  # noqa: E501
        :rtype: RedirectViewServletContext
        """
        return self._servlet_context

    @servlet_context.setter
    def servlet_context(self, servlet_context):
        """Sets the servlet_context of this RedirectView.


        :param servlet_context: The servlet_context of this RedirectView.  # noqa: E501
        :type: RedirectViewServletContext
        """

        self._servlet_context = servlet_context

    @property
    def content_type(self):
        """Gets the content_type of this RedirectView.  # noqa: E501


        :return: The content_type of this RedirectView.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this RedirectView.


        :param content_type: The content_type of this RedirectView.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def request_context_attribute(self):
        """Gets the request_context_attribute of this RedirectView.  # noqa: E501


        :return: The request_context_attribute of this RedirectView.  # noqa: E501
        :rtype: str
        """
        return self._request_context_attribute

    @request_context_attribute.setter
    def request_context_attribute(self, request_context_attribute):
        """Sets the request_context_attribute of this RedirectView.


        :param request_context_attribute: The request_context_attribute of this RedirectView.  # noqa: E501
        :type: str
        """

        self._request_context_attribute = request_context_attribute

    @property
    def static_attributes(self):
        """Gets the static_attributes of this RedirectView.  # noqa: E501


        :return: The static_attributes of this RedirectView.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._static_attributes

    @static_attributes.setter
    def static_attributes(self, static_attributes):
        """Sets the static_attributes of this RedirectView.


        :param static_attributes: The static_attributes of this RedirectView.  # noqa: E501
        :type: dict(str, object)
        """

        self._static_attributes = static_attributes

    @property
    def expose_path_variables(self):
        """Gets the expose_path_variables of this RedirectView.  # noqa: E501


        :return: The expose_path_variables of this RedirectView.  # noqa: E501
        :rtype: bool
        """
        return self._expose_path_variables

    @expose_path_variables.setter
    def expose_path_variables(self, expose_path_variables):
        """Sets the expose_path_variables of this RedirectView.


        :param expose_path_variables: The expose_path_variables of this RedirectView.  # noqa: E501
        :type: bool
        """

        self._expose_path_variables = expose_path_variables

    @property
    def expose_context_beans_as_attributes(self):
        """Gets the expose_context_beans_as_attributes of this RedirectView.  # noqa: E501


        :return: The expose_context_beans_as_attributes of this RedirectView.  # noqa: E501
        :rtype: bool
        """
        return self._expose_context_beans_as_attributes

    @expose_context_beans_as_attributes.setter
    def expose_context_beans_as_attributes(self, expose_context_beans_as_attributes):
        """Sets the expose_context_beans_as_attributes of this RedirectView.


        :param expose_context_beans_as_attributes: The expose_context_beans_as_attributes of this RedirectView.  # noqa: E501
        :type: bool
        """

        self._expose_context_beans_as_attributes = expose_context_beans_as_attributes

    @property
    def exposed_context_bean_names(self):
        """Gets the exposed_context_bean_names of this RedirectView.  # noqa: E501


        :return: The exposed_context_bean_names of this RedirectView.  # noqa: E501
        :rtype: list[str]
        """
        return self._exposed_context_bean_names

    @exposed_context_bean_names.setter
    def exposed_context_bean_names(self, exposed_context_bean_names):
        """Sets the exposed_context_bean_names of this RedirectView.


        :param exposed_context_bean_names: The exposed_context_bean_names of this RedirectView.  # noqa: E501
        :type: list[str]
        """

        self._exposed_context_bean_names = exposed_context_bean_names

    @property
    def bean_name(self):
        """Gets the bean_name of this RedirectView.  # noqa: E501


        :return: The bean_name of this RedirectView.  # noqa: E501
        :rtype: str
        """
        return self._bean_name

    @bean_name.setter
    def bean_name(self, bean_name):
        """Sets the bean_name of this RedirectView.


        :param bean_name: The bean_name of this RedirectView.  # noqa: E501
        :type: str
        """

        self._bean_name = bean_name

    @property
    def url(self):
        """Gets the url of this RedirectView.  # noqa: E501


        :return: The url of this RedirectView.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RedirectView.


        :param url: The url of this RedirectView.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def context_relative(self):
        """Gets the context_relative of this RedirectView.  # noqa: E501


        :return: The context_relative of this RedirectView.  # noqa: E501
        :rtype: bool
        """
        return self._context_relative

    @context_relative.setter
    def context_relative(self, context_relative):
        """Sets the context_relative of this RedirectView.


        :param context_relative: The context_relative of this RedirectView.  # noqa: E501
        :type: bool
        """

        self._context_relative = context_relative

    @property
    def http10_compatible(self):
        """Gets the http10_compatible of this RedirectView.  # noqa: E501


        :return: The http10_compatible of this RedirectView.  # noqa: E501
        :rtype: bool
        """
        return self._http10_compatible

    @http10_compatible.setter
    def http10_compatible(self, http10_compatible):
        """Sets the http10_compatible of this RedirectView.


        :param http10_compatible: The http10_compatible of this RedirectView.  # noqa: E501
        :type: bool
        """

        self._http10_compatible = http10_compatible

    @property
    def expose_model_attributes(self):
        """Gets the expose_model_attributes of this RedirectView.  # noqa: E501


        :return: The expose_model_attributes of this RedirectView.  # noqa: E501
        :rtype: bool
        """
        return self._expose_model_attributes

    @expose_model_attributes.setter
    def expose_model_attributes(self, expose_model_attributes):
        """Sets the expose_model_attributes of this RedirectView.


        :param expose_model_attributes: The expose_model_attributes of this RedirectView.  # noqa: E501
        :type: bool
        """

        self._expose_model_attributes = expose_model_attributes

    @property
    def encoding_scheme(self):
        """Gets the encoding_scheme of this RedirectView.  # noqa: E501


        :return: The encoding_scheme of this RedirectView.  # noqa: E501
        :rtype: str
        """
        return self._encoding_scheme

    @encoding_scheme.setter
    def encoding_scheme(self, encoding_scheme):
        """Sets the encoding_scheme of this RedirectView.


        :param encoding_scheme: The encoding_scheme of this RedirectView.  # noqa: E501
        :type: str
        """

        self._encoding_scheme = encoding_scheme

    @property
    def status_code(self):
        """Gets the status_code of this RedirectView.  # noqa: E501


        :return: The status_code of this RedirectView.  # noqa: E501
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this RedirectView.


        :param status_code: The status_code of this RedirectView.  # noqa: E501
        :type: str
        """
        allowed_values = ["100 CONTINUE", "101 SWITCHING_PROTOCOLS", "102 PROCESSING", "103 CHECKPOINT", "200 OK", "201 CREATED", "202 ACCEPTED", "203 NON_AUTHORITATIVE_INFORMATION", "204 NO_CONTENT", "205 RESET_CONTENT", "206 PARTIAL_CONTENT", "207 MULTI_STATUS", "208 ALREADY_REPORTED", "226 IM_USED", "300 MULTIPLE_CHOICES", "301 MOVED_PERMANENTLY", "302 FOUND", "302 MOVED_TEMPORARILY", "303 SEE_OTHER", "304 NOT_MODIFIED", "305 USE_PROXY", "307 TEMPORARY_REDIRECT", "308 PERMANENT_REDIRECT", "400 BAD_REQUEST", "401 UNAUTHORIZED", "402 PAYMENT_REQUIRED", "403 FORBIDDEN", "404 NOT_FOUND", "405 METHOD_NOT_ALLOWED", "406 NOT_ACCEPTABLE", "407 PROXY_AUTHENTICATION_REQUIRED", "408 REQUEST_TIMEOUT", "409 CONFLICT", "410 GONE", "411 LENGTH_REQUIRED", "412 PRECONDITION_FAILED", "413 PAYLOAD_TOO_LARGE", "413 REQUEST_ENTITY_TOO_LARGE", "414 URI_TOO_LONG", "414 REQUEST_URI_TOO_LONG", "415 UNSUPPORTED_MEDIA_TYPE", "416 REQUESTED_RANGE_NOT_SATISFIABLE", "417 EXPECTATION_FAILED", "418 I_AM_A_TEAPOT", "419 INSUFFICIENT_SPACE_ON_RESOURCE", "420 METHOD_FAILURE", "421 DESTINATION_LOCKED", "422 UNPROCESSABLE_ENTITY", "423 LOCKED", "424 FAILED_DEPENDENCY", "425 TOO_EARLY", "426 UPGRADE_REQUIRED", "428 PRECONDITION_REQUIRED", "429 TOO_MANY_REQUESTS", "431 REQUEST_HEADER_FIELDS_TOO_LARGE", "451 UNAVAILABLE_FOR_LEGAL_REASONS", "500 INTERNAL_SERVER_ERROR", "501 NOT_IMPLEMENTED", "502 BAD_GATEWAY", "503 SERVICE_UNAVAILABLE", "504 GATEWAY_TIMEOUT", "505 HTTP_VERSION_NOT_SUPPORTED", "506 VARIANT_ALSO_NEGOTIATES", "507 INSUFFICIENT_STORAGE", "508 LOOP_DETECTED", "509 BANDWIDTH_LIMIT_EXCEEDED", "510 NOT_EXTENDED", "511 NETWORK_AUTHENTICATION_REQUIRED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status_code not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status_code` ({0}), must be one of {1}"  # noqa: E501
                .format(status_code, allowed_values)
            )

        self._status_code = status_code

    @property
    def expand_uri_template_variables(self):
        """Gets the expand_uri_template_variables of this RedirectView.  # noqa: E501


        :return: The expand_uri_template_variables of this RedirectView.  # noqa: E501
        :rtype: bool
        """
        return self._expand_uri_template_variables

    @expand_uri_template_variables.setter
    def expand_uri_template_variables(self, expand_uri_template_variables):
        """Sets the expand_uri_template_variables of this RedirectView.


        :param expand_uri_template_variables: The expand_uri_template_variables of this RedirectView.  # noqa: E501
        :type: bool
        """

        self._expand_uri_template_variables = expand_uri_template_variables

    @property
    def propagate_query_params(self):
        """Gets the propagate_query_params of this RedirectView.  # noqa: E501


        :return: The propagate_query_params of this RedirectView.  # noqa: E501
        :rtype: bool
        """
        return self._propagate_query_params

    @propagate_query_params.setter
    def propagate_query_params(self, propagate_query_params):
        """Sets the propagate_query_params of this RedirectView.


        :param propagate_query_params: The propagate_query_params of this RedirectView.  # noqa: E501
        :type: bool
        """

        self._propagate_query_params = propagate_query_params

    @property
    def hosts(self):
        """Gets the hosts of this RedirectView.  # noqa: E501


        :return: The hosts of this RedirectView.  # noqa: E501
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this RedirectView.


        :param hosts: The hosts of this RedirectView.  # noqa: E501
        :type: list[str]
        """

        self._hosts = hosts

    @property
    def propagate_query_properties(self):
        """Gets the propagate_query_properties of this RedirectView.  # noqa: E501


        :return: The propagate_query_properties of this RedirectView.  # noqa: E501
        :rtype: bool
        """
        return self._propagate_query_properties

    @propagate_query_properties.setter
    def propagate_query_properties(self, propagate_query_properties):
        """Sets the propagate_query_properties of this RedirectView.


        :param propagate_query_properties: The propagate_query_properties of this RedirectView.  # noqa: E501
        :type: bool
        """

        self._propagate_query_properties = propagate_query_properties

    @property
    def redirect_view(self):
        """Gets the redirect_view of this RedirectView.  # noqa: E501


        :return: The redirect_view of this RedirectView.  # noqa: E501
        :rtype: bool
        """
        return self._redirect_view

    @redirect_view.setter
    def redirect_view(self, redirect_view):
        """Sets the redirect_view of this RedirectView.


        :param redirect_view: The redirect_view of this RedirectView.  # noqa: E501
        :type: bool
        """

        self._redirect_view = redirect_view

    @property
    def attributes_map(self):
        """Gets the attributes_map of this RedirectView.  # noqa: E501


        :return: The attributes_map of this RedirectView.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._attributes_map

    @attributes_map.setter
    def attributes_map(self, attributes_map):
        """Sets the attributes_map of this RedirectView.


        :param attributes_map: The attributes_map of this RedirectView.  # noqa: E501
        :type: dict(str, object)
        """

        self._attributes_map = attributes_map

    @property
    def attributes_csv(self):
        """Gets the attributes_csv of this RedirectView.  # noqa: E501


        :return: The attributes_csv of this RedirectView.  # noqa: E501
        :rtype: str
        """
        return self._attributes_csv

    @attributes_csv.setter
    def attributes_csv(self, attributes_csv):
        """Sets the attributes_csv of this RedirectView.


        :param attributes_csv: The attributes_csv of this RedirectView.  # noqa: E501
        :type: str
        """

        self._attributes_csv = attributes_csv

    @property
    def attributes(self):
        """Gets the attributes of this RedirectView.  # noqa: E501


        :return: The attributes of this RedirectView.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this RedirectView.


        :param attributes: The attributes of this RedirectView.  # noqa: E501
        :type: dict(str, str)
        """

        self._attributes = attributes

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
        if not isinstance(other, RedirectView):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RedirectView):
            return True

        return self.to_dict() != other.to_dict()
