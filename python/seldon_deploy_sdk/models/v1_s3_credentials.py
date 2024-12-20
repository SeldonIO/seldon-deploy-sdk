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


class V1S3Credentials(object):
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
        's3_access_key_id': 'str',
        's3_secret_access_key': 'str'
    }

    attribute_map = {
        's3_access_key_id': 's3AccessKeyId',
        's3_secret_access_key': 's3SecretAccessKey'
    }

    def __init__(self, s3_access_key_id=None, s3_secret_access_key=None):  # noqa: E501
        """V1S3Credentials - a model defined in Swagger"""  # noqa: E501

        self._s3_access_key_id = None
        self._s3_secret_access_key = None
        self.discriminator = None

        if s3_access_key_id is not None:
            self.s3_access_key_id = s3_access_key_id
        if s3_secret_access_key is not None:
            self.s3_secret_access_key = s3_secret_access_key

    @property
    def s3_access_key_id(self):
        """Gets the s3_access_key_id of this V1S3Credentials.  # noqa: E501

        The S3 access key ID.  # noqa: E501

        :return: The s3_access_key_id of this V1S3Credentials.  # noqa: E501
        :rtype: str
        """
        return self._s3_access_key_id

    @s3_access_key_id.setter
    def s3_access_key_id(self, s3_access_key_id):
        """Sets the s3_access_key_id of this V1S3Credentials.

        The S3 access key ID.  # noqa: E501

        :param s3_access_key_id: The s3_access_key_id of this V1S3Credentials.  # noqa: E501
        :type: str
        """

        self._s3_access_key_id = s3_access_key_id

    @property
    def s3_secret_access_key(self):
        """Gets the s3_secret_access_key of this V1S3Credentials.  # noqa: E501

        The S3 secret access key.  # noqa: E501

        :return: The s3_secret_access_key of this V1S3Credentials.  # noqa: E501
        :rtype: str
        """
        return self._s3_secret_access_key

    @s3_secret_access_key.setter
    def s3_secret_access_key(self, s3_secret_access_key):
        """Sets the s3_secret_access_key of this V1S3Credentials.

        The S3 secret access key.  # noqa: E501

        :param s3_secret_access_key: The s3_secret_access_key of this V1S3Credentials.  # noqa: E501
        :type: str
        """

        self._s3_secret_access_key = s3_secret_access_key

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
        if issubclass(V1S3Credentials, dict):
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
        if not isinstance(other, V1S3Credentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
