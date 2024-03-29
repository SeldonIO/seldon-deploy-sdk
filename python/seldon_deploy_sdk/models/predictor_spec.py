# coding: utf-8

"""
    Seldon Deploy API

    API to interact and manage the lifecycle of your machine learning models deployed through Seldon Deploy.  # noqa: E501

    OpenAPI spec version: v1alpha1
    Contact: hello@seldon.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PredictorSpec(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'annotations': 'dict(str, str)',
        'component_specs': 'list[SeldonPodSpec]',
        'engine_resources': 'ResourceRequirements',
        'explainer': 'Explainer',
        'graph': 'PredictiveUnit',
        'labels': 'dict(str, str)',
        'name': 'str',
        'progress_deadline_seconds': 'int',
        'replicas': 'int',
        'shadow': 'bool',
        'ssl': 'SSL',
        'svc_orch_spec': 'SvcOrchSpec',
        'traffic': 'int'
    }

    attribute_map = {
        'annotations': 'annotations',
        'component_specs': 'componentSpecs',
        'engine_resources': 'engineResources',
        'explainer': 'explainer',
        'graph': 'graph',
        'labels': 'labels',
        'name': 'name',
        'progress_deadline_seconds': 'progressDeadlineSeconds',
        'replicas': 'replicas',
        'shadow': 'shadow',
        'ssl': 'ssl',
        'svc_orch_spec': 'svcOrchSpec',
        'traffic': 'traffic'
    }

    def __init__(self, annotations=None, component_specs=None, engine_resources=None, explainer=None, graph=None, labels=None, name=None, progress_deadline_seconds=None, replicas=None, shadow=None, ssl=None, svc_orch_spec=None, traffic=None):  # noqa: E501
        """PredictorSpec - a model defined in Swagger"""  # noqa: E501

        self._annotations = None
        self._component_specs = None
        self._engine_resources = None
        self._explainer = None
        self._graph = None
        self._labels = None
        self._name = None
        self._progress_deadline_seconds = None
        self._replicas = None
        self._shadow = None
        self._ssl = None
        self._svc_orch_spec = None
        self._traffic = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if component_specs is not None:
            self.component_specs = component_specs
        if engine_resources is not None:
            self.engine_resources = engine_resources
        if explainer is not None:
            self.explainer = explainer
        if graph is not None:
            self.graph = graph
        if labels is not None:
            self.labels = labels
        if name is not None:
            self.name = name
        if progress_deadline_seconds is not None:
            self.progress_deadline_seconds = progress_deadline_seconds
        if replicas is not None:
            self.replicas = replicas
        if shadow is not None:
            self.shadow = shadow
        if ssl is not None:
            self.ssl = ssl
        if svc_orch_spec is not None:
            self.svc_orch_spec = svc_orch_spec
        if traffic is not None:
            self.traffic = traffic

    @property
    def annotations(self):
        """Gets the annotations of this PredictorSpec.  # noqa: E501


        :return: The annotations of this PredictorSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this PredictorSpec.


        :param annotations: The annotations of this PredictorSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._annotations = annotations

    @property
    def component_specs(self):
        """Gets the component_specs of this PredictorSpec.  # noqa: E501


        :return: The component_specs of this PredictorSpec.  # noqa: E501
        :rtype: list[SeldonPodSpec]
        """
        return self._component_specs

    @component_specs.setter
    def component_specs(self, component_specs):
        """Sets the component_specs of this PredictorSpec.


        :param component_specs: The component_specs of this PredictorSpec.  # noqa: E501
        :type: list[SeldonPodSpec]
        """

        self._component_specs = component_specs

    @property
    def engine_resources(self):
        """Gets the engine_resources of this PredictorSpec.  # noqa: E501


        :return: The engine_resources of this PredictorSpec.  # noqa: E501
        :rtype: ResourceRequirements
        """
        return self._engine_resources

    @engine_resources.setter
    def engine_resources(self, engine_resources):
        """Sets the engine_resources of this PredictorSpec.


        :param engine_resources: The engine_resources of this PredictorSpec.  # noqa: E501
        :type: ResourceRequirements
        """

        self._engine_resources = engine_resources

    @property
    def explainer(self):
        """Gets the explainer of this PredictorSpec.  # noqa: E501


        :return: The explainer of this PredictorSpec.  # noqa: E501
        :rtype: Explainer
        """
        return self._explainer

    @explainer.setter
    def explainer(self, explainer):
        """Sets the explainer of this PredictorSpec.


        :param explainer: The explainer of this PredictorSpec.  # noqa: E501
        :type: Explainer
        """

        self._explainer = explainer

    @property
    def graph(self):
        """Gets the graph of this PredictorSpec.  # noqa: E501


        :return: The graph of this PredictorSpec.  # noqa: E501
        :rtype: PredictiveUnit
        """
        return self._graph

    @graph.setter
    def graph(self, graph):
        """Sets the graph of this PredictorSpec.


        :param graph: The graph of this PredictorSpec.  # noqa: E501
        :type: PredictiveUnit
        """

        self._graph = graph

    @property
    def labels(self):
        """Gets the labels of this PredictorSpec.  # noqa: E501


        :return: The labels of this PredictorSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this PredictorSpec.


        :param labels: The labels of this PredictorSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def name(self):
        """Gets the name of this PredictorSpec.  # noqa: E501


        :return: The name of this PredictorSpec.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PredictorSpec.


        :param name: The name of this PredictorSpec.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def progress_deadline_seconds(self):
        """Gets the progress_deadline_seconds of this PredictorSpec.  # noqa: E501


        :return: The progress_deadline_seconds of this PredictorSpec.  # noqa: E501
        :rtype: int
        """
        return self._progress_deadline_seconds

    @progress_deadline_seconds.setter
    def progress_deadline_seconds(self, progress_deadline_seconds):
        """Sets the progress_deadline_seconds of this PredictorSpec.


        :param progress_deadline_seconds: The progress_deadline_seconds of this PredictorSpec.  # noqa: E501
        :type: int
        """

        self._progress_deadline_seconds = progress_deadline_seconds

    @property
    def replicas(self):
        """Gets the replicas of this PredictorSpec.  # noqa: E501


        :return: The replicas of this PredictorSpec.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this PredictorSpec.


        :param replicas: The replicas of this PredictorSpec.  # noqa: E501
        :type: int
        """

        self._replicas = replicas

    @property
    def shadow(self):
        """Gets the shadow of this PredictorSpec.  # noqa: E501


        :return: The shadow of this PredictorSpec.  # noqa: E501
        :rtype: bool
        """
        return self._shadow

    @shadow.setter
    def shadow(self, shadow):
        """Sets the shadow of this PredictorSpec.


        :param shadow: The shadow of this PredictorSpec.  # noqa: E501
        :type: bool
        """

        self._shadow = shadow

    @property
    def ssl(self):
        """Gets the ssl of this PredictorSpec.  # noqa: E501


        :return: The ssl of this PredictorSpec.  # noqa: E501
        :rtype: SSL
        """
        return self._ssl

    @ssl.setter
    def ssl(self, ssl):
        """Sets the ssl of this PredictorSpec.


        :param ssl: The ssl of this PredictorSpec.  # noqa: E501
        :type: SSL
        """

        self._ssl = ssl

    @property
    def svc_orch_spec(self):
        """Gets the svc_orch_spec of this PredictorSpec.  # noqa: E501


        :return: The svc_orch_spec of this PredictorSpec.  # noqa: E501
        :rtype: SvcOrchSpec
        """
        return self._svc_orch_spec

    @svc_orch_spec.setter
    def svc_orch_spec(self, svc_orch_spec):
        """Sets the svc_orch_spec of this PredictorSpec.


        :param svc_orch_spec: The svc_orch_spec of this PredictorSpec.  # noqa: E501
        :type: SvcOrchSpec
        """

        self._svc_orch_spec = svc_orch_spec

    @property
    def traffic(self):
        """Gets the traffic of this PredictorSpec.  # noqa: E501


        :return: The traffic of this PredictorSpec.  # noqa: E501
        :rtype: int
        """
        return self._traffic

    @traffic.setter
    def traffic(self, traffic):
        """Sets the traffic of this PredictorSpec.


        :param traffic: The traffic of this PredictorSpec.  # noqa: E501
        :type: int
        """

        self._traffic = traffic

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PredictorSpec, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PredictorSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
