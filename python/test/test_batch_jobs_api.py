# coding: utf-8

"""
    Seldon Deploy API

    API to interact and manage the lifecycle of your machine learning models deployed through Seldon Deploy.  # noqa: E501

    OpenAPI spec version: v1alpha1
    Contact: hello@seldon.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import seldon_deploy_sdk
from seldon_deploy_sdk.api.batch_jobs_api import BatchJobsApi  # noqa: E501
from seldon_deploy_sdk.rest import ApiException


class TestBatchJobsApi(unittest.TestCase):
    """BatchJobsApi unit test stubs"""

    def setUp(self):
        self.api = seldon_deploy_sdk.api.batch_jobs_api.BatchJobsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_pipeline_batch_job(self):
        """Test case for create_pipeline_batch_job

        """
        pass

    def test_create_seldon_deployment_batch_job(self):
        """Test case for create_seldon_deployment_batch_job

        """
        pass

    def test_get_deployment_batch_job(self):
        """Test case for get_deployment_batch_job

        """
        pass

    def test_get_pipeline_batch_job(self):
        """Test case for get_pipeline_batch_job

        """
        pass

    def test_list_pipeline_batch_jobs(self):
        """Test case for list_pipeline_batch_jobs

        """
        pass

    def test_list_seldon_deployment_batch_jobs(self):
        """Test case for list_seldon_deployment_batch_jobs

        """
        pass


if __name__ == '__main__':
    unittest.main()
