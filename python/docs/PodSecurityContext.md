# PodSecurityContext

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_group** | **int** | A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod:  1. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3. The permission bits are OR&#39;d with rw-rw----  If unset, the Kubelet will not modify the ownership and permissions of any volume. Note that this field cannot be set when spec.os.name is windows. +optional | [optional] 
**fs_group_change_policy** | [**PodFSGroupChangePolicy**](PodFSGroupChangePolicy.md) |  | [optional] 
**run_as_group** | **int** | The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows. +optional | [optional] 
**run_as_non_root** | **bool** | Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. +optional | [optional] 
**run_as_user** | **int** | The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows. +optional | [optional] 
**se_linux_options** | [**SELinuxOptions**](SELinuxOptions.md) |  | [optional] 
**seccomp_profile** | [**SeccompProfile**](SeccompProfile.md) |  | [optional] 
**supplemental_groups** | **list[int]** | A list of groups applied to the first process run in each container, in addition to the container&#39;s primary GID, the fsGroup (if specified), and group memberships defined in the container image for the uid of the container process. If unspecified, no additional groups are added to any container. Note that group memberships defined in the container image for the uid of the container process are still effective, even if they are not included in this list. Note that this field cannot be set when spec.os.name is windows. +optional | [optional] 
**sysctls** | [**list[Sysctl]**](Sysctl.md) | Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch. Note that this field cannot be set when spec.os.name is windows. +optional | [optional] 
**windows_options** | [**WindowsSecurityContextOptions**](WindowsSecurityContextOptions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


