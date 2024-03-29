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


class ServiceSpec(object):
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
        'allocate_load_balancer_node_ports': 'bool',
        'cluster_ip': 'str',
        'cluster_i_ps': 'list[str]',
        'external_i_ps': 'list[str]',
        'external_name': 'str',
        'external_traffic_policy': 'ServiceExternalTrafficPolicy',
        'health_check_node_port': 'int',
        'internal_traffic_policy': 'ServiceInternalTrafficPolicy',
        'ip_families': 'list[IPFamily]',
        'ip_family_policy': 'IPFamilyPolicy',
        'load_balancer_class': 'str',
        'load_balancer_ip': 'str',
        'load_balancer_source_ranges': 'list[str]',
        'ports': 'list[ServicePort]',
        'publish_not_ready_addresses': 'bool',
        'selector': 'dict(str, str)',
        'session_affinity': 'ServiceAffinity',
        'session_affinity_config': 'SessionAffinityConfig',
        'type': 'ServiceType'
    }

    attribute_map = {
        'allocate_load_balancer_node_ports': 'allocateLoadBalancerNodePorts',
        'cluster_ip': 'clusterIP',
        'cluster_i_ps': 'clusterIPs',
        'external_i_ps': 'externalIPs',
        'external_name': 'externalName',
        'external_traffic_policy': 'externalTrafficPolicy',
        'health_check_node_port': 'healthCheckNodePort',
        'internal_traffic_policy': 'internalTrafficPolicy',
        'ip_families': 'ipFamilies',
        'ip_family_policy': 'ipFamilyPolicy',
        'load_balancer_class': 'loadBalancerClass',
        'load_balancer_ip': 'loadBalancerIP',
        'load_balancer_source_ranges': 'loadBalancerSourceRanges',
        'ports': 'ports',
        'publish_not_ready_addresses': 'publishNotReadyAddresses',
        'selector': 'selector',
        'session_affinity': 'sessionAffinity',
        'session_affinity_config': 'sessionAffinityConfig',
        'type': 'type'
    }

    def __init__(self, allocate_load_balancer_node_ports=None, cluster_ip=None, cluster_i_ps=None, external_i_ps=None, external_name=None, external_traffic_policy=None, health_check_node_port=None, internal_traffic_policy=None, ip_families=None, ip_family_policy=None, load_balancer_class=None, load_balancer_ip=None, load_balancer_source_ranges=None, ports=None, publish_not_ready_addresses=None, selector=None, session_affinity=None, session_affinity_config=None, type=None):  # noqa: E501
        """ServiceSpec - a model defined in Swagger"""  # noqa: E501

        self._allocate_load_balancer_node_ports = None
        self._cluster_ip = None
        self._cluster_i_ps = None
        self._external_i_ps = None
        self._external_name = None
        self._external_traffic_policy = None
        self._health_check_node_port = None
        self._internal_traffic_policy = None
        self._ip_families = None
        self._ip_family_policy = None
        self._load_balancer_class = None
        self._load_balancer_ip = None
        self._load_balancer_source_ranges = None
        self._ports = None
        self._publish_not_ready_addresses = None
        self._selector = None
        self._session_affinity = None
        self._session_affinity_config = None
        self._type = None
        self.discriminator = None

        if allocate_load_balancer_node_ports is not None:
            self.allocate_load_balancer_node_ports = allocate_load_balancer_node_ports
        if cluster_ip is not None:
            self.cluster_ip = cluster_ip
        if cluster_i_ps is not None:
            self.cluster_i_ps = cluster_i_ps
        if external_i_ps is not None:
            self.external_i_ps = external_i_ps
        if external_name is not None:
            self.external_name = external_name
        if external_traffic_policy is not None:
            self.external_traffic_policy = external_traffic_policy
        if health_check_node_port is not None:
            self.health_check_node_port = health_check_node_port
        if internal_traffic_policy is not None:
            self.internal_traffic_policy = internal_traffic_policy
        if ip_families is not None:
            self.ip_families = ip_families
        if ip_family_policy is not None:
            self.ip_family_policy = ip_family_policy
        if load_balancer_class is not None:
            self.load_balancer_class = load_balancer_class
        if load_balancer_ip is not None:
            self.load_balancer_ip = load_balancer_ip
        if load_balancer_source_ranges is not None:
            self.load_balancer_source_ranges = load_balancer_source_ranges
        if ports is not None:
            self.ports = ports
        if publish_not_ready_addresses is not None:
            self.publish_not_ready_addresses = publish_not_ready_addresses
        if selector is not None:
            self.selector = selector
        if session_affinity is not None:
            self.session_affinity = session_affinity
        if session_affinity_config is not None:
            self.session_affinity_config = session_affinity_config
        if type is not None:
            self.type = type

    @property
    def allocate_load_balancer_node_ports(self):
        """Gets the allocate_load_balancer_node_ports of this ServiceSpec.  # noqa: E501

        allocateLoadBalancerNodePorts defines if NodePorts will be automatically allocated for services with type LoadBalancer.  Default is \"true\". It may be set to \"false\" if the cluster load-balancer does not rely on NodePorts.  If the caller requests specific NodePorts (by specifying a value), those requests will be respected, regardless of this field. This field may only be set for services with type LoadBalancer and will be cleared if the type is changed to any other type. +optional  # noqa: E501

        :return: The allocate_load_balancer_node_ports of this ServiceSpec.  # noqa: E501
        :rtype: bool
        """
        return self._allocate_load_balancer_node_ports

    @allocate_load_balancer_node_ports.setter
    def allocate_load_balancer_node_ports(self, allocate_load_balancer_node_ports):
        """Sets the allocate_load_balancer_node_ports of this ServiceSpec.

        allocateLoadBalancerNodePorts defines if NodePorts will be automatically allocated for services with type LoadBalancer.  Default is \"true\". It may be set to \"false\" if the cluster load-balancer does not rely on NodePorts.  If the caller requests specific NodePorts (by specifying a value), those requests will be respected, regardless of this field. This field may only be set for services with type LoadBalancer and will be cleared if the type is changed to any other type. +optional  # noqa: E501

        :param allocate_load_balancer_node_ports: The allocate_load_balancer_node_ports of this ServiceSpec.  # noqa: E501
        :type: bool
        """

        self._allocate_load_balancer_node_ports = allocate_load_balancer_node_ports

    @property
    def cluster_ip(self):
        """Gets the cluster_ip of this ServiceSpec.  # noqa: E501

        clusterIP is the IP address of the service and is usually assigned randomly. If an address is specified manually, is in-range (as per system configuration), and is not in use, it will be allocated to the service; otherwise creation of the service will fail. This field may not be changed through updates unless the type field is also being changed to ExternalName (which requires this field to be blank) or the type field is being changed from ExternalName (in which case this field may optionally be specified, as describe above).  Valid values are \"None\", empty string (\"\"), or a valid IP address. Setting this to \"None\" makes a \"headless service\" (no virtual IP), which is useful when direct endpoint connections are preferred and proxying is not required.  Only applies to types ClusterIP, NodePort, and LoadBalancer. If this field is specified when creating a Service of type ExternalName, creation will fail. This field will be wiped when updating a Service to type ExternalName. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies +optional  # noqa: E501

        :return: The cluster_ip of this ServiceSpec.  # noqa: E501
        :rtype: str
        """
        return self._cluster_ip

    @cluster_ip.setter
    def cluster_ip(self, cluster_ip):
        """Sets the cluster_ip of this ServiceSpec.

        clusterIP is the IP address of the service and is usually assigned randomly. If an address is specified manually, is in-range (as per system configuration), and is not in use, it will be allocated to the service; otherwise creation of the service will fail. This field may not be changed through updates unless the type field is also being changed to ExternalName (which requires this field to be blank) or the type field is being changed from ExternalName (in which case this field may optionally be specified, as describe above).  Valid values are \"None\", empty string (\"\"), or a valid IP address. Setting this to \"None\" makes a \"headless service\" (no virtual IP), which is useful when direct endpoint connections are preferred and proxying is not required.  Only applies to types ClusterIP, NodePort, and LoadBalancer. If this field is specified when creating a Service of type ExternalName, creation will fail. This field will be wiped when updating a Service to type ExternalName. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies +optional  # noqa: E501

        :param cluster_ip: The cluster_ip of this ServiceSpec.  # noqa: E501
        :type: str
        """

        self._cluster_ip = cluster_ip

    @property
    def cluster_i_ps(self):
        """Gets the cluster_i_ps of this ServiceSpec.  # noqa: E501

        ClusterIPs is a list of IP addresses assigned to this service, and are usually assigned randomly.  If an address is specified manually, is in-range (as per system configuration), and is not in use, it will be allocated to the service; otherwise creation of the service will fail. This field may not be changed through updates unless the type field is also being changed to ExternalName (which requires this field to be empty) or the type field is being changed from ExternalName (in which case this field may optionally be specified, as describe above).  Valid values are \"None\", empty string (\"\"), or a valid IP address.  Setting this to \"None\" makes a \"headless service\" (no virtual IP), which is useful when direct endpoint connections are preferred and proxying is not required.  Only applies to types ClusterIP, NodePort, and LoadBalancer. If this field is specified when creating a Service of type ExternalName, creation will fail. This field will be wiped when updating a Service to type ExternalName.  If this field is not specified, it will be initialized from the clusterIP field.  If this field is specified, clients must ensure that clusterIPs[0] and clusterIP have the same value.  This field may hold a maximum of two entries (dual-stack IPs, in either order). These IPs must correspond to the values of the ipFamilies field. Both clusterIPs and ipFamilies are governed by the ipFamilyPolicy field. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies +listType=atomic +optional  # noqa: E501

        :return: The cluster_i_ps of this ServiceSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._cluster_i_ps

    @cluster_i_ps.setter
    def cluster_i_ps(self, cluster_i_ps):
        """Sets the cluster_i_ps of this ServiceSpec.

        ClusterIPs is a list of IP addresses assigned to this service, and are usually assigned randomly.  If an address is specified manually, is in-range (as per system configuration), and is not in use, it will be allocated to the service; otherwise creation of the service will fail. This field may not be changed through updates unless the type field is also being changed to ExternalName (which requires this field to be empty) or the type field is being changed from ExternalName (in which case this field may optionally be specified, as describe above).  Valid values are \"None\", empty string (\"\"), or a valid IP address.  Setting this to \"None\" makes a \"headless service\" (no virtual IP), which is useful when direct endpoint connections are preferred and proxying is not required.  Only applies to types ClusterIP, NodePort, and LoadBalancer. If this field is specified when creating a Service of type ExternalName, creation will fail. This field will be wiped when updating a Service to type ExternalName.  If this field is not specified, it will be initialized from the clusterIP field.  If this field is specified, clients must ensure that clusterIPs[0] and clusterIP have the same value.  This field may hold a maximum of two entries (dual-stack IPs, in either order). These IPs must correspond to the values of the ipFamilies field. Both clusterIPs and ipFamilies are governed by the ipFamilyPolicy field. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies +listType=atomic +optional  # noqa: E501

        :param cluster_i_ps: The cluster_i_ps of this ServiceSpec.  # noqa: E501
        :type: list[str]
        """

        self._cluster_i_ps = cluster_i_ps

    @property
    def external_i_ps(self):
        """Gets the external_i_ps of this ServiceSpec.  # noqa: E501

        externalIPs is a list of IP addresses for which nodes in the cluster will also accept traffic for this service.  These IPs are not managed by Kubernetes.  The user is responsible for ensuring that traffic arrives at a node with this IP.  A common example is external load-balancers that are not part of the Kubernetes system. +optional  # noqa: E501

        :return: The external_i_ps of this ServiceSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._external_i_ps

    @external_i_ps.setter
    def external_i_ps(self, external_i_ps):
        """Sets the external_i_ps of this ServiceSpec.

        externalIPs is a list of IP addresses for which nodes in the cluster will also accept traffic for this service.  These IPs are not managed by Kubernetes.  The user is responsible for ensuring that traffic arrives at a node with this IP.  A common example is external load-balancers that are not part of the Kubernetes system. +optional  # noqa: E501

        :param external_i_ps: The external_i_ps of this ServiceSpec.  # noqa: E501
        :type: list[str]
        """

        self._external_i_ps = external_i_ps

    @property
    def external_name(self):
        """Gets the external_name of this ServiceSpec.  # noqa: E501

        externalName is the external reference that discovery mechanisms will return as an alias for this service (e.g. a DNS CNAME record). No proxying will be involved.  Must be a lowercase RFC-1123 hostname (https://tools.ietf.org/html/rfc1123) and requires `type` to be \"ExternalName\". +optional  # noqa: E501

        :return: The external_name of this ServiceSpec.  # noqa: E501
        :rtype: str
        """
        return self._external_name

    @external_name.setter
    def external_name(self, external_name):
        """Sets the external_name of this ServiceSpec.

        externalName is the external reference that discovery mechanisms will return as an alias for this service (e.g. a DNS CNAME record). No proxying will be involved.  Must be a lowercase RFC-1123 hostname (https://tools.ietf.org/html/rfc1123) and requires `type` to be \"ExternalName\". +optional  # noqa: E501

        :param external_name: The external_name of this ServiceSpec.  # noqa: E501
        :type: str
        """

        self._external_name = external_name

    @property
    def external_traffic_policy(self):
        """Gets the external_traffic_policy of this ServiceSpec.  # noqa: E501


        :return: The external_traffic_policy of this ServiceSpec.  # noqa: E501
        :rtype: ServiceExternalTrafficPolicy
        """
        return self._external_traffic_policy

    @external_traffic_policy.setter
    def external_traffic_policy(self, external_traffic_policy):
        """Sets the external_traffic_policy of this ServiceSpec.


        :param external_traffic_policy: The external_traffic_policy of this ServiceSpec.  # noqa: E501
        :type: ServiceExternalTrafficPolicy
        """

        self._external_traffic_policy = external_traffic_policy

    @property
    def health_check_node_port(self):
        """Gets the health_check_node_port of this ServiceSpec.  # noqa: E501

        healthCheckNodePort specifies the healthcheck nodePort for the service. This only applies when type is set to LoadBalancer and externalTrafficPolicy is set to Local. If a value is specified, is in-range, and is not in use, it will be used.  If not specified, a value will be automatically allocated.  External systems (e.g. load-balancers) can use this port to determine if a given node holds endpoints for this service or not.  If this field is specified when creating a Service which does not need it, creation will fail. This field will be wiped when updating a Service to no longer need it (e.g. changing type). This field cannot be updated once set. +optional  # noqa: E501

        :return: The health_check_node_port of this ServiceSpec.  # noqa: E501
        :rtype: int
        """
        return self._health_check_node_port

    @health_check_node_port.setter
    def health_check_node_port(self, health_check_node_port):
        """Sets the health_check_node_port of this ServiceSpec.

        healthCheckNodePort specifies the healthcheck nodePort for the service. This only applies when type is set to LoadBalancer and externalTrafficPolicy is set to Local. If a value is specified, is in-range, and is not in use, it will be used.  If not specified, a value will be automatically allocated.  External systems (e.g. load-balancers) can use this port to determine if a given node holds endpoints for this service or not.  If this field is specified when creating a Service which does not need it, creation will fail. This field will be wiped when updating a Service to no longer need it (e.g. changing type). This field cannot be updated once set. +optional  # noqa: E501

        :param health_check_node_port: The health_check_node_port of this ServiceSpec.  # noqa: E501
        :type: int
        """

        self._health_check_node_port = health_check_node_port

    @property
    def internal_traffic_policy(self):
        """Gets the internal_traffic_policy of this ServiceSpec.  # noqa: E501


        :return: The internal_traffic_policy of this ServiceSpec.  # noqa: E501
        :rtype: ServiceInternalTrafficPolicy
        """
        return self._internal_traffic_policy

    @internal_traffic_policy.setter
    def internal_traffic_policy(self, internal_traffic_policy):
        """Sets the internal_traffic_policy of this ServiceSpec.


        :param internal_traffic_policy: The internal_traffic_policy of this ServiceSpec.  # noqa: E501
        :type: ServiceInternalTrafficPolicy
        """

        self._internal_traffic_policy = internal_traffic_policy

    @property
    def ip_families(self):
        """Gets the ip_families of this ServiceSpec.  # noqa: E501

        IPFamilies is a list of IP families (e.g. IPv4, IPv6) assigned to this service. This field is usually assigned automatically based on cluster configuration and the ipFamilyPolicy field. If this field is specified manually, the requested family is available in the cluster, and ipFamilyPolicy allows it, it will be used; otherwise creation of the service will fail. This field is conditionally mutable: it allows for adding or removing a secondary IP family, but it does not allow changing the primary IP family of the Service. Valid values are \"IPv4\" and \"IPv6\".  This field only applies to Services of types ClusterIP, NodePort, and LoadBalancer, and does apply to \"headless\" services. This field will be wiped when updating a Service to type ExternalName.  This field may hold a maximum of two entries (dual-stack families, in either order).  These families must correspond to the values of the clusterIPs field, if specified. Both clusterIPs and ipFamilies are governed by the ipFamilyPolicy field. +listType=atomic +optional  # noqa: E501

        :return: The ip_families of this ServiceSpec.  # noqa: E501
        :rtype: list[IPFamily]
        """
        return self._ip_families

    @ip_families.setter
    def ip_families(self, ip_families):
        """Sets the ip_families of this ServiceSpec.

        IPFamilies is a list of IP families (e.g. IPv4, IPv6) assigned to this service. This field is usually assigned automatically based on cluster configuration and the ipFamilyPolicy field. If this field is specified manually, the requested family is available in the cluster, and ipFamilyPolicy allows it, it will be used; otherwise creation of the service will fail. This field is conditionally mutable: it allows for adding or removing a secondary IP family, but it does not allow changing the primary IP family of the Service. Valid values are \"IPv4\" and \"IPv6\".  This field only applies to Services of types ClusterIP, NodePort, and LoadBalancer, and does apply to \"headless\" services. This field will be wiped when updating a Service to type ExternalName.  This field may hold a maximum of two entries (dual-stack families, in either order).  These families must correspond to the values of the clusterIPs field, if specified. Both clusterIPs and ipFamilies are governed by the ipFamilyPolicy field. +listType=atomic +optional  # noqa: E501

        :param ip_families: The ip_families of this ServiceSpec.  # noqa: E501
        :type: list[IPFamily]
        """

        self._ip_families = ip_families

    @property
    def ip_family_policy(self):
        """Gets the ip_family_policy of this ServiceSpec.  # noqa: E501


        :return: The ip_family_policy of this ServiceSpec.  # noqa: E501
        :rtype: IPFamilyPolicy
        """
        return self._ip_family_policy

    @ip_family_policy.setter
    def ip_family_policy(self, ip_family_policy):
        """Sets the ip_family_policy of this ServiceSpec.


        :param ip_family_policy: The ip_family_policy of this ServiceSpec.  # noqa: E501
        :type: IPFamilyPolicy
        """

        self._ip_family_policy = ip_family_policy

    @property
    def load_balancer_class(self):
        """Gets the load_balancer_class of this ServiceSpec.  # noqa: E501

        loadBalancerClass is the class of the load balancer implementation this Service belongs to. If specified, the value of this field must be a label-style identifier, with an optional prefix, e.g. \"internal-vip\" or \"example.com/internal-vip\". Unprefixed names are reserved for end-users. This field can only be set when the Service type is 'LoadBalancer'. If not set, the default load balancer implementation is used, today this is typically done through the cloud provider integration, but should apply for any default implementation. If set, it is assumed that a load balancer implementation is watching for Services with a matching class. Any default load balancer implementation (e.g. cloud providers) should ignore Services that set this field. This field can only be set when creating or updating a Service to type 'LoadBalancer'. Once set, it can not be changed. This field will be wiped when a service is updated to a non 'LoadBalancer' type. +optional  # noqa: E501

        :return: The load_balancer_class of this ServiceSpec.  # noqa: E501
        :rtype: str
        """
        return self._load_balancer_class

    @load_balancer_class.setter
    def load_balancer_class(self, load_balancer_class):
        """Sets the load_balancer_class of this ServiceSpec.

        loadBalancerClass is the class of the load balancer implementation this Service belongs to. If specified, the value of this field must be a label-style identifier, with an optional prefix, e.g. \"internal-vip\" or \"example.com/internal-vip\". Unprefixed names are reserved for end-users. This field can only be set when the Service type is 'LoadBalancer'. If not set, the default load balancer implementation is used, today this is typically done through the cloud provider integration, but should apply for any default implementation. If set, it is assumed that a load balancer implementation is watching for Services with a matching class. Any default load balancer implementation (e.g. cloud providers) should ignore Services that set this field. This field can only be set when creating or updating a Service to type 'LoadBalancer'. Once set, it can not be changed. This field will be wiped when a service is updated to a non 'LoadBalancer' type. +optional  # noqa: E501

        :param load_balancer_class: The load_balancer_class of this ServiceSpec.  # noqa: E501
        :type: str
        """

        self._load_balancer_class = load_balancer_class

    @property
    def load_balancer_ip(self):
        """Gets the load_balancer_ip of this ServiceSpec.  # noqa: E501

        Only applies to Service Type: LoadBalancer. This feature depends on whether the underlying cloud-provider supports specifying the loadBalancerIP when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature. Deprecated: This field was under-specified and its meaning varies across implementations. Using it is non-portable and it may not support dual-stack. Users are encouraged to use implementation-specific annotations when available. +optional  # noqa: E501

        :return: The load_balancer_ip of this ServiceSpec.  # noqa: E501
        :rtype: str
        """
        return self._load_balancer_ip

    @load_balancer_ip.setter
    def load_balancer_ip(self, load_balancer_ip):
        """Sets the load_balancer_ip of this ServiceSpec.

        Only applies to Service Type: LoadBalancer. This feature depends on whether the underlying cloud-provider supports specifying the loadBalancerIP when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature. Deprecated: This field was under-specified and its meaning varies across implementations. Using it is non-portable and it may not support dual-stack. Users are encouraged to use implementation-specific annotations when available. +optional  # noqa: E501

        :param load_balancer_ip: The load_balancer_ip of this ServiceSpec.  # noqa: E501
        :type: str
        """

        self._load_balancer_ip = load_balancer_ip

    @property
    def load_balancer_source_ranges(self):
        """Gets the load_balancer_source_ranges of this ServiceSpec.  # noqa: E501

        If specified and supported by the platform, this will restrict traffic through the cloud-provider load-balancer will be restricted to the specified client IPs. This field will be ignored if the cloud-provider does not support the feature.\" More info: https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/ +optional  # noqa: E501

        :return: The load_balancer_source_ranges of this ServiceSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._load_balancer_source_ranges

    @load_balancer_source_ranges.setter
    def load_balancer_source_ranges(self, load_balancer_source_ranges):
        """Sets the load_balancer_source_ranges of this ServiceSpec.

        If specified and supported by the platform, this will restrict traffic through the cloud-provider load-balancer will be restricted to the specified client IPs. This field will be ignored if the cloud-provider does not support the feature.\" More info: https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/ +optional  # noqa: E501

        :param load_balancer_source_ranges: The load_balancer_source_ranges of this ServiceSpec.  # noqa: E501
        :type: list[str]
        """

        self._load_balancer_source_ranges = load_balancer_source_ranges

    @property
    def ports(self):
        """Gets the ports of this ServiceSpec.  # noqa: E501

        The list of ports that are exposed by this service. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies +patchMergeKey=port +patchStrategy=merge +listType=map +listMapKey=port +listMapKey=protocol  # noqa: E501

        :return: The ports of this ServiceSpec.  # noqa: E501
        :rtype: list[ServicePort]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this ServiceSpec.

        The list of ports that are exposed by this service. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies +patchMergeKey=port +patchStrategy=merge +listType=map +listMapKey=port +listMapKey=protocol  # noqa: E501

        :param ports: The ports of this ServiceSpec.  # noqa: E501
        :type: list[ServicePort]
        """

        self._ports = ports

    @property
    def publish_not_ready_addresses(self):
        """Gets the publish_not_ready_addresses of this ServiceSpec.  # noqa: E501

        publishNotReadyAddresses indicates that any agent which deals with endpoints for this Service should disregard any indications of ready/not-ready. The primary use case for setting this field is for a StatefulSet's Headless Service to propagate SRV DNS records for its Pods for the purpose of peer discovery. The Kubernetes controllers that generate Endpoints and EndpointSlice resources for Services interpret this to mean that all endpoints are considered \"ready\" even if the Pods themselves are not. Agents which consume only Kubernetes generated endpoints through the Endpoints or EndpointSlice resources can safely assume this behavior. +optional  # noqa: E501

        :return: The publish_not_ready_addresses of this ServiceSpec.  # noqa: E501
        :rtype: bool
        """
        return self._publish_not_ready_addresses

    @publish_not_ready_addresses.setter
    def publish_not_ready_addresses(self, publish_not_ready_addresses):
        """Sets the publish_not_ready_addresses of this ServiceSpec.

        publishNotReadyAddresses indicates that any agent which deals with endpoints for this Service should disregard any indications of ready/not-ready. The primary use case for setting this field is for a StatefulSet's Headless Service to propagate SRV DNS records for its Pods for the purpose of peer discovery. The Kubernetes controllers that generate Endpoints and EndpointSlice resources for Services interpret this to mean that all endpoints are considered \"ready\" even if the Pods themselves are not. Agents which consume only Kubernetes generated endpoints through the Endpoints or EndpointSlice resources can safely assume this behavior. +optional  # noqa: E501

        :param publish_not_ready_addresses: The publish_not_ready_addresses of this ServiceSpec.  # noqa: E501
        :type: bool
        """

        self._publish_not_ready_addresses = publish_not_ready_addresses

    @property
    def selector(self):
        """Gets the selector of this ServiceSpec.  # noqa: E501

        Route service traffic to pods with label keys and values matching this selector. If empty or not present, the service is assumed to have an external process managing its endpoints, which Kubernetes will not modify. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName. More info: https://kubernetes.io/docs/concepts/services-networking/service/ +optional +mapType=atomic  # noqa: E501

        :return: The selector of this ServiceSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this ServiceSpec.

        Route service traffic to pods with label keys and values matching this selector. If empty or not present, the service is assumed to have an external process managing its endpoints, which Kubernetes will not modify. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName. More info: https://kubernetes.io/docs/concepts/services-networking/service/ +optional +mapType=atomic  # noqa: E501

        :param selector: The selector of this ServiceSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._selector = selector

    @property
    def session_affinity(self):
        """Gets the session_affinity of this ServiceSpec.  # noqa: E501


        :return: The session_affinity of this ServiceSpec.  # noqa: E501
        :rtype: ServiceAffinity
        """
        return self._session_affinity

    @session_affinity.setter
    def session_affinity(self, session_affinity):
        """Sets the session_affinity of this ServiceSpec.


        :param session_affinity: The session_affinity of this ServiceSpec.  # noqa: E501
        :type: ServiceAffinity
        """

        self._session_affinity = session_affinity

    @property
    def session_affinity_config(self):
        """Gets the session_affinity_config of this ServiceSpec.  # noqa: E501


        :return: The session_affinity_config of this ServiceSpec.  # noqa: E501
        :rtype: SessionAffinityConfig
        """
        return self._session_affinity_config

    @session_affinity_config.setter
    def session_affinity_config(self, session_affinity_config):
        """Sets the session_affinity_config of this ServiceSpec.


        :param session_affinity_config: The session_affinity_config of this ServiceSpec.  # noqa: E501
        :type: SessionAffinityConfig
        """

        self._session_affinity_config = session_affinity_config

    @property
    def type(self):
        """Gets the type of this ServiceSpec.  # noqa: E501


        :return: The type of this ServiceSpec.  # noqa: E501
        :rtype: ServiceType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ServiceSpec.


        :param type: The type of this ServiceSpec.  # noqa: E501
        :type: ServiceType
        """

        self._type = type

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
        if issubclass(ServiceSpec, dict):
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
        if not isinstance(other, ServiceSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
