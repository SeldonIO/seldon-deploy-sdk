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


class V1ListDeploymentInferenceLogsResponse(object):
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
        'inference_logs': 'list[V1InferenceLogsDeploymentItem]'
    }

    attribute_map = {
        'inference_logs': 'inferenceLogs'
    }

    def __init__(self, inference_logs=None):  # noqa: E501
        """V1ListDeploymentInferenceLogsResponse - a model defined in Swagger"""  # noqa: E501

        self._inference_logs = None
        self.discriminator = None

        if inference_logs is not None:
            self.inference_logs = inference_logs

    @property
    def inference_logs(self):
        """Gets the inference_logs of this V1ListDeploymentInferenceLogsResponse.  # noqa: E501


        :return: The inference_logs of this V1ListDeploymentInferenceLogsResponse.  # noqa: E501
        :rtype: list[V1InferenceLogsDeploymentItem]
        """
        return self._inference_logs

    @inference_logs.setter
    def inference_logs(self, inference_logs):
        """Sets the inference_logs of this V1ListDeploymentInferenceLogsResponse.


        :param inference_logs: The inference_logs of this V1ListDeploymentInferenceLogsResponse.  # noqa: E501
        :type: list[V1InferenceLogsDeploymentItem]
        """

        self._inference_logs = inference_logs

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
        if issubclass(V1ListDeploymentInferenceLogsResponse, dict):
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
        if not isinstance(other, V1ListDeploymentInferenceLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
