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


class Container(object):
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
        'args': 'list[str]',
        'command': 'list[str]',
        'env': 'list[EnvVar]',
        'env_from': 'list[EnvFromSource]',
        'image': 'str',
        'image_pull_policy': 'PullPolicy',
        'lifecycle': 'Lifecycle',
        'liveness_probe': 'Probe',
        'name': 'str',
        'ports': 'list[ContainerPort]',
        'readiness_probe': 'Probe',
        'resize_policy': 'list[ContainerResizePolicy]',
        'resources': 'ResourceRequirements',
        'restart_policy': 'ContainerRestartPolicy',
        'security_context': 'SecurityContext',
        'startup_probe': 'Probe',
        'stdin': 'bool',
        'stdin_once': 'bool',
        'termination_message_path': 'str',
        'termination_message_policy': 'TerminationMessagePolicy',
        'tty': 'bool',
        'volume_devices': 'list[VolumeDevice]',
        'volume_mounts': 'list[VolumeMount]',
        'working_dir': 'str'
    }

    attribute_map = {
        'args': 'args',
        'command': 'command',
        'env': 'env',
        'env_from': 'envFrom',
        'image': 'image',
        'image_pull_policy': 'imagePullPolicy',
        'lifecycle': 'lifecycle',
        'liveness_probe': 'livenessProbe',
        'name': 'name',
        'ports': 'ports',
        'readiness_probe': 'readinessProbe',
        'resize_policy': 'resizePolicy',
        'resources': 'resources',
        'restart_policy': 'restartPolicy',
        'security_context': 'securityContext',
        'startup_probe': 'startupProbe',
        'stdin': 'stdin',
        'stdin_once': 'stdinOnce',
        'termination_message_path': 'terminationMessagePath',
        'termination_message_policy': 'terminationMessagePolicy',
        'tty': 'tty',
        'volume_devices': 'volumeDevices',
        'volume_mounts': 'volumeMounts',
        'working_dir': 'workingDir'
    }

    def __init__(self, args=None, command=None, env=None, env_from=None, image=None, image_pull_policy=None, lifecycle=None, liveness_probe=None, name=None, ports=None, readiness_probe=None, resize_policy=None, resources=None, restart_policy=None, security_context=None, startup_probe=None, stdin=None, stdin_once=None, termination_message_path=None, termination_message_policy=None, tty=None, volume_devices=None, volume_mounts=None, working_dir=None):  # noqa: E501
        """Container - a model defined in Swagger"""  # noqa: E501

        self._args = None
        self._command = None
        self._env = None
        self._env_from = None
        self._image = None
        self._image_pull_policy = None
        self._lifecycle = None
        self._liveness_probe = None
        self._name = None
        self._ports = None
        self._readiness_probe = None
        self._resize_policy = None
        self._resources = None
        self._restart_policy = None
        self._security_context = None
        self._startup_probe = None
        self._stdin = None
        self._stdin_once = None
        self._termination_message_path = None
        self._termination_message_policy = None
        self._tty = None
        self._volume_devices = None
        self._volume_mounts = None
        self._working_dir = None
        self.discriminator = None

        if args is not None:
            self.args = args
        if command is not None:
            self.command = command
        if env is not None:
            self.env = env
        if env_from is not None:
            self.env_from = env_from
        if image is not None:
            self.image = image
        if image_pull_policy is not None:
            self.image_pull_policy = image_pull_policy
        if lifecycle is not None:
            self.lifecycle = lifecycle
        if liveness_probe is not None:
            self.liveness_probe = liveness_probe
        if name is not None:
            self.name = name
        if ports is not None:
            self.ports = ports
        if readiness_probe is not None:
            self.readiness_probe = readiness_probe
        if resize_policy is not None:
            self.resize_policy = resize_policy
        if resources is not None:
            self.resources = resources
        if restart_policy is not None:
            self.restart_policy = restart_policy
        if security_context is not None:
            self.security_context = security_context
        if startup_probe is not None:
            self.startup_probe = startup_probe
        if stdin is not None:
            self.stdin = stdin
        if stdin_once is not None:
            self.stdin_once = stdin_once
        if termination_message_path is not None:
            self.termination_message_path = termination_message_path
        if termination_message_policy is not None:
            self.termination_message_policy = termination_message_policy
        if tty is not None:
            self.tty = tty
        if volume_devices is not None:
            self.volume_devices = volume_devices
        if volume_mounts is not None:
            self.volume_mounts = volume_mounts
        if working_dir is not None:
            self.working_dir = working_dir

    @property
    def args(self):
        """Gets the args of this Container.  # noqa: E501

        Arguments to the entrypoint. The container image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \"$$(VAR_NAME)\" will produce the string literal \"$(VAR_NAME)\". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell +optional  # noqa: E501

        :return: The args of this Container.  # noqa: E501
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this Container.

        Arguments to the entrypoint. The container image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \"$$(VAR_NAME)\" will produce the string literal \"$(VAR_NAME)\". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell +optional  # noqa: E501

        :param args: The args of this Container.  # noqa: E501
        :type: list[str]
        """

        self._args = args

    @property
    def command(self):
        """Gets the command of this Container.  # noqa: E501

        Entrypoint array. Not executed within a shell. The container image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \"$$(VAR_NAME)\" will produce the string literal \"$(VAR_NAME)\". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell +optional  # noqa: E501

        :return: The command of this Container.  # noqa: E501
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this Container.

        Entrypoint array. Not executed within a shell. The container image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \"$$(VAR_NAME)\" will produce the string literal \"$(VAR_NAME)\". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell +optional  # noqa: E501

        :param command: The command of this Container.  # noqa: E501
        :type: list[str]
        """

        self._command = command

    @property
    def env(self):
        """Gets the env of this Container.  # noqa: E501

        List of environment variables to set in the container. Cannot be updated. +optional +patchMergeKey=name +patchStrategy=merge  # noqa: E501

        :return: The env of this Container.  # noqa: E501
        :rtype: list[EnvVar]
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this Container.

        List of environment variables to set in the container. Cannot be updated. +optional +patchMergeKey=name +patchStrategy=merge  # noqa: E501

        :param env: The env of this Container.  # noqa: E501
        :type: list[EnvVar]
        """

        self._env = env

    @property
    def env_from(self):
        """Gets the env_from of this Container.  # noqa: E501

        List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated. +optional  # noqa: E501

        :return: The env_from of this Container.  # noqa: E501
        :rtype: list[EnvFromSource]
        """
        return self._env_from

    @env_from.setter
    def env_from(self, env_from):
        """Sets the env_from of this Container.

        List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated. +optional  # noqa: E501

        :param env_from: The env_from of this Container.  # noqa: E501
        :type: list[EnvFromSource]
        """

        self._env_from = env_from

    @property
    def image(self):
        """Gets the image of this Container.  # noqa: E501

        Container image name. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets. +optional  # noqa: E501

        :return: The image of this Container.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Container.

        Container image name. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets. +optional  # noqa: E501

        :param image: The image of this Container.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def image_pull_policy(self):
        """Gets the image_pull_policy of this Container.  # noqa: E501


        :return: The image_pull_policy of this Container.  # noqa: E501
        :rtype: PullPolicy
        """
        return self._image_pull_policy

    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy):
        """Sets the image_pull_policy of this Container.


        :param image_pull_policy: The image_pull_policy of this Container.  # noqa: E501
        :type: PullPolicy
        """

        self._image_pull_policy = image_pull_policy

    @property
    def lifecycle(self):
        """Gets the lifecycle of this Container.  # noqa: E501


        :return: The lifecycle of this Container.  # noqa: E501
        :rtype: Lifecycle
        """
        return self._lifecycle

    @lifecycle.setter
    def lifecycle(self, lifecycle):
        """Sets the lifecycle of this Container.


        :param lifecycle: The lifecycle of this Container.  # noqa: E501
        :type: Lifecycle
        """

        self._lifecycle = lifecycle

    @property
    def liveness_probe(self):
        """Gets the liveness_probe of this Container.  # noqa: E501


        :return: The liveness_probe of this Container.  # noqa: E501
        :rtype: Probe
        """
        return self._liveness_probe

    @liveness_probe.setter
    def liveness_probe(self, liveness_probe):
        """Sets the liveness_probe of this Container.


        :param liveness_probe: The liveness_probe of this Container.  # noqa: E501
        :type: Probe
        """

        self._liveness_probe = liveness_probe

    @property
    def name(self):
        """Gets the name of this Container.  # noqa: E501

        Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.  # noqa: E501

        :return: The name of this Container.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Container.

        Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.  # noqa: E501

        :param name: The name of this Container.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ports(self):
        """Gets the ports of this Container.  # noqa: E501

        List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default \"0.0.0.0\" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See https://github.com/kubernetes/kubernetes/issues/108255. Cannot be updated. +optional +patchMergeKey=containerPort +patchStrategy=merge +listType=map +listMapKey=containerPort +listMapKey=protocol  # noqa: E501

        :return: The ports of this Container.  # noqa: E501
        :rtype: list[ContainerPort]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this Container.

        List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default \"0.0.0.0\" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See https://github.com/kubernetes/kubernetes/issues/108255. Cannot be updated. +optional +patchMergeKey=containerPort +patchStrategy=merge +listType=map +listMapKey=containerPort +listMapKey=protocol  # noqa: E501

        :param ports: The ports of this Container.  # noqa: E501
        :type: list[ContainerPort]
        """

        self._ports = ports

    @property
    def readiness_probe(self):
        """Gets the readiness_probe of this Container.  # noqa: E501


        :return: The readiness_probe of this Container.  # noqa: E501
        :rtype: Probe
        """
        return self._readiness_probe

    @readiness_probe.setter
    def readiness_probe(self, readiness_probe):
        """Sets the readiness_probe of this Container.


        :param readiness_probe: The readiness_probe of this Container.  # noqa: E501
        :type: Probe
        """

        self._readiness_probe = readiness_probe

    @property
    def resize_policy(self):
        """Gets the resize_policy of this Container.  # noqa: E501

        Resources resize policy for the container. +featureGate=InPlacePodVerticalScaling +optional +listType=atomic  # noqa: E501

        :return: The resize_policy of this Container.  # noqa: E501
        :rtype: list[ContainerResizePolicy]
        """
        return self._resize_policy

    @resize_policy.setter
    def resize_policy(self, resize_policy):
        """Sets the resize_policy of this Container.

        Resources resize policy for the container. +featureGate=InPlacePodVerticalScaling +optional +listType=atomic  # noqa: E501

        :param resize_policy: The resize_policy of this Container.  # noqa: E501
        :type: list[ContainerResizePolicy]
        """

        self._resize_policy = resize_policy

    @property
    def resources(self):
        """Gets the resources of this Container.  # noqa: E501


        :return: The resources of this Container.  # noqa: E501
        :rtype: ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this Container.


        :param resources: The resources of this Container.  # noqa: E501
        :type: ResourceRequirements
        """

        self._resources = resources

    @property
    def restart_policy(self):
        """Gets the restart_policy of this Container.  # noqa: E501


        :return: The restart_policy of this Container.  # noqa: E501
        :rtype: ContainerRestartPolicy
        """
        return self._restart_policy

    @restart_policy.setter
    def restart_policy(self, restart_policy):
        """Sets the restart_policy of this Container.


        :param restart_policy: The restart_policy of this Container.  # noqa: E501
        :type: ContainerRestartPolicy
        """

        self._restart_policy = restart_policy

    @property
    def security_context(self):
        """Gets the security_context of this Container.  # noqa: E501


        :return: The security_context of this Container.  # noqa: E501
        :rtype: SecurityContext
        """
        return self._security_context

    @security_context.setter
    def security_context(self, security_context):
        """Sets the security_context of this Container.


        :param security_context: The security_context of this Container.  # noqa: E501
        :type: SecurityContext
        """

        self._security_context = security_context

    @property
    def startup_probe(self):
        """Gets the startup_probe of this Container.  # noqa: E501


        :return: The startup_probe of this Container.  # noqa: E501
        :rtype: Probe
        """
        return self._startup_probe

    @startup_probe.setter
    def startup_probe(self, startup_probe):
        """Sets the startup_probe of this Container.


        :param startup_probe: The startup_probe of this Container.  # noqa: E501
        :type: Probe
        """

        self._startup_probe = startup_probe

    @property
    def stdin(self):
        """Gets the stdin of this Container.  # noqa: E501

        Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false. +optional  # noqa: E501

        :return: The stdin of this Container.  # noqa: E501
        :rtype: bool
        """
        return self._stdin

    @stdin.setter
    def stdin(self, stdin):
        """Sets the stdin of this Container.

        Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false. +optional  # noqa: E501

        :param stdin: The stdin of this Container.  # noqa: E501
        :type: bool
        """

        self._stdin = stdin

    @property
    def stdin_once(self):
        """Gets the stdin_once of this Container.  # noqa: E501

        Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false +optional  # noqa: E501

        :return: The stdin_once of this Container.  # noqa: E501
        :rtype: bool
        """
        return self._stdin_once

    @stdin_once.setter
    def stdin_once(self, stdin_once):
        """Sets the stdin_once of this Container.

        Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false +optional  # noqa: E501

        :param stdin_once: The stdin_once of this Container.  # noqa: E501
        :type: bool
        """

        self._stdin_once = stdin_once

    @property
    def termination_message_path(self):
        """Gets the termination_message_path of this Container.  # noqa: E501

        Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated. +optional  # noqa: E501

        :return: The termination_message_path of this Container.  # noqa: E501
        :rtype: str
        """
        return self._termination_message_path

    @termination_message_path.setter
    def termination_message_path(self, termination_message_path):
        """Sets the termination_message_path of this Container.

        Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated. +optional  # noqa: E501

        :param termination_message_path: The termination_message_path of this Container.  # noqa: E501
        :type: str
        """

        self._termination_message_path = termination_message_path

    @property
    def termination_message_policy(self):
        """Gets the termination_message_policy of this Container.  # noqa: E501


        :return: The termination_message_policy of this Container.  # noqa: E501
        :rtype: TerminationMessagePolicy
        """
        return self._termination_message_policy

    @termination_message_policy.setter
    def termination_message_policy(self, termination_message_policy):
        """Sets the termination_message_policy of this Container.


        :param termination_message_policy: The termination_message_policy of this Container.  # noqa: E501
        :type: TerminationMessagePolicy
        """

        self._termination_message_policy = termination_message_policy

    @property
    def tty(self):
        """Gets the tty of this Container.  # noqa: E501

        Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false. +optional  # noqa: E501

        :return: The tty of this Container.  # noqa: E501
        :rtype: bool
        """
        return self._tty

    @tty.setter
    def tty(self, tty):
        """Sets the tty of this Container.

        Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false. +optional  # noqa: E501

        :param tty: The tty of this Container.  # noqa: E501
        :type: bool
        """

        self._tty = tty

    @property
    def volume_devices(self):
        """Gets the volume_devices of this Container.  # noqa: E501

        volumeDevices is the list of block devices to be used by the container. +patchMergeKey=devicePath +patchStrategy=merge +optional  # noqa: E501

        :return: The volume_devices of this Container.  # noqa: E501
        :rtype: list[VolumeDevice]
        """
        return self._volume_devices

    @volume_devices.setter
    def volume_devices(self, volume_devices):
        """Sets the volume_devices of this Container.

        volumeDevices is the list of block devices to be used by the container. +patchMergeKey=devicePath +patchStrategy=merge +optional  # noqa: E501

        :param volume_devices: The volume_devices of this Container.  # noqa: E501
        :type: list[VolumeDevice]
        """

        self._volume_devices = volume_devices

    @property
    def volume_mounts(self):
        """Gets the volume_mounts of this Container.  # noqa: E501

        Pod volumes to mount into the container's filesystem. Cannot be updated. +optional +patchMergeKey=mountPath +patchStrategy=merge  # noqa: E501

        :return: The volume_mounts of this Container.  # noqa: E501
        :rtype: list[VolumeMount]
        """
        return self._volume_mounts

    @volume_mounts.setter
    def volume_mounts(self, volume_mounts):
        """Sets the volume_mounts of this Container.

        Pod volumes to mount into the container's filesystem. Cannot be updated. +optional +patchMergeKey=mountPath +patchStrategy=merge  # noqa: E501

        :param volume_mounts: The volume_mounts of this Container.  # noqa: E501
        :type: list[VolumeMount]
        """

        self._volume_mounts = volume_mounts

    @property
    def working_dir(self):
        """Gets the working_dir of this Container.  # noqa: E501

        Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. +optional  # noqa: E501

        :return: The working_dir of this Container.  # noqa: E501
        :rtype: str
        """
        return self._working_dir

    @working_dir.setter
    def working_dir(self, working_dir):
        """Sets the working_dir of this Container.

        Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. +optional  # noqa: E501

        :param working_dir: The working_dir of this Container.  # noqa: E501
        :type: str
        """

        self._working_dir = working_dir

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
        if issubclass(Container, dict):
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
        if not isinstance(other, Container):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
