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


class SeldonPodSpec(object):
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
        'hpa_spec': 'SeldonHpaSpec',
        'keda_spec': 'SeldonScaledObjectSpec',
        'metadata': 'ObjectMeta',
        'pdb_spec': 'SeldonPdbSpec',
        'replicas': 'int',
        'spec': 'PodSpec'
    }

    attribute_map = {
        'hpa_spec': 'hpaSpec',
        'keda_spec': 'kedaSpec',
        'metadata': 'metadata',
        'pdb_spec': 'pdbSpec',
        'replicas': 'replicas',
        'spec': 'spec'
    }

    def __init__(self, hpa_spec=None, keda_spec=None, metadata=None, pdb_spec=None, replicas=None, spec=None):  # noqa: E501
        """SeldonPodSpec - a model defined in Swagger"""  # noqa: E501

        self._hpa_spec = None
        self._keda_spec = None
        self._metadata = None
        self._pdb_spec = None
        self._replicas = None
        self._spec = None
        self.discriminator = None

        if hpa_spec is not None:
            self.hpa_spec = hpa_spec
        if keda_spec is not None:
            self.keda_spec = keda_spec
        if metadata is not None:
            self.metadata = metadata
        if pdb_spec is not None:
            self.pdb_spec = pdb_spec
        if replicas is not None:
            self.replicas = replicas
        if spec is not None:
            self.spec = spec

    @property
    def hpa_spec(self):
        """Gets the hpa_spec of this SeldonPodSpec.  # noqa: E501


        :return: The hpa_spec of this SeldonPodSpec.  # noqa: E501
        :rtype: SeldonHpaSpec
        """
        return self._hpa_spec

    @hpa_spec.setter
    def hpa_spec(self, hpa_spec):
        """Sets the hpa_spec of this SeldonPodSpec.


        :param hpa_spec: The hpa_spec of this SeldonPodSpec.  # noqa: E501
        :type: SeldonHpaSpec
        """

        self._hpa_spec = hpa_spec

    @property
    def keda_spec(self):
        """Gets the keda_spec of this SeldonPodSpec.  # noqa: E501


        :return: The keda_spec of this SeldonPodSpec.  # noqa: E501
        :rtype: SeldonScaledObjectSpec
        """
        return self._keda_spec

    @keda_spec.setter
    def keda_spec(self, keda_spec):
        """Sets the keda_spec of this SeldonPodSpec.


        :param keda_spec: The keda_spec of this SeldonPodSpec.  # noqa: E501
        :type: SeldonScaledObjectSpec
        """

        self._keda_spec = keda_spec

    @property
    def metadata(self):
        """Gets the metadata of this SeldonPodSpec.  # noqa: E501


        :return: The metadata of this SeldonPodSpec.  # noqa: E501
        :rtype: ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this SeldonPodSpec.


        :param metadata: The metadata of this SeldonPodSpec.  # noqa: E501
        :type: ObjectMeta
        """

        self._metadata = metadata

    @property
    def pdb_spec(self):
        """Gets the pdb_spec of this SeldonPodSpec.  # noqa: E501


        :return: The pdb_spec of this SeldonPodSpec.  # noqa: E501
        :rtype: SeldonPdbSpec
        """
        return self._pdb_spec

    @pdb_spec.setter
    def pdb_spec(self, pdb_spec):
        """Sets the pdb_spec of this SeldonPodSpec.


        :param pdb_spec: The pdb_spec of this SeldonPodSpec.  # noqa: E501
        :type: SeldonPdbSpec
        """

        self._pdb_spec = pdb_spec

    @property
    def replicas(self):
        """Gets the replicas of this SeldonPodSpec.  # noqa: E501


        :return: The replicas of this SeldonPodSpec.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this SeldonPodSpec.


        :param replicas: The replicas of this SeldonPodSpec.  # noqa: E501
        :type: int
        """

        self._replicas = replicas

    @property
    def spec(self):
        """Gets the spec of this SeldonPodSpec.  # noqa: E501


        :return: The spec of this SeldonPodSpec.  # noqa: E501
        :rtype: PodSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this SeldonPodSpec.


        :param spec: The spec of this SeldonPodSpec.  # noqa: E501
        :type: PodSpec
        """

        self._spec = spec

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
        if issubclass(SeldonPodSpec, dict):
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
        if not isinstance(other, SeldonPodSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
