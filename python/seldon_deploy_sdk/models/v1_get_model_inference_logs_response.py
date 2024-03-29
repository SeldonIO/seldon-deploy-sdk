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


class V1GetModelInferenceLogsResponse(object):
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
        'namespace': 'str',
        'pipeline_name': 'str',
        'model_name': 'str',
        'payloads': 'list[V1InferenceLogsRawPayload]',
        'next_page_token': 'str',
        'total_count': 'int'
    }

    attribute_map = {
        'namespace': 'namespace',
        'pipeline_name': 'pipelineName',
        'model_name': 'modelName',
        'payloads': 'payloads',
        'next_page_token': 'nextPageToken',
        'total_count': 'totalCount'
    }

    def __init__(self, namespace=None, pipeline_name=None, model_name=None, payloads=None, next_page_token=None, total_count=None):  # noqa: E501
        """V1GetModelInferenceLogsResponse - a model defined in Swagger"""  # noqa: E501

        self._namespace = None
        self._pipeline_name = None
        self._model_name = None
        self._payloads = None
        self._next_page_token = None
        self._total_count = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if pipeline_name is not None:
            self.pipeline_name = pipeline_name
        if model_name is not None:
            self.model_name = model_name
        if payloads is not None:
            self.payloads = payloads
        if next_page_token is not None:
            self.next_page_token = next_page_token
        if total_count is not None:
            self.total_count = total_count

    @property
    def namespace(self):
        """Gets the namespace of this V1GetModelInferenceLogsResponse.  # noqa: E501


        :return: The namespace of this V1GetModelInferenceLogsResponse.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this V1GetModelInferenceLogsResponse.


        :param namespace: The namespace of this V1GetModelInferenceLogsResponse.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def pipeline_name(self):
        """Gets the pipeline_name of this V1GetModelInferenceLogsResponse.  # noqa: E501


        :return: The pipeline_name of this V1GetModelInferenceLogsResponse.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_name

    @pipeline_name.setter
    def pipeline_name(self, pipeline_name):
        """Sets the pipeline_name of this V1GetModelInferenceLogsResponse.


        :param pipeline_name: The pipeline_name of this V1GetModelInferenceLogsResponse.  # noqa: E501
        :type: str
        """

        self._pipeline_name = pipeline_name

    @property
    def model_name(self):
        """Gets the model_name of this V1GetModelInferenceLogsResponse.  # noqa: E501


        :return: The model_name of this V1GetModelInferenceLogsResponse.  # noqa: E501
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        """Sets the model_name of this V1GetModelInferenceLogsResponse.


        :param model_name: The model_name of this V1GetModelInferenceLogsResponse.  # noqa: E501
        :type: str
        """

        self._model_name = model_name

    @property
    def payloads(self):
        """Gets the payloads of this V1GetModelInferenceLogsResponse.  # noqa: E501


        :return: The payloads of this V1GetModelInferenceLogsResponse.  # noqa: E501
        :rtype: list[V1InferenceLogsRawPayload]
        """
        return self._payloads

    @payloads.setter
    def payloads(self, payloads):
        """Sets the payloads of this V1GetModelInferenceLogsResponse.


        :param payloads: The payloads of this V1GetModelInferenceLogsResponse.  # noqa: E501
        :type: list[V1InferenceLogsRawPayload]
        """

        self._payloads = payloads

    @property
    def next_page_token(self):
        """Gets the next_page_token of this V1GetModelInferenceLogsResponse.  # noqa: E501


        :return: The next_page_token of this V1GetModelInferenceLogsResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this V1GetModelInferenceLogsResponse.


        :param next_page_token: The next_page_token of this V1GetModelInferenceLogsResponse.  # noqa: E501
        :type: str
        """

        self._next_page_token = next_page_token

    @property
    def total_count(self):
        """Gets the total_count of this V1GetModelInferenceLogsResponse.  # noqa: E501


        :return: The total_count of this V1GetModelInferenceLogsResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this V1GetModelInferenceLogsResponse.


        :param total_count: The total_count of this V1GetModelInferenceLogsResponse.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

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
        if issubclass(V1GetModelInferenceLogsResponse, dict):
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
        if not isinstance(other, V1GetModelInferenceLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
