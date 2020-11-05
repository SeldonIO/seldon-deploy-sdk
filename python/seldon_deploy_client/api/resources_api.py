# coding: utf-8

"""
    Seldon-Deploy API.

    Documentation of Seldon-Deploy API.  # noqa: E501

    OpenAPI spec version: v1alpha1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from seldon_deploy_client.api_client import ApiClient


class ResourcesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_inference_service_predictor_resources(self, name, namespace, predictor_name, **kwargs):  # noqa: E501
        """list_inference_service_predictor_resources  # noqa: E501

        list objects of kind resource for Inference Service predictor  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_inference_service_predictor_resources(name, namespace, predictor_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name identifies a resource (required)
        :param str namespace: Namespace provides a logical grouping of resources (required)
        :param str predictor_name: Predictor Name identifies a predictor resource (required)
        :param str component: Component differentiates between types of model (e.g. predictor, explainer... etc)
        :param str endpoint: Endpoint differentiates between versions of model (e.g. default, canary... etc)
        :return: list[Component]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_inference_service_predictor_resources_with_http_info(name, namespace, predictor_name, **kwargs)  # noqa: E501
        else:
            (data) = self.list_inference_service_predictor_resources_with_http_info(name, namespace, predictor_name, **kwargs)  # noqa: E501
            return data

    def list_inference_service_predictor_resources_with_http_info(self, name, namespace, predictor_name, **kwargs):  # noqa: E501
        """list_inference_service_predictor_resources  # noqa: E501

        list objects of kind resource for Inference Service predictor  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_inference_service_predictor_resources_with_http_info(name, namespace, predictor_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name identifies a resource (required)
        :param str namespace: Namespace provides a logical grouping of resources (required)
        :param str predictor_name: Predictor Name identifies a predictor resource (required)
        :param str component: Component differentiates between types of model (e.g. predictor, explainer... etc)
        :param str endpoint: Endpoint differentiates between versions of model (e.g. default, canary... etc)
        :return: list[Component]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'namespace', 'predictor_name', 'component', 'endpoint']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_inference_service_predictor_resources" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `list_inference_service_predictor_resources`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `list_inference_service_predictor_resources`")  # noqa: E501
        # verify the required parameter 'predictor_name' is set
        if ('predictor_name' not in params or
                params['predictor_name'] is None):
            raise ValueError("Missing the required parameter `predictor_name` when calling `list_inference_service_predictor_resources`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501
        if 'predictor_name' in params:
            path_params['predictorName'] = params['predictor_name']  # noqa: E501

        query_params = []
        if 'component' in params:
            query_params.append(('component', params['component']))  # noqa: E501
        if 'endpoint' in params:
            query_params.append(('endpoint', params['endpoint']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/namespaces/{namespace}/inferenceservices/{name}/predictor/{predictorName}/resources', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Component]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_inference_service_resources(self, name, namespace, **kwargs):  # noqa: E501
        """list_inference_service_resources  # noqa: E501

        list objects of kind resource for Inference Service  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_inference_service_resources(name, namespace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name identifies a resource (required)
        :param str namespace: Namespace provides a logical grouping of resources (required)
        :param str component: Component differentiates between types of model (e.g. predictor, explainer... etc)
        :param str endpoint: Endpoint differentiates between versions of model (e.g. default, canary... etc)
        :return: list[Component]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_inference_service_resources_with_http_info(name, namespace, **kwargs)  # noqa: E501
        else:
            (data) = self.list_inference_service_resources_with_http_info(name, namespace, **kwargs)  # noqa: E501
            return data

    def list_inference_service_resources_with_http_info(self, name, namespace, **kwargs):  # noqa: E501
        """list_inference_service_resources  # noqa: E501

        list objects of kind resource for Inference Service  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_inference_service_resources_with_http_info(name, namespace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name identifies a resource (required)
        :param str namespace: Namespace provides a logical grouping of resources (required)
        :param str component: Component differentiates between types of model (e.g. predictor, explainer... etc)
        :param str endpoint: Endpoint differentiates between versions of model (e.g. default, canary... etc)
        :return: list[Component]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'namespace', 'component', 'endpoint']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_inference_service_resources" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `list_inference_service_resources`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `list_inference_service_resources`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501

        query_params = []
        if 'component' in params:
            query_params.append(('component', params['component']))  # noqa: E501
        if 'endpoint' in params:
            query_params.append(('endpoint', params['endpoint']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/namespaces/{namespace}/inferenceservices/{name}/resources', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Component]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_seldon_deployment_predictor_resources(self, name, namespace, predictor_name, **kwargs):  # noqa: E501
        """list_seldon_deployment_predictor_resources  # noqa: E501

        list objects of kind resource for Seldon Deployment predictor  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_seldon_deployment_predictor_resources(name, namespace, predictor_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name identifies a resource (required)
        :param str namespace: Namespace provides a logical grouping of resources (required)
        :param str predictor_name: Predictor Name identifies a predictor resource (required)
        :param str component: Component differentiates between types of model (e.g. predictor, explainer... etc)
        :param str endpoint: Endpoint differentiates between versions of model (e.g. default, canary... etc)
        :return: list[Component]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_seldon_deployment_predictor_resources_with_http_info(name, namespace, predictor_name, **kwargs)  # noqa: E501
        else:
            (data) = self.list_seldon_deployment_predictor_resources_with_http_info(name, namespace, predictor_name, **kwargs)  # noqa: E501
            return data

    def list_seldon_deployment_predictor_resources_with_http_info(self, name, namespace, predictor_name, **kwargs):  # noqa: E501
        """list_seldon_deployment_predictor_resources  # noqa: E501

        list objects of kind resource for Seldon Deployment predictor  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_seldon_deployment_predictor_resources_with_http_info(name, namespace, predictor_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name identifies a resource (required)
        :param str namespace: Namespace provides a logical grouping of resources (required)
        :param str predictor_name: Predictor Name identifies a predictor resource (required)
        :param str component: Component differentiates between types of model (e.g. predictor, explainer... etc)
        :param str endpoint: Endpoint differentiates between versions of model (e.g. default, canary... etc)
        :return: list[Component]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'namespace', 'predictor_name', 'component', 'endpoint']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_seldon_deployment_predictor_resources" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `list_seldon_deployment_predictor_resources`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `list_seldon_deployment_predictor_resources`")  # noqa: E501
        # verify the required parameter 'predictor_name' is set
        if ('predictor_name' not in params or
                params['predictor_name'] is None):
            raise ValueError("Missing the required parameter `predictor_name` when calling `list_seldon_deployment_predictor_resources`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501
        if 'predictor_name' in params:
            path_params['predictorName'] = params['predictor_name']  # noqa: E501

        query_params = []
        if 'component' in params:
            query_params.append(('component', params['component']))  # noqa: E501
        if 'endpoint' in params:
            query_params.append(('endpoint', params['endpoint']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/namespaces/{namespace}/seldondeployments/{name}/predictor/{predictorName}/resources', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Component]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_seldon_deployment_resources(self, name, namespace, **kwargs):  # noqa: E501
        """list_seldon_deployment_resources  # noqa: E501

        list objects of kind resource for Seldon Deployment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_seldon_deployment_resources(name, namespace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name identifies a resource (required)
        :param str namespace: Namespace provides a logical grouping of resources (required)
        :param str component: Component differentiates between types of model (e.g. predictor, explainer... etc)
        :param str endpoint: Endpoint differentiates between versions of model (e.g. default, canary... etc)
        :return: list[Component]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_seldon_deployment_resources_with_http_info(name, namespace, **kwargs)  # noqa: E501
        else:
            (data) = self.list_seldon_deployment_resources_with_http_info(name, namespace, **kwargs)  # noqa: E501
            return data

    def list_seldon_deployment_resources_with_http_info(self, name, namespace, **kwargs):  # noqa: E501
        """list_seldon_deployment_resources  # noqa: E501

        list objects of kind resource for Seldon Deployment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_seldon_deployment_resources_with_http_info(name, namespace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name identifies a resource (required)
        :param str namespace: Namespace provides a logical grouping of resources (required)
        :param str component: Component differentiates between types of model (e.g. predictor, explainer... etc)
        :param str endpoint: Endpoint differentiates between versions of model (e.g. default, canary... etc)
        :return: list[Component]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'namespace', 'component', 'endpoint']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_seldon_deployment_resources" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `list_seldon_deployment_resources`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `list_seldon_deployment_resources`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501

        query_params = []
        if 'component' in params:
            query_params.append(('component', params['component']))  # noqa: E501
        if 'endpoint' in params:
            query_params.append(('endpoint', params['endpoint']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/namespaces/{namespace}/seldondeployments/{name}/resources', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Component]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
