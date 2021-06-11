# FeatureFilter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_name** | **str** | CategoryName refers to name of the feature category relevant to PROBA and ONE_HOT features | [optional] 
**feature** | **str** | FeatureName refers to the name of feature as per the model predictions schema | [optional] 
**gt** | **str** | GreaterThan refers to numerical value of the feature filter relevant for timestamps or REAL features | [optional] 
**gte** | **str** | GreaterThanOrEqual refers to numerical value of the feature filter relevant for timestamps or REAL features | [optional] 
**interaction** | [**FeatureInteraction**](FeatureInteraction.md) |  | [optional] 
**is_outlier** | **bool** | IsOutlier refers to boolean for outlier filters | [optional] 
**is_timestamp** | **bool** | IsTimestamp refers to boolean for timestamp filters | [optional] 
**lt** | **str** | LessThan refers to numerical value of the feature filter relevant for timestamps or REAL features | [optional] 
**lte** | **str** | LessThanOrEqual refers to numerical value of the feature filter relevant for timestamps or REAL features | [optional] 
**terms** | **list[str]** | Terms refers to set of feature categories to filter relevant to CATEGORICAL features | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


