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


class GitRepoVolumeSource(object):
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
        'directory': 'str',
        'repository': 'str',
        'revision': 'str'
    }

    attribute_map = {
        'directory': 'directory',
        'repository': 'repository',
        'revision': 'revision'
    }

    def __init__(self, directory=None, repository=None, revision=None):  # noqa: E501
        """GitRepoVolumeSource - a model defined in Swagger"""  # noqa: E501

        self._directory = None
        self._repository = None
        self._revision = None
        self.discriminator = None

        if directory is not None:
            self.directory = directory
        if repository is not None:
            self.repository = repository
        if revision is not None:
            self.revision = revision

    @property
    def directory(self):
        """Gets the directory of this GitRepoVolumeSource.  # noqa: E501

        directory is the target directory name. Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name. +optional  # noqa: E501

        :return: The directory of this GitRepoVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """Sets the directory of this GitRepoVolumeSource.

        directory is the target directory name. Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name. +optional  # noqa: E501

        :param directory: The directory of this GitRepoVolumeSource.  # noqa: E501
        :type: str
        """

        self._directory = directory

    @property
    def repository(self):
        """Gets the repository of this GitRepoVolumeSource.  # noqa: E501

        repository is the URL  # noqa: E501

        :return: The repository of this GitRepoVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this GitRepoVolumeSource.

        repository is the URL  # noqa: E501

        :param repository: The repository of this GitRepoVolumeSource.  # noqa: E501
        :type: str
        """

        self._repository = repository

    @property
    def revision(self):
        """Gets the revision of this GitRepoVolumeSource.  # noqa: E501

        revision is the commit hash for the specified revision. +optional  # noqa: E501

        :return: The revision of this GitRepoVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this GitRepoVolumeSource.

        revision is the commit hash for the specified revision. +optional  # noqa: E501

        :param revision: The revision of this GitRepoVolumeSource.  # noqa: E501
        :type: str
        """

        self._revision = revision

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
        if issubclass(GitRepoVolumeSource, dict):
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
        if not isinstance(other, GitRepoVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
