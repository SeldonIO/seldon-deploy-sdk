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


class PodAffinityTerm(object):
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
        'label_selector': 'LabelSelector',
        'match_label_keys': 'list[str]',
        'mismatch_label_keys': 'list[str]',
        'namespace_selector': 'LabelSelector',
        'namespaces': 'list[str]',
        'topology_key': 'str'
    }

    attribute_map = {
        'label_selector': 'labelSelector',
        'match_label_keys': 'matchLabelKeys',
        'mismatch_label_keys': 'mismatchLabelKeys',
        'namespace_selector': 'namespaceSelector',
        'namespaces': 'namespaces',
        'topology_key': 'topologyKey'
    }

    def __init__(self, label_selector=None, match_label_keys=None, mismatch_label_keys=None, namespace_selector=None, namespaces=None, topology_key=None):  # noqa: E501
        """PodAffinityTerm - a model defined in Swagger"""  # noqa: E501

        self._label_selector = None
        self._match_label_keys = None
        self._mismatch_label_keys = None
        self._namespace_selector = None
        self._namespaces = None
        self._topology_key = None
        self.discriminator = None

        if label_selector is not None:
            self.label_selector = label_selector
        if match_label_keys is not None:
            self.match_label_keys = match_label_keys
        if mismatch_label_keys is not None:
            self.mismatch_label_keys = mismatch_label_keys
        if namespace_selector is not None:
            self.namespace_selector = namespace_selector
        if namespaces is not None:
            self.namespaces = namespaces
        if topology_key is not None:
            self.topology_key = topology_key

    @property
    def label_selector(self):
        """Gets the label_selector of this PodAffinityTerm.  # noqa: E501


        :return: The label_selector of this PodAffinityTerm.  # noqa: E501
        :rtype: LabelSelector
        """
        return self._label_selector

    @label_selector.setter
    def label_selector(self, label_selector):
        """Sets the label_selector of this PodAffinityTerm.


        :param label_selector: The label_selector of this PodAffinityTerm.  # noqa: E501
        :type: LabelSelector
        """

        self._label_selector = label_selector

    @property
    def match_label_keys(self):
        """Gets the match_label_keys of this PodAffinityTerm.  # noqa: E501

        MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `LabelSelector` as `key in (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both MatchLabelKeys and LabelSelector. Also, MatchLabelKeys cannot be set when LabelSelector isn't set. This is an alpha field and requires enabling MatchLabelKeysInPodAffinity feature gate. +listType=atomic +optional  # noqa: E501

        :return: The match_label_keys of this PodAffinityTerm.  # noqa: E501
        :rtype: list[str]
        """
        return self._match_label_keys

    @match_label_keys.setter
    def match_label_keys(self, match_label_keys):
        """Sets the match_label_keys of this PodAffinityTerm.

        MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `LabelSelector` as `key in (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both MatchLabelKeys and LabelSelector. Also, MatchLabelKeys cannot be set when LabelSelector isn't set. This is an alpha field and requires enabling MatchLabelKeysInPodAffinity feature gate. +listType=atomic +optional  # noqa: E501

        :param match_label_keys: The match_label_keys of this PodAffinityTerm.  # noqa: E501
        :type: list[str]
        """

        self._match_label_keys = match_label_keys

    @property
    def mismatch_label_keys(self):
        """Gets the mismatch_label_keys of this PodAffinityTerm.  # noqa: E501

        MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `LabelSelector` as `key notin (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both MismatchLabelKeys and LabelSelector. Also, MismatchLabelKeys cannot be set when LabelSelector isn't set. This is an alpha field and requires enabling MatchLabelKeysInPodAffinity feature gate. +listType=atomic +optional  # noqa: E501

        :return: The mismatch_label_keys of this PodAffinityTerm.  # noqa: E501
        :rtype: list[str]
        """
        return self._mismatch_label_keys

    @mismatch_label_keys.setter
    def mismatch_label_keys(self, mismatch_label_keys):
        """Sets the mismatch_label_keys of this PodAffinityTerm.

        MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `LabelSelector` as `key notin (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both MismatchLabelKeys and LabelSelector. Also, MismatchLabelKeys cannot be set when LabelSelector isn't set. This is an alpha field and requires enabling MatchLabelKeysInPodAffinity feature gate. +listType=atomic +optional  # noqa: E501

        :param mismatch_label_keys: The mismatch_label_keys of this PodAffinityTerm.  # noqa: E501
        :type: list[str]
        """

        self._mismatch_label_keys = mismatch_label_keys

    @property
    def namespace_selector(self):
        """Gets the namespace_selector of this PodAffinityTerm.  # noqa: E501


        :return: The namespace_selector of this PodAffinityTerm.  # noqa: E501
        :rtype: LabelSelector
        """
        return self._namespace_selector

    @namespace_selector.setter
    def namespace_selector(self, namespace_selector):
        """Sets the namespace_selector of this PodAffinityTerm.


        :param namespace_selector: The namespace_selector of this PodAffinityTerm.  # noqa: E501
        :type: LabelSelector
        """

        self._namespace_selector = namespace_selector

    @property
    def namespaces(self):
        """Gets the namespaces of this PodAffinityTerm.  # noqa: E501

        namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means \"this pod's namespace\". +optional  # noqa: E501

        :return: The namespaces of this PodAffinityTerm.  # noqa: E501
        :rtype: list[str]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """Sets the namespaces of this PodAffinityTerm.

        namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means \"this pod's namespace\". +optional  # noqa: E501

        :param namespaces: The namespaces of this PodAffinityTerm.  # noqa: E501
        :type: list[str]
        """

        self._namespaces = namespaces

    @property
    def topology_key(self):
        """Gets the topology_key of this PodAffinityTerm.  # noqa: E501

        This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.  # noqa: E501

        :return: The topology_key of this PodAffinityTerm.  # noqa: E501
        :rtype: str
        """
        return self._topology_key

    @topology_key.setter
    def topology_key(self, topology_key):
        """Sets the topology_key of this PodAffinityTerm.

        This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.  # noqa: E501

        :param topology_key: The topology_key of this PodAffinityTerm.  # noqa: E501
        :type: str
        """

        self._topology_key = topology_key

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
        if issubclass(PodAffinityTerm, dict):
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
        if not isinstance(other, PodAffinityTerm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
