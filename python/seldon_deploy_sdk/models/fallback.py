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


class Fallback(object):
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
        'failure_threshold': 'int',
        'replicas': 'int'
    }

    attribute_map = {
        'failure_threshold': 'failureThreshold',
        'replicas': 'replicas'
    }

    def __init__(self, failure_threshold=None, replicas=None):  # noqa: E501
        """Fallback - a model defined in Swagger"""  # noqa: E501

        self._failure_threshold = None
        self._replicas = None
        self.discriminator = None

        if failure_threshold is not None:
            self.failure_threshold = failure_threshold
        if replicas is not None:
            self.replicas = replicas

    @property
    def failure_threshold(self):
        """Gets the failure_threshold of this Fallback.  # noqa: E501


        :return: The failure_threshold of this Fallback.  # noqa: E501
        :rtype: int
        """
        return self._failure_threshold

    @failure_threshold.setter
    def failure_threshold(self, failure_threshold):
        """Sets the failure_threshold of this Fallback.


        :param failure_threshold: The failure_threshold of this Fallback.  # noqa: E501
        :type: int
        """

        self._failure_threshold = failure_threshold

    @property
    def replicas(self):
        """Gets the replicas of this Fallback.  # noqa: E501


        :return: The replicas of this Fallback.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this Fallback.


        :param replicas: The replicas of this Fallback.  # noqa: E501
        :type: int
        """

        self._replicas = replicas

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
        if issubclass(Fallback, dict):
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
        if not isinstance(other, Fallback):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
