from __future__ import absolute_import

# flake8: noqa

# import apis into api package
from seldon_deploy_client.api.drift_detector_api import DriftDetectorApi
from seldon_deploy_client.api.environment_api import EnvironmentApi
from seldon_deploy_client.api.explainer_api import ExplainerApi
from seldon_deploy_client.api.git_api import GitApi
from seldon_deploy_client.api.gitops_api import GitopsApi
from seldon_deploy_client.api.inference_services_api import InferenceServicesApi
from seldon_deploy_client.api.jobs_api import JobsApi
from seldon_deploy_client.api.loadtest_api import LoadtestApi
from seldon_deploy_client.api.logger_api import LoggerApi
from seldon_deploy_client.api.metrics_server_api import MetricsServerApi
from seldon_deploy_client.api.monitor_api import MonitorApi
from seldon_deploy_client.api.outlier_detector_api import OutlierDetectorApi
from seldon_deploy_client.api.predict_api import PredictApi
from seldon_deploy_client.api.requests_api import RequestsApi
from seldon_deploy_client.api.resources_api import ResourcesApi
from seldon_deploy_client.api.seldon_deployments_api import SeldonDeploymentsApi
from seldon_deploy_client.api.validate_api import ValidateApi
