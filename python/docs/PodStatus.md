# PodStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[PodCondition]**](PodCondition.md) | Current service state of pod. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions +optional +patchMergeKey&#x3D;type +patchStrategy&#x3D;merge | [optional] 
**container_statuses** | [**list[ContainerStatus]**](ContainerStatus.md) | The list has one entry per container in the manifest. Each entry is currently the output of &#x60;docker inspect&#x60;. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status +optional | [optional] 
**ephemeral_container_statuses** | [**list[ContainerStatus]**](ContainerStatus.md) | Status for any ephemeral containers that have run in this pod. This field is alpha-level and is only populated by servers that enable the EphemeralContainers feature. +optional | [optional] 
**host_ip** | **str** | IP address of the host to which the pod is assigned. Empty if not yet scheduled. +optional | [optional] 
**init_container_statuses** | [**list[ContainerStatus]**](ContainerStatus.md) | The list has one entry per init container in the manifest. The most recent successful init container will have ready &#x3D; true, the most recently started container will have startTime set. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status | [optional] 
**message** | **str** | A human readable message indicating details about why the pod is in this condition. +optional | [optional] 
**nominated_node_name** | **str** | nominatedNodeName is set only when this pod preempts other pods on the node, but it cannot be scheduled right away as preemption victims receive their graceful termination periods. This field does not guarantee that the pod will be scheduled on this node. Scheduler may decide to place the pod elsewhere if other nodes become available sooner. Scheduler may also decide to give the resources on this node to a higher priority pod that is created after preemption. As a result, this field may be different than PodSpec.nodeName when the pod is scheduled. +optional | [optional] 
**phase** | [**PodPhase**](PodPhase.md) |  | [optional] 
**pod_ip** | **str** | IP address allocated to the pod. Routable at least within the cluster. Empty if not yet allocated. +optional | [optional] 
**pod_i_ps** | [**list[PodIP]**](PodIP.md) | podIPs holds the IP addresses allocated to the pod. If this field is specified, the 0th entry must match the podIP field. Pods may be allocated at most 1 value for each of IPv4 and IPv6. This list is empty if no IPs have been allocated yet. +optional +patchStrategy&#x3D;merge +patchMergeKey&#x3D;ip | [optional] 
**qos_class** | [**PodQOSClass**](PodQOSClass.md) |  | [optional] 
**reason** | **str** | A brief CamelCase message indicating details about why the pod is in this state. e.g. &#39;Evicted&#39; +optional | [optional] 
**start_time** | **str** | RFC 3339 date and time at which the object was acknowledged by the Kubelet. This is before the Kubelet pulled the container image(s) for the pod. +optional | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


