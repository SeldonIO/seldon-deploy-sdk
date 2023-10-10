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


class Body1(object):
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
        'predictor_name': 'str',
        'container_name': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'limit': 'int',
        'page_token': 'str'
    }

    attribute_map = {
        'predictor_name': 'predictorName',
        'container_name': 'containerName',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'limit': 'limit',
        'page_token': 'pageToken'
    }

    def __init__(self, predictor_name=None, container_name=None, start_time=None, end_time=None, limit=None, page_token=None):  # noqa: E501
        """Body1 - a model defined in Swagger"""  # noqa: E501

        self._predictor_name = None
        self._container_name = None
        self._start_time = None
        self._end_time = None
        self._limit = None
        self._page_token = None
        self.discriminator = None

        self.predictor_name = predictor_name
        self.container_name = container_name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if limit is not None:
            self.limit = limit
        if page_token is not None:
            self.page_token = page_token

    @property
    def predictor_name(self):
        """Gets the predictor_name of this Body1.  # noqa: E501

        The predictor name of the seldon deployment to get inference logs for. e.g. \"default\", \"canary\", \"shadow\"  # noqa: E501

        :return: The predictor_name of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._predictor_name

    @predictor_name.setter
    def predictor_name(self, predictor_name):
        """Sets the predictor_name of this Body1.

        The predictor name of the seldon deployment to get inference logs for. e.g. \"default\", \"canary\", \"shadow\"  # noqa: E501

        :param predictor_name: The predictor_name of this Body1.  # noqa: E501
        :type: str
        """
        if predictor_name is None:
            raise ValueError("Invalid value for `predictor_name`, must not be `None`")  # noqa: E501

        self._predictor_name = predictor_name

    @property
    def container_name(self):
        """Gets the container_name of this Body1.  # noqa: E501

        The container name of the seldon deployment to get inference logs for. e.g. \"my-container\", \"input-transformer\", \"output-transformer\"  # noqa: E501

        :return: The container_name of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        """Sets the container_name of this Body1.

        The container name of the seldon deployment to get inference logs for. e.g. \"my-container\", \"input-transformer\", \"output-transformer\"  # noqa: E501

        :param container_name: The container_name of this Body1.  # noqa: E501
        :type: str
        """
        if container_name is None:
            raise ValueError("Invalid value for `container_name`, must not be `None`")  # noqa: E501

        self._container_name = container_name

    @property
    def start_time(self):
        """Gets the start_time of this Body1.  # noqa: E501

        The start time of the inference logs to get.  # noqa: E501

        :return: The start_time of this Body1.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Body1.

        The start time of the inference logs to get.  # noqa: E501

        :param start_time: The start_time of this Body1.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this Body1.  # noqa: E501

        The end time of the inference logs to get.  # noqa: E501

        :return: The end_time of this Body1.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Body1.

        The end time of the inference logs to get.  # noqa: E501

        :param end_time: The end_time of this Body1.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def limit(self):
        """Gets the limit of this Body1.  # noqa: E501

        The maximum number of inference logs to get.  # noqa: E501

        :return: The limit of this Body1.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this Body1.

        The maximum number of inference logs to get.  # noqa: E501

        :param limit: The limit of this Body1.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def page_token(self):
        """Gets the page_token of this Body1.  # noqa: E501

        The page token to use to get the next page of inference logs.  # noqa: E501

        :return: The page_token of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._page_token

    @page_token.setter
    def page_token(self, page_token):
        """Sets the page_token of this Body1.

        The page token to use to get the next page of inference logs.  # noqa: E501

        :param page_token: The page_token of this Body1.  # noqa: E501
        :type: str
        """

        self._page_token = page_token

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
        if issubclass(Body1, dict):
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
        if not isinstance(other, Body1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
