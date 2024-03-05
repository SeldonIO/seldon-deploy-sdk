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


class Lifecycle(object):
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
        'post_start': 'LifecycleHandler',
        'pre_stop': 'LifecycleHandler'
    }

    attribute_map = {
        'post_start': 'postStart',
        'pre_stop': 'preStop'
    }

    def __init__(self, post_start=None, pre_stop=None):  # noqa: E501
        """Lifecycle - a model defined in Swagger"""  # noqa: E501

        self._post_start = None
        self._pre_stop = None
        self.discriminator = None

        if post_start is not None:
            self.post_start = post_start
        if pre_stop is not None:
            self.pre_stop = pre_stop

    @property
    def post_start(self):
        """Gets the post_start of this Lifecycle.  # noqa: E501


        :return: The post_start of this Lifecycle.  # noqa: E501
        :rtype: LifecycleHandler
        """
        return self._post_start

    @post_start.setter
    def post_start(self, post_start):
        """Sets the post_start of this Lifecycle.


        :param post_start: The post_start of this Lifecycle.  # noqa: E501
        :type: LifecycleHandler
        """

        self._post_start = post_start

    @property
    def pre_stop(self):
        """Gets the pre_stop of this Lifecycle.  # noqa: E501


        :return: The pre_stop of this Lifecycle.  # noqa: E501
        :rtype: LifecycleHandler
        """
        return self._pre_stop

    @pre_stop.setter
    def pre_stop(self, pre_stop):
        """Sets the pre_stop of this Lifecycle.


        :param pre_stop: The pre_stop of this Lifecycle.  # noqa: E501
        :type: LifecycleHandler
        """

        self._pre_stop = pre_stop

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
        if issubclass(Lifecycle, dict):
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
        if not isinstance(other, Lifecycle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
