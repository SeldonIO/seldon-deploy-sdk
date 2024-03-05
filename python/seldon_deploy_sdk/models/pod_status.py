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


class PodStatus(object):
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
        'conditions': 'list[PodCondition]',
        'container_statuses': 'list[ContainerStatus]',
        'ephemeral_container_statuses': 'list[ContainerStatus]',
        'host_ip': 'str',
        'host_i_ps': 'list[HostIP]',
        'init_container_statuses': 'list[ContainerStatus]',
        'message': 'str',
        'nominated_node_name': 'str',
        'phase': 'PodPhase',
        'pod_ip': 'str',
        'pod_i_ps': 'list[PodIP]',
        'qos_class': 'PodQOSClass',
        'reason': 'str',
        'resize': 'PodResizeStatus',
        'resource_claim_statuses': 'list[PodResourceClaimStatus]',
        'start_time': 'str'
    }

    attribute_map = {
        'conditions': 'conditions',
        'container_statuses': 'containerStatuses',
        'ephemeral_container_statuses': 'ephemeralContainerStatuses',
        'host_ip': 'hostIP',
        'host_i_ps': 'hostIPs',
        'init_container_statuses': 'initContainerStatuses',
        'message': 'message',
        'nominated_node_name': 'nominatedNodeName',
        'phase': 'phase',
        'pod_ip': 'podIP',
        'pod_i_ps': 'podIPs',
        'qos_class': 'qosClass',
        'reason': 'reason',
        'resize': 'resize',
        'resource_claim_statuses': 'resourceClaimStatuses',
        'start_time': 'startTime'
    }

    def __init__(self, conditions=None, container_statuses=None, ephemeral_container_statuses=None, host_ip=None, host_i_ps=None, init_container_statuses=None, message=None, nominated_node_name=None, phase=None, pod_ip=None, pod_i_ps=None, qos_class=None, reason=None, resize=None, resource_claim_statuses=None, start_time=None):  # noqa: E501
        """PodStatus - a model defined in Swagger"""  # noqa: E501

        self._conditions = None
        self._container_statuses = None
        self._ephemeral_container_statuses = None
        self._host_ip = None
        self._host_i_ps = None
        self._init_container_statuses = None
        self._message = None
        self._nominated_node_name = None
        self._phase = None
        self._pod_ip = None
        self._pod_i_ps = None
        self._qos_class = None
        self._reason = None
        self._resize = None
        self._resource_claim_statuses = None
        self._start_time = None
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions
        if container_statuses is not None:
            self.container_statuses = container_statuses
        if ephemeral_container_statuses is not None:
            self.ephemeral_container_statuses = ephemeral_container_statuses
        if host_ip is not None:
            self.host_ip = host_ip
        if host_i_ps is not None:
            self.host_i_ps = host_i_ps
        if init_container_statuses is not None:
            self.init_container_statuses = init_container_statuses
        if message is not None:
            self.message = message
        if nominated_node_name is not None:
            self.nominated_node_name = nominated_node_name
        if phase is not None:
            self.phase = phase
        if pod_ip is not None:
            self.pod_ip = pod_ip
        if pod_i_ps is not None:
            self.pod_i_ps = pod_i_ps
        if qos_class is not None:
            self.qos_class = qos_class
        if reason is not None:
            self.reason = reason
        if resize is not None:
            self.resize = resize
        if resource_claim_statuses is not None:
            self.resource_claim_statuses = resource_claim_statuses
        if start_time is not None:
            self.start_time = start_time

    @property
    def conditions(self):
        """Gets the conditions of this PodStatus.  # noqa: E501

        Current service state of pod. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions +optional +patchMergeKey=type +patchStrategy=merge  # noqa: E501

        :return: The conditions of this PodStatus.  # noqa: E501
        :rtype: list[PodCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this PodStatus.

        Current service state of pod. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions +optional +patchMergeKey=type +patchStrategy=merge  # noqa: E501

        :param conditions: The conditions of this PodStatus.  # noqa: E501
        :type: list[PodCondition]
        """

        self._conditions = conditions

    @property
    def container_statuses(self):
        """Gets the container_statuses of this PodStatus.  # noqa: E501

        The list has one entry per container in the manifest. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status +optional  # noqa: E501

        :return: The container_statuses of this PodStatus.  # noqa: E501
        :rtype: list[ContainerStatus]
        """
        return self._container_statuses

    @container_statuses.setter
    def container_statuses(self, container_statuses):
        """Sets the container_statuses of this PodStatus.

        The list has one entry per container in the manifest. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status +optional  # noqa: E501

        :param container_statuses: The container_statuses of this PodStatus.  # noqa: E501
        :type: list[ContainerStatus]
        """

        self._container_statuses = container_statuses

    @property
    def ephemeral_container_statuses(self):
        """Gets the ephemeral_container_statuses of this PodStatus.  # noqa: E501

        Status for any ephemeral containers that have run in this pod. +optional  # noqa: E501

        :return: The ephemeral_container_statuses of this PodStatus.  # noqa: E501
        :rtype: list[ContainerStatus]
        """
        return self._ephemeral_container_statuses

    @ephemeral_container_statuses.setter
    def ephemeral_container_statuses(self, ephemeral_container_statuses):
        """Sets the ephemeral_container_statuses of this PodStatus.

        Status for any ephemeral containers that have run in this pod. +optional  # noqa: E501

        :param ephemeral_container_statuses: The ephemeral_container_statuses of this PodStatus.  # noqa: E501
        :type: list[ContainerStatus]
        """

        self._ephemeral_container_statuses = ephemeral_container_statuses

    @property
    def host_ip(self):
        """Gets the host_ip of this PodStatus.  # noqa: E501

        hostIP holds the IP address of the host to which the pod is assigned. Empty if the pod has not started yet. A pod can be assigned to a node that has a problem in kubelet which in turns mean that HostIP will not be updated even if there is a node is assigned to pod +optional  # noqa: E501

        :return: The host_ip of this PodStatus.  # noqa: E501
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this PodStatus.

        hostIP holds the IP address of the host to which the pod is assigned. Empty if the pod has not started yet. A pod can be assigned to a node that has a problem in kubelet which in turns mean that HostIP will not be updated even if there is a node is assigned to pod +optional  # noqa: E501

        :param host_ip: The host_ip of this PodStatus.  # noqa: E501
        :type: str
        """

        self._host_ip = host_ip

    @property
    def host_i_ps(self):
        """Gets the host_i_ps of this PodStatus.  # noqa: E501

        hostIPs holds the IP addresses allocated to the host. If this field is specified, the first entry must match the hostIP field. This list is empty if the pod has not started yet. A pod can be assigned to a node that has a problem in kubelet which in turns means that HostIPs will not be updated even if there is a node is assigned to this pod. +optional +patchStrategy=merge +patchMergeKey=ip +listType=atomic  # noqa: E501

        :return: The host_i_ps of this PodStatus.  # noqa: E501
        :rtype: list[HostIP]
        """
        return self._host_i_ps

    @host_i_ps.setter
    def host_i_ps(self, host_i_ps):
        """Sets the host_i_ps of this PodStatus.

        hostIPs holds the IP addresses allocated to the host. If this field is specified, the first entry must match the hostIP field. This list is empty if the pod has not started yet. A pod can be assigned to a node that has a problem in kubelet which in turns means that HostIPs will not be updated even if there is a node is assigned to this pod. +optional +patchStrategy=merge +patchMergeKey=ip +listType=atomic  # noqa: E501

        :param host_i_ps: The host_i_ps of this PodStatus.  # noqa: E501
        :type: list[HostIP]
        """

        self._host_i_ps = host_i_ps

    @property
    def init_container_statuses(self):
        """Gets the init_container_statuses of this PodStatus.  # noqa: E501

        The list has one entry per init container in the manifest. The most recent successful init container will have ready = true, the most recently started container will have startTime set. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status  # noqa: E501

        :return: The init_container_statuses of this PodStatus.  # noqa: E501
        :rtype: list[ContainerStatus]
        """
        return self._init_container_statuses

    @init_container_statuses.setter
    def init_container_statuses(self, init_container_statuses):
        """Sets the init_container_statuses of this PodStatus.

        The list has one entry per init container in the manifest. The most recent successful init container will have ready = true, the most recently started container will have startTime set. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status  # noqa: E501

        :param init_container_statuses: The init_container_statuses of this PodStatus.  # noqa: E501
        :type: list[ContainerStatus]
        """

        self._init_container_statuses = init_container_statuses

    @property
    def message(self):
        """Gets the message of this PodStatus.  # noqa: E501

        A human readable message indicating details about why the pod is in this condition. +optional  # noqa: E501

        :return: The message of this PodStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PodStatus.

        A human readable message indicating details about why the pod is in this condition. +optional  # noqa: E501

        :param message: The message of this PodStatus.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def nominated_node_name(self):
        """Gets the nominated_node_name of this PodStatus.  # noqa: E501

        nominatedNodeName is set only when this pod preempts other pods on the node, but it cannot be scheduled right away as preemption victims receive their graceful termination periods. This field does not guarantee that the pod will be scheduled on this node. Scheduler may decide to place the pod elsewhere if other nodes become available sooner. Scheduler may also decide to give the resources on this node to a higher priority pod that is created after preemption. As a result, this field may be different than PodSpec.nodeName when the pod is scheduled. +optional  # noqa: E501

        :return: The nominated_node_name of this PodStatus.  # noqa: E501
        :rtype: str
        """
        return self._nominated_node_name

    @nominated_node_name.setter
    def nominated_node_name(self, nominated_node_name):
        """Sets the nominated_node_name of this PodStatus.

        nominatedNodeName is set only when this pod preempts other pods on the node, but it cannot be scheduled right away as preemption victims receive their graceful termination periods. This field does not guarantee that the pod will be scheduled on this node. Scheduler may decide to place the pod elsewhere if other nodes become available sooner. Scheduler may also decide to give the resources on this node to a higher priority pod that is created after preemption. As a result, this field may be different than PodSpec.nodeName when the pod is scheduled. +optional  # noqa: E501

        :param nominated_node_name: The nominated_node_name of this PodStatus.  # noqa: E501
        :type: str
        """

        self._nominated_node_name = nominated_node_name

    @property
    def phase(self):
        """Gets the phase of this PodStatus.  # noqa: E501


        :return: The phase of this PodStatus.  # noqa: E501
        :rtype: PodPhase
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this PodStatus.


        :param phase: The phase of this PodStatus.  # noqa: E501
        :type: PodPhase
        """

        self._phase = phase

    @property
    def pod_ip(self):
        """Gets the pod_ip of this PodStatus.  # noqa: E501

        podIP address allocated to the pod. Routable at least within the cluster. Empty if not yet allocated. +optional  # noqa: E501

        :return: The pod_ip of this PodStatus.  # noqa: E501
        :rtype: str
        """
        return self._pod_ip

    @pod_ip.setter
    def pod_ip(self, pod_ip):
        """Sets the pod_ip of this PodStatus.

        podIP address allocated to the pod. Routable at least within the cluster. Empty if not yet allocated. +optional  # noqa: E501

        :param pod_ip: The pod_ip of this PodStatus.  # noqa: E501
        :type: str
        """

        self._pod_ip = pod_ip

    @property
    def pod_i_ps(self):
        """Gets the pod_i_ps of this PodStatus.  # noqa: E501

        podIPs holds the IP addresses allocated to the pod. If this field is specified, the 0th entry must match the podIP field. Pods may be allocated at most 1 value for each of IPv4 and IPv6. This list is empty if no IPs have been allocated yet. +optional +patchStrategy=merge +patchMergeKey=ip  # noqa: E501

        :return: The pod_i_ps of this PodStatus.  # noqa: E501
        :rtype: list[PodIP]
        """
        return self._pod_i_ps

    @pod_i_ps.setter
    def pod_i_ps(self, pod_i_ps):
        """Sets the pod_i_ps of this PodStatus.

        podIPs holds the IP addresses allocated to the pod. If this field is specified, the 0th entry must match the podIP field. Pods may be allocated at most 1 value for each of IPv4 and IPv6. This list is empty if no IPs have been allocated yet. +optional +patchStrategy=merge +patchMergeKey=ip  # noqa: E501

        :param pod_i_ps: The pod_i_ps of this PodStatus.  # noqa: E501
        :type: list[PodIP]
        """

        self._pod_i_ps = pod_i_ps

    @property
    def qos_class(self):
        """Gets the qos_class of this PodStatus.  # noqa: E501


        :return: The qos_class of this PodStatus.  # noqa: E501
        :rtype: PodQOSClass
        """
        return self._qos_class

    @qos_class.setter
    def qos_class(self, qos_class):
        """Sets the qos_class of this PodStatus.


        :param qos_class: The qos_class of this PodStatus.  # noqa: E501
        :type: PodQOSClass
        """

        self._qos_class = qos_class

    @property
    def reason(self):
        """Gets the reason of this PodStatus.  # noqa: E501

        A brief CamelCase message indicating details about why the pod is in this state. e.g. 'Evicted' +optional  # noqa: E501

        :return: The reason of this PodStatus.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this PodStatus.

        A brief CamelCase message indicating details about why the pod is in this state. e.g. 'Evicted' +optional  # noqa: E501

        :param reason: The reason of this PodStatus.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def resize(self):
        """Gets the resize of this PodStatus.  # noqa: E501


        :return: The resize of this PodStatus.  # noqa: E501
        :rtype: PodResizeStatus
        """
        return self._resize

    @resize.setter
    def resize(self, resize):
        """Sets the resize of this PodStatus.


        :param resize: The resize of this PodStatus.  # noqa: E501
        :type: PodResizeStatus
        """

        self._resize = resize

    @property
    def resource_claim_statuses(self):
        """Gets the resource_claim_statuses of this PodStatus.  # noqa: E501

        Status of resource claims. +patchMergeKey=name +patchStrategy=merge,retainKeys +listType=map +listMapKey=name +featureGate=DynamicResourceAllocation +optional  # noqa: E501

        :return: The resource_claim_statuses of this PodStatus.  # noqa: E501
        :rtype: list[PodResourceClaimStatus]
        """
        return self._resource_claim_statuses

    @resource_claim_statuses.setter
    def resource_claim_statuses(self, resource_claim_statuses):
        """Sets the resource_claim_statuses of this PodStatus.

        Status of resource claims. +patchMergeKey=name +patchStrategy=merge,retainKeys +listType=map +listMapKey=name +featureGate=DynamicResourceAllocation +optional  # noqa: E501

        :param resource_claim_statuses: The resource_claim_statuses of this PodStatus.  # noqa: E501
        :type: list[PodResourceClaimStatus]
        """

        self._resource_claim_statuses = resource_claim_statuses

    @property
    def start_time(self):
        """Gets the start_time of this PodStatus.  # noqa: E501

        RFC 3339 date and time at which the object was acknowledged by the Kubelet. This is before the Kubelet pulled the container image(s) for the pod. +optional  # noqa: E501

        :return: The start_time of this PodStatus.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this PodStatus.

        RFC 3339 date and time at which the object was acknowledged by the Kubelet. This is before the Kubelet pulled the container image(s) for the pod. +optional  # noqa: E501

        :param start_time: The start_time of this PodStatus.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

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
        if issubclass(PodStatus, dict):
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
        if not isinstance(other, PodStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
