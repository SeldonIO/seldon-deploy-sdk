# TopologySpreadConstraint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_selector** | [**LabelSelector**](LabelSelector.md) |  | [optional] 
**max_skew** | **int** | MaxSkew describes the degree to which pods may be unevenly distributed. It&#39;s the maximum permitted difference between the number of matching pods in any two topology domains of a given topology type. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 1/1/0: +-------+-------+-------+  zone1 | zone2 | zone3 | +-------+-------+-------+    P   |   P   |       | +-------+-------+-------+ if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become 1/1/1; scheduling it onto zone1(zone2) would make the ActualSkew(2-0) on zone1(zone2) violate MaxSkew(1). if MaxSkew is 2, incoming pod can be scheduled onto any zone. It&#39;s a required field. Default value is 1 and 0 is not allowed. | [optional] 
**topology_key** | **str** | TopologyKey is the key of node labels. Nodes that have a label with this key and identical values are considered to be in the same topology. We consider each &lt;key, value&gt; as a \&quot;bucket\&quot;, and try to put balanced number of pods into each bucket. It&#39;s a required field. | [optional] 
**when_unsatisfiable** | [**UnsatisfiableConstraintAction**](UnsatisfiableConstraintAction.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


