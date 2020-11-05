# coding: utf-8

"""
    Seldon-Deploy API.

    Documentation of Seldon-Deploy API.  # noqa: E501

    OpenAPI spec version: v1alpha1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class HorizontalPodAutoscalerConfig(object):
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
        'behavior': 'HorizontalPodAutoscalerBehavior',
        'resource_metrics': 'list[ResourceMetricSource]'
    }

    attribute_map = {
        'behavior': 'behavior',
        'resource_metrics': 'resourceMetrics'
    }

    def __init__(self, behavior=None, resource_metrics=None):  # noqa: E501
        """HorizontalPodAutoscalerConfig - a model defined in Swagger"""  # noqa: E501

        self._behavior = None
        self._resource_metrics = None
        self.discriminator = None

        if behavior is not None:
            self.behavior = behavior
        if resource_metrics is not None:
            self.resource_metrics = resource_metrics

    @property
    def behavior(self):
        """Gets the behavior of this HorizontalPodAutoscalerConfig.  # noqa: E501


        :return: The behavior of this HorizontalPodAutoscalerConfig.  # noqa: E501
        :rtype: HorizontalPodAutoscalerBehavior
        """
        return self._behavior

    @behavior.setter
    def behavior(self, behavior):
        """Sets the behavior of this HorizontalPodAutoscalerConfig.


        :param behavior: The behavior of this HorizontalPodAutoscalerConfig.  # noqa: E501
        :type: HorizontalPodAutoscalerBehavior
        """

        self._behavior = behavior

    @property
    def resource_metrics(self):
        """Gets the resource_metrics of this HorizontalPodAutoscalerConfig.  # noqa: E501


        :return: The resource_metrics of this HorizontalPodAutoscalerConfig.  # noqa: E501
        :rtype: list[ResourceMetricSource]
        """
        return self._resource_metrics

    @resource_metrics.setter
    def resource_metrics(self, resource_metrics):
        """Sets the resource_metrics of this HorizontalPodAutoscalerConfig.


        :param resource_metrics: The resource_metrics of this HorizontalPodAutoscalerConfig.  # noqa: E501
        :type: list[ResourceMetricSource]
        """

        self._resource_metrics = resource_metrics

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
        if issubclass(HorizontalPodAutoscalerConfig, dict):
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
        if not isinstance(other, HorizontalPodAutoscalerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
