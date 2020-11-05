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


class Batcher(object):
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
        'max_batch_size': 'int',
        'max_latency': 'int',
        'timeout': 'int'
    }

    attribute_map = {
        'max_batch_size': 'maxBatchSize',
        'max_latency': 'maxLatency',
        'timeout': 'timeout'
    }

    def __init__(self, max_batch_size=None, max_latency=None, timeout=None):  # noqa: E501
        """Batcher - a model defined in Swagger"""  # noqa: E501

        self._max_batch_size = None
        self._max_latency = None
        self._timeout = None
        self.discriminator = None

        if max_batch_size is not None:
            self.max_batch_size = max_batch_size
        if max_latency is not None:
            self.max_latency = max_latency
        if timeout is not None:
            self.timeout = timeout

    @property
    def max_batch_size(self):
        """Gets the max_batch_size of this Batcher.  # noqa: E501

        MaxBatchSize of batcher service +optional  # noqa: E501

        :return: The max_batch_size of this Batcher.  # noqa: E501
        :rtype: int
        """
        return self._max_batch_size

    @max_batch_size.setter
    def max_batch_size(self, max_batch_size):
        """Sets the max_batch_size of this Batcher.

        MaxBatchSize of batcher service +optional  # noqa: E501

        :param max_batch_size: The max_batch_size of this Batcher.  # noqa: E501
        :type: int
        """

        self._max_batch_size = max_batch_size

    @property
    def max_latency(self):
        """Gets the max_latency of this Batcher.  # noqa: E501

        MaxLatency of batcher service +optional  # noqa: E501

        :return: The max_latency of this Batcher.  # noqa: E501
        :rtype: int
        """
        return self._max_latency

    @max_latency.setter
    def max_latency(self, max_latency):
        """Sets the max_latency of this Batcher.

        MaxLatency of batcher service +optional  # noqa: E501

        :param max_latency: The max_latency of this Batcher.  # noqa: E501
        :type: int
        """

        self._max_latency = max_latency

    @property
    def timeout(self):
        """Gets the timeout of this Batcher.  # noqa: E501

        Timeout of batcher service +optional  # noqa: E501

        :return: The timeout of this Batcher.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this Batcher.

        Timeout of batcher service +optional  # noqa: E501

        :param timeout: The timeout of this Batcher.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

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
        if issubclass(Batcher, dict):
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
        if not isinstance(other, Batcher):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
