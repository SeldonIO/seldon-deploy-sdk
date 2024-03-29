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


class FeatureDistributionBucket(object):
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
        'count': 'float',
        'distribution': 'FeatureDistribution',
        'key': 'str'
    }

    attribute_map = {
        'count': 'count',
        'distribution': 'distribution',
        'key': 'key'
    }

    def __init__(self, count=None, distribution=None, key=None):  # noqa: E501
        """FeatureDistributionBucket - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._distribution = None
        self._key = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if distribution is not None:
            self.distribution = distribution
        if key is not None:
            self.key = key

    @property
    def count(self):
        """Gets the count of this FeatureDistributionBucket.  # noqa: E501

        Bucket Count in a feature distribution  # noqa: E501

        :return: The count of this FeatureDistributionBucket.  # noqa: E501
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this FeatureDistributionBucket.

        Bucket Count in a feature distribution  # noqa: E501

        :param count: The count of this FeatureDistributionBucket.  # noqa: E501
        :type: float
        """

        self._count = count

    @property
    def distribution(self):
        """Gets the distribution of this FeatureDistributionBucket.  # noqa: E501


        :return: The distribution of this FeatureDistributionBucket.  # noqa: E501
        :rtype: FeatureDistribution
        """
        return self._distribution

    @distribution.setter
    def distribution(self, distribution):
        """Sets the distribution of this FeatureDistributionBucket.


        :param distribution: The distribution of this FeatureDistributionBucket.  # noqa: E501
        :type: FeatureDistribution
        """

        self._distribution = distribution

    @property
    def key(self):
        """Gets the key of this FeatureDistributionBucket.  # noqa: E501

        Bucket Key in a feature distribution  # noqa: E501

        :return: The key of this FeatureDistributionBucket.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this FeatureDistributionBucket.

        Bucket Key in a feature distribution  # noqa: E501

        :param key: The key of this FeatureDistributionBucket.  # noqa: E501
        :type: str
        """

        self._key = key

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
        if issubclass(FeatureDistributionBucket, dict):
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
        if not isinstance(other, FeatureDistributionBucket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
