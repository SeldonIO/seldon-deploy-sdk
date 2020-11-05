# Container

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **list[str]** | Arguments to the entrypoint. The docker image&#39;s CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container&#39;s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell +optional | [optional] 
**command** | **list[str]** | Entrypoint array. Not executed within a shell. The docker image&#39;s ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container&#39;s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell +optional | [optional] 
**env** | [**list[EnvVar]**](EnvVar.md) | List of environment variables to set in the container. Cannot be updated. +optional +patchMergeKey&#x3D;name +patchStrategy&#x3D;merge | [optional] 
**env_from** | [**list[EnvFromSource]**](EnvFromSource.md) | List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated. +optional | [optional] 
**image** | **str** | Docker image name. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets. +optional | [optional] 
**image_pull_policy** | [**PullPolicy**](PullPolicy.md) |  | [optional] 
**lifecycle** | [**Lifecycle**](Lifecycle.md) |  | [optional] 
**liveness_probe** | [**Probe**](Probe.md) |  | [optional] 
**name** | **str** | Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. | [optional] 
**ports** | [**list[ContainerPort]**](ContainerPort.md) | List of ports to expose from the container. Exposing a port here gives the system additional information about the network connections a container uses, but is primarily informational. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default \&quot;0.0.0.0\&quot; address inside a container will be accessible from the network. Cannot be updated. +optional +patchMergeKey&#x3D;containerPort +patchStrategy&#x3D;merge +listType&#x3D;map +listMapKey&#x3D;containerPort +listMapKey&#x3D;protocol | [optional] 
**readiness_probe** | [**Probe**](Probe.md) |  | [optional] 
**resources** | [**ResourceRequirements**](ResourceRequirements.md) |  | [optional] 
**security_context** | [**SecurityContext**](SecurityContext.md) |  | [optional] 
**startup_probe** | [**Probe**](Probe.md) |  | [optional] 
**stdin** | **bool** | Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false. +optional | [optional] 
**stdin_once** | **bool** | Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false +optional | [optional] 
**termination_message_path** | **str** | Optional: Path at which the file to which the container&#39;s termination message will be written is mounted into the container&#39;s filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated. +optional | [optional] 
**termination_message_policy** | [**TerminationMessagePolicy**](TerminationMessagePolicy.md) |  | [optional] 
**tty** | **bool** | Whether this container should allocate a TTY for itself, also requires &#39;stdin&#39; to be true. Default is false. +optional | [optional] 
**volume_devices** | [**list[VolumeDevice]**](VolumeDevice.md) | volumeDevices is the list of block devices to be used by the container. This is a beta feature. +patchMergeKey&#x3D;devicePath +patchStrategy&#x3D;merge +optional | [optional] 
**volume_mounts** | [**list[VolumeMount]**](VolumeMount.md) | Pod volumes to mount into the container&#39;s filesystem. Cannot be updated. +optional +patchMergeKey&#x3D;mountPath +patchStrategy&#x3D;merge | [optional] 
**working_dir** | **str** | Container&#39;s working directory. If not specified, the container runtime&#39;s default will be used, which might be configured in the container image. Cannot be updated. +optional | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


