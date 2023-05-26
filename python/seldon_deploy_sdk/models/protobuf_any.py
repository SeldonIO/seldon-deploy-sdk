# coding: utf-8

"""
    Seldon Deploy API

    API to interact and manage the lifecycle of your machine learning models deployed through Seldon Deploy.  # noqa: E501

    OpenAPI spec version: v1alpha1
    Contact: hello@seldon.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ProtobufAny(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type_url': 'str',
        'value': 'str'
    }

    attribute_map = {
        'type_url': 'typeUrl',
        'value': 'value'
    }

    def __init__(self, type_url=None, value=None):  # noqa: E501
        """ProtobufAny - a model defined in Swagger"""  # noqa: E501

        self._type_url = None
        self._value = None
        self.discriminator = None

        if type_url is not None:
            self.type_url = type_url
        if value is not None:
            self.value = value

    @property
    def type_url(self):
        """Gets the type_url of this ProtobufAny.  # noqa: E501


        :return: The type_url of this ProtobufAny.  # noqa: E501
        :rtype: str
        """
        return self._type_url

    @type_url.setter
    def type_url(self, type_url):
        """Sets the type_url of this ProtobufAny.


        :param type_url: The type_url of this ProtobufAny.  # noqa: E501
        :type: str
        """

        self._type_url = type_url

    @property
    def value(self):
        """Gets the value of this ProtobufAny.  # noqa: E501


        :return: The value of this ProtobufAny.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ProtobufAny.


        :param value: The value of this ProtobufAny.  # noqa: E501
        :type: str
        """
        if value is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', value):  # noqa: E501
            raise ValueError(r"Invalid value for `value`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._value = value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ProtobufAny, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProtobufAny):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
