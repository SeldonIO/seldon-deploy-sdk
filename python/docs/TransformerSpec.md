# TransformerSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batcher** | [**Batcher**](Batcher.md) |  | [optional] 
**custom** | [**CustomSpec**](CustomSpec.md) |  | [optional] 
**logger** | [**Logger**](Logger.md) |  | [optional] 
**max_replicas** | **int** | This is the up bound for autoscaler to scale to +optional | [optional] 
**min_replicas** | **int** | Minimum number of replicas which defaults to 1, when minReplicas &#x3D; 0 pods scale down to 0 in case of no traffic +optional | [optional] 
**parallelism** | **int** | Parallelism specifies how many requests can be processed concurrently, this sets the hard limit of the container concurrency(https://knative.dev/docs/serving/autoscaling/concurrency). | [optional] 
**service_account_name** | **str** | ServiceAccountName is the name of the ServiceAccount to use to run the service +optional | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


