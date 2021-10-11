# BatchJobDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_data_type** | **str** | Batch Data Type (data, json or str) | [optional] 
**batch_gateway_endpoint** | **str** | Batch Gateway Endpoint | [optional] 
**batch_gateway_type** | **str** | Batch Gateway Type (istio or seldon) | [optional] 
**batch_interval** | **float** | Size of the batch (number of predictions per request) | [optional] 
**batch_method** | **str** | Batch Method (predict) | [optional] 
**batch_payload_type** | **str** | Batch Payload Type (ndarray, tensor, tftensor - only if DataType&#x3D;data) | [optional] 
**batch_retries** | **str** | Number of retries for each instance | [optional] 
**batch_size** | **int** | Size of the batch (number of predictions per request) | [optional] 
**batch_transport_protocol** | **str** | Batch Transport Protocol (rest or grpc) | [optional] 
**batch_workers** | **str** | Number of batch workers | [optional] 
**input_data** | **str** | S3 URI of input data file | [optional] 
**object_store_secret_name** | **str** | name of Kubernetes Secret with S3 credentials | [optional] 
**output_data** | **str** | S3 URI of output data file | [optional] 
**pvc_size** | **str** | Size of PVC required for the batch job | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


