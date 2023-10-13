# BatchJobDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_data_type** | **str** | Batch Data Type (data, json or str) | [optional] 
**batch_interval** | **float** | Interval between batches | [optional] 
**batch_method** | **str** | Batch Method (predict, feedback (for SCv1)) | [optional] 
**batch_payload_type** | **str** | Batch Payload Type (ndarray, tensor, tftensor, v2raw, v2binary - only if DataType&#x3D;data) | [optional] 
**batch_retries** | **int** | Number of retries for each instance | [optional] 
**batch_size** | **int** | Size of the batch (number of predictions per request) | [optional] 
**batch_transport_protocol** | **str** | Batch Transport Protocol (rest or grpc) | [optional] 
**batch_workers** | **int** | Number of batch workers | [optional] 
**input_data** | **str** | S3 URI of input data file | [optional] 
**limits_cpu** | **str** | Container Resources for running batch jobs: limits: CPU | [optional] 
**limits_memory** | **str** | Container Resources for running batch jobs: limits: Memory | [optional] 
**object_store_secret_name** | **str** | name of Kubernetes Secret with S3 credentials | [optional] 
**output_data** | **str** | S3 URI of output data file | [optional] 
**pvc_size** | **str** | Size of PVC required for the batch job | [optional] 
**requests_cpu** | **str** | Container Resources for running batch jobs: requests: CPU | [optional] 
**requests_memory** | **str** | Container Resources for running batch jobs: requests: Memory | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


