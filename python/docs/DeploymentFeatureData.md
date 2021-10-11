# DeploymentFeatureData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregate_over_time** | **bool** | AggregateOverTime is a boolean to decide if the distribution response is to be aggregated over the time period selected | [optional] 
**deployment_kind** | **str** | DeploymentType refers to kubernetes kind of the deployment relevant to the feature distribution query | [optional] 
**deployment_name** | **str** | DeploymentName refers to name of the deployment relevant to the feature distribution query | [optional] 
**deployment_namespace** | **str** | DeploymentNamespace refers to namespace of the deployment relevant to the feature distribution query | [optional] 
**feature** | **str** | FeatureName refers to the name of feature as per the model predictions schema | [optional] 
**filters** | [**list[FeatureFilter]**](FeatureFilter.md) | Filters is a set of time, feature and/or outlier filters for the distribution/stats query | [optional] 
**interaction** | [**FeatureInteraction**](FeatureInteraction.md) |  | [optional] 
**parameters** | [**FeatureDistributionParameters**](FeatureDistributionParameters.md) |  | [optional] 
**reference_data** | **bool** | ReferenceData is a boolean to compute stats and distributions over reference data or inference data (false by default) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


