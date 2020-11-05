# coding: utf-8

"""
    Seldon-Deploy API.

    Documentation of Seldon-Deploy API.  # noqa: E501

    OpenAPI spec version: v1alpha1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import seldon_deploy_client
from seldon_deploy_client.api.outlier_detector_api import OutlierDetectorApi  # noqa: E501
from seldon_deploy_client.rest import ApiException


class TestOutlierDetectorApi(unittest.TestCase):
    """OutlierDetectorApi unit test stubs"""

    def setUp(self):
        self.api = seldon_deploy_client.api.outlier_detector_api.OutlierDetectorApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_outlier_detector_inference_service(self):
        """Test case for create_outlier_detector_inference_service

        """
        pass

    def test_create_outlier_detector_seldon_deployment(self):
        """Test case for create_outlier_detector_seldon_deployment

        """
        pass

    def test_delete_outlier_detector_inference_service(self):
        """Test case for delete_outlier_detector_inference_service

        """
        pass

    def test_delete_outlier_detector_seldon_deployment(self):
        """Test case for delete_outlier_detector_seldon_deployment

        """
        pass

    def test_read_outlier_detector_inference_service(self):
        """Test case for read_outlier_detector_inference_service

        """
        pass

    def test_read_outlier_detector_seldon_deployment(self):
        """Test case for read_outlier_detector_seldon_deployment

        """
        pass


if __name__ == '__main__':
    unittest.main()
