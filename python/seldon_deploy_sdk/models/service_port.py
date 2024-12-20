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


class ServicePort(object):
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
        'app_protocol': 'str',
        'name': 'str',
        'node_port': 'int',
        'port': 'int',
        'protocol': 'Protocol',
        'target_port': 'IntOrString'
    }

    attribute_map = {
        'app_protocol': 'appProtocol',
        'name': 'name',
        'node_port': 'nodePort',
        'port': 'port',
        'protocol': 'protocol',
        'target_port': 'targetPort'
    }

    def __init__(self, app_protocol=None, name=None, node_port=None, port=None, protocol=None, target_port=None):  # noqa: E501
        """ServicePort - a model defined in Swagger"""  # noqa: E501

        self._app_protocol = None
        self._name = None
        self._node_port = None
        self._port = None
        self._protocol = None
        self._target_port = None
        self.discriminator = None

        if app_protocol is not None:
            self.app_protocol = app_protocol
        if name is not None:
            self.name = name
        if node_port is not None:
            self.node_port = node_port
        if port is not None:
            self.port = port
        if protocol is not None:
            self.protocol = protocol
        if target_port is not None:
            self.target_port = target_port

    @property
    def app_protocol(self):
        """Gets the app_protocol of this ServicePort.  # noqa: E501

        The application protocol for this port. This is used as a hint for implementations to offer richer behavior for protocols that they understand. This field follows standard Kubernetes label syntax. Valid values are either:  Un-prefixed protocol names - reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names).  Kubernetes-defined prefixed names: 'kubernetes.io/h2c' - HTTP/2 prior knowledge over cleartext as described in https://www.rfc-editor.org/rfc/rfc9113.html#name-starting-http-2-with-prior- 'kubernetes.io/ws'  - WebSocket over cleartext as described in https://www.rfc-editor.org/rfc/rfc6455 'kubernetes.io/wss' - WebSocket over TLS as described in https://www.rfc-editor.org/rfc/rfc6455  Other protocols should use implementation-defined prefixed names such as mycompany.com/my-custom-protocol. +optional  # noqa: E501

        :return: The app_protocol of this ServicePort.  # noqa: E501
        :rtype: str
        """
        return self._app_protocol

    @app_protocol.setter
    def app_protocol(self, app_protocol):
        """Sets the app_protocol of this ServicePort.

        The application protocol for this port. This is used as a hint for implementations to offer richer behavior for protocols that they understand. This field follows standard Kubernetes label syntax. Valid values are either:  Un-prefixed protocol names - reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names).  Kubernetes-defined prefixed names: 'kubernetes.io/h2c' - HTTP/2 prior knowledge over cleartext as described in https://www.rfc-editor.org/rfc/rfc9113.html#name-starting-http-2-with-prior- 'kubernetes.io/ws'  - WebSocket over cleartext as described in https://www.rfc-editor.org/rfc/rfc6455 'kubernetes.io/wss' - WebSocket over TLS as described in https://www.rfc-editor.org/rfc/rfc6455  Other protocols should use implementation-defined prefixed names such as mycompany.com/my-custom-protocol. +optional  # noqa: E501

        :param app_protocol: The app_protocol of this ServicePort.  # noqa: E501
        :type: str
        """

        self._app_protocol = app_protocol

    @property
    def name(self):
        """Gets the name of this ServicePort.  # noqa: E501

        The name of this port within the service. This must be a DNS_LABEL. All ports within a ServiceSpec must have unique names. When considering the endpoints for a Service, this must match the 'name' field in the EndpointPort. Optional if only one ServicePort is defined on this service. +optional  # noqa: E501

        :return: The name of this ServicePort.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ServicePort.

        The name of this port within the service. This must be a DNS_LABEL. All ports within a ServiceSpec must have unique names. When considering the endpoints for a Service, this must match the 'name' field in the EndpointPort. Optional if only one ServicePort is defined on this service. +optional  # noqa: E501

        :param name: The name of this ServicePort.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def node_port(self):
        """Gets the node_port of this ServicePort.  # noqa: E501

        The port on each node on which this service is exposed when type is NodePort or LoadBalancer.  Usually assigned by the system. If a value is specified, in-range, and not in use it will be used, otherwise the operation will fail.  If not specified, a port will be allocated if this Service requires one.  If this field is specified when creating a Service which does not need it, creation will fail. This field will be wiped when updating a Service to no longer need it (e.g. changing type from NodePort to ClusterIP). More info: https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport +optional  # noqa: E501

        :return: The node_port of this ServicePort.  # noqa: E501
        :rtype: int
        """
        return self._node_port

    @node_port.setter
    def node_port(self, node_port):
        """Sets the node_port of this ServicePort.

        The port on each node on which this service is exposed when type is NodePort or LoadBalancer.  Usually assigned by the system. If a value is specified, in-range, and not in use it will be used, otherwise the operation will fail.  If not specified, a port will be allocated if this Service requires one.  If this field is specified when creating a Service which does not need it, creation will fail. This field will be wiped when updating a Service to no longer need it (e.g. changing type from NodePort to ClusterIP). More info: https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport +optional  # noqa: E501

        :param node_port: The node_port of this ServicePort.  # noqa: E501
        :type: int
        """

        self._node_port = node_port

    @property
    def port(self):
        """Gets the port of this ServicePort.  # noqa: E501

        The port that will be exposed by this service.  # noqa: E501

        :return: The port of this ServicePort.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ServicePort.

        The port that will be exposed by this service.  # noqa: E501

        :param port: The port of this ServicePort.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this ServicePort.  # noqa: E501


        :return: The protocol of this ServicePort.  # noqa: E501
        :rtype: Protocol
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ServicePort.


        :param protocol: The protocol of this ServicePort.  # noqa: E501
        :type: Protocol
        """

        self._protocol = protocol

    @property
    def target_port(self):
        """Gets the target_port of this ServicePort.  # noqa: E501


        :return: The target_port of this ServicePort.  # noqa: E501
        :rtype: IntOrString
        """
        return self._target_port

    @target_port.setter
    def target_port(self, target_port):
        """Sets the target_port of this ServicePort.


        :param target_port: The target_port of this ServicePort.  # noqa: E501
        :type: IntOrString
        """

        self._target_port = target_port

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
        if issubclass(ServicePort, dict):
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
        if not isinstance(other, ServicePort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
