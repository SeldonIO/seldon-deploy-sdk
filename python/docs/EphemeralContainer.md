# EphemeralContainer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **list[str]** | Arguments to the entrypoint. The image&#39;s CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container&#39;s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \&quot;$$(VAR_NAME)\&quot; will produce the string literal \&quot;$(VAR_NAME)\&quot;. Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell +optional | [optional] 
**command** | **list[str]** | Entrypoint array. Not executed within a shell. The image&#39;s ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container&#39;s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \&quot;$$(VAR_NAME)\&quot; will produce the string literal \&quot;$(VAR_NAME)\&quot;. Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell +optional | [optional] 
**env** | [**list[EnvVar]**](EnvVar.md) | List of environment variables to set in the container. Cannot be updated. +optional +patchMergeKey&#x3D;name +patchStrategy&#x3D;merge | [optional] 
**env_from** | [**list[EnvFromSource]**](EnvFromSource.md) | List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated. +optional | [optional] 
**image** | **str** | Container image name. More info: https://kubernetes.io/docs/concepts/containers/images | [optional] 
**image_pull_policy** | [**PullPolicy**](PullPolicy.md) |  | [optional] 
**lifecycle** | [**Lifecycle**](Lifecycle.md) |  | [optional] 
**liveness_probe** | [**Probe**](Probe.md) |  | [optional] 
**name** | **str** | Name of the ephemeral container specified as a DNS_LABEL. This name must be unique among all containers, init containers and ephemeral containers. | [optional] 
**ports** | [**list[ContainerPort]**](ContainerPort.md) | Ports are not allowed for ephemeral containers. +optional +patchMergeKey&#x3D;containerPort +patchStrategy&#x3D;merge +listType&#x3D;map +listMapKey&#x3D;containerPort +listMapKey&#x3D;protocol | [optional] 
**readiness_probe** | [**Probe**](Probe.md) |  | [optional] 
**resize_policy** | [**list[ContainerResizePolicy]**](ContainerResizePolicy.md) | Resources resize policy for the container. +featureGate&#x3D;InPlacePodVerticalScaling +optional +listType&#x3D;atomic | [optional] 
**resources** | [**ResourceRequirements**](ResourceRequirements.md) |  | [optional] 
**restart_policy** | [**ContainerRestartPolicy**](ContainerRestartPolicy.md) |  | [optional] 
**security_context** | [**SecurityContext**](SecurityContext.md) |  | [optional] 
**startup_probe** | [**Probe**](Probe.md) |  | [optional] 
**stdin** | **bool** | Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false. +optional | [optional] 
**stdin_once** | **bool** | Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false +optional | [optional] 
**target_container_name** | **str** | If set, the name of the container from PodSpec that this ephemeral container targets. The ephemeral container will be run in the namespaces (IPC, PID, etc) of this container. If not set then the ephemeral container uses the namespaces configured in the Pod spec.  The container runtime must implement support for this feature. If the runtime does not support namespace targeting then the result of setting this field is undefined. +optional | [optional] 
**termination_message_path** | **str** | Optional: Path at which the file to which the container&#39;s termination message will be written is mounted into the container&#39;s filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated. +optional | [optional] 
**termination_message_policy** | [**TerminationMessagePolicy**](TerminationMessagePolicy.md) |  | [optional] 
**tty** | **bool** | Whether this container should allocate a TTY for itself, also requires &#39;stdin&#39; to be true. Default is false. +optional | [optional] 
**volume_devices** | [**list[VolumeDevice]**](VolumeDevice.md) | volumeDevices is the list of block devices to be used by the container. +patchMergeKey&#x3D;devicePath +patchStrategy&#x3D;merge +optional | [optional] 
**volume_mounts** | [**list[VolumeMount]**](VolumeMount.md) | Pod volumes to mount into the container&#39;s filesystem. Subpath mounts are not allowed for ephemeral containers. Cannot be updated. +optional +patchMergeKey&#x3D;mountPath +patchStrategy&#x3D;merge | [optional] 
**working_dir** | **str** | Container&#39;s working directory. If not specified, the container runtime&#39;s default will be used, which might be configured in the container image. Cannot be updated. +optional | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


