# coding: utf-8

"""
    Adobe Experience Manager (AEM) API

    Swagger AEM is an OpenAPI specification for Adobe Experience Manager (AEM) API  # noqa: E501

    The version of the OpenAPI document: 3.4.0
    Contact: opensource@shinesolutions.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swaggeraem.api_client import ApiClient
from swaggeraem.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class CrxApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_crxde_status(self, **kwargs):  # noqa: E501
        """get_crxde_status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_crxde_status(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_crxde_status_with_http_info(**kwargs)  # noqa: E501

    def get_crxde_status_with_http_info(self, **kwargs):  # noqa: E501
        """get_crxde_status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_crxde_status_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_crxde_status" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['plain/text'])  # noqa: E501

        # Authentication setting
        auth_settings = ['aemAuth']  # noqa: E501

        return self.api_client.call_api(
            '/crx/server/crx.default/jcr:root/.1.json', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_install_status(self, **kwargs):  # noqa: E501
        """get_install_status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_install_status(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InstallStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_install_status_with_http_info(**kwargs)  # noqa: E501

    def get_install_status_with_http_info(self, **kwargs):  # noqa: E501
        """get_install_status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_install_status_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InstallStatus, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_install_status" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['aemAuth']  # noqa: E501

        return self.api_client.call_api(
            '/crx/packmgr/installstatus.jsp', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InstallStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_package_manager_servlet(self, **kwargs):  # noqa: E501
        """get_package_manager_servlet  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_package_manager_servlet(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_package_manager_servlet_with_http_info(**kwargs)  # noqa: E501

    def get_package_manager_servlet_with_http_info(self, **kwargs):  # noqa: E501
        """get_package_manager_servlet  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_package_manager_servlet_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_package_manager_servlet" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/html'])  # noqa: E501

        # Authentication setting
        auth_settings = ['aemAuth']  # noqa: E501

        return self.api_client.call_api(
            '/crx/packmgr/service/script.html', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_package_service(self, cmd, **kwargs):  # noqa: E501
        """post_package_service  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_package_service(cmd, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str cmd: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.post_package_service_with_http_info(cmd, **kwargs)  # noqa: E501

    def post_package_service_with_http_info(self, cmd, **kwargs):  # noqa: E501
        """post_package_service  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_package_service_with_http_info(cmd, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str cmd: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'cmd'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_package_service" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'cmd' is set
        if self.api_client.client_side_validation and ('cmd' not in local_var_params or  # noqa: E501
                                                        local_var_params['cmd'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cmd` when calling `post_package_service`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cmd' in local_var_params and local_var_params['cmd'] is not None:  # noqa: E501
            query_params.append(('cmd', local_var_params['cmd']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['aemAuth']  # noqa: E501

        return self.api_client.call_api(
            '/crx/packmgr/service.jsp', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_package_service_json(self, path, cmd, **kwargs):  # noqa: E501
        """post_package_service_json  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_package_service_json(path, cmd, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str path: (required)
        :param str cmd: (required)
        :param str group_name:
        :param str package_name:
        :param str package_version:
        :param str charset_:
        :param bool force:
        :param bool recursive:
        :param file package:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.post_package_service_json_with_http_info(path, cmd, **kwargs)  # noqa: E501

    def post_package_service_json_with_http_info(self, path, cmd, **kwargs):  # noqa: E501
        """post_package_service_json  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_package_service_json_with_http_info(path, cmd, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str path: (required)
        :param str cmd: (required)
        :param str group_name:
        :param str package_name:
        :param str package_version:
        :param str charset_:
        :param bool force:
        :param bool recursive:
        :param file package:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'path',
            'cmd',
            'group_name',
            'package_name',
            'package_version',
            'charset_',
            'force',
            'recursive',
            'package'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_package_service_json" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'path' is set
        if self.api_client.client_side_validation and ('path' not in local_var_params or  # noqa: E501
                                                        local_var_params['path'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `path` when calling `post_package_service_json`")  # noqa: E501
        # verify the required parameter 'cmd' is set
        if self.api_client.client_side_validation and ('cmd' not in local_var_params or  # noqa: E501
                                                        local_var_params['cmd'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cmd` when calling `post_package_service_json`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'path' in local_var_params:
            path_params['path'] = local_var_params['path']  # noqa: E501

        query_params = []
        if 'cmd' in local_var_params and local_var_params['cmd'] is not None:  # noqa: E501
            query_params.append(('cmd', local_var_params['cmd']))  # noqa: E501
        if 'group_name' in local_var_params and local_var_params['group_name'] is not None:  # noqa: E501
            query_params.append(('groupName', local_var_params['group_name']))  # noqa: E501
        if 'package_name' in local_var_params and local_var_params['package_name'] is not None:  # noqa: E501
            query_params.append(('packageName', local_var_params['package_name']))  # noqa: E501
        if 'package_version' in local_var_params and local_var_params['package_version'] is not None:  # noqa: E501
            query_params.append(('packageVersion', local_var_params['package_version']))  # noqa: E501
        if 'charset_' in local_var_params and local_var_params['charset_'] is not None:  # noqa: E501
            query_params.append(('_charset_', local_var_params['charset_']))  # noqa: E501
        if 'force' in local_var_params and local_var_params['force'] is not None:  # noqa: E501
            query_params.append(('force', local_var_params['force']))  # noqa: E501
        if 'recursive' in local_var_params and local_var_params['recursive'] is not None:  # noqa: E501
            query_params.append(('recursive', local_var_params['recursive']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'package' in local_var_params:
            local_var_files['package'] = local_var_params['package']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['aemAuth']  # noqa: E501

        return self.api_client.call_api(
            '/crx/packmgr/service/.json/{path}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_package_update(self, group_name, package_name, version, path, **kwargs):  # noqa: E501
        """post_package_update  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_package_update(group_name, package_name, version, path, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str group_name: (required)
        :param str package_name: (required)
        :param str version: (required)
        :param str path: (required)
        :param str filter:
        :param str charset_:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.post_package_update_with_http_info(group_name, package_name, version, path, **kwargs)  # noqa: E501

    def post_package_update_with_http_info(self, group_name, package_name, version, path, **kwargs):  # noqa: E501
        """post_package_update  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_package_update_with_http_info(group_name, package_name, version, path, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str group_name: (required)
        :param str package_name: (required)
        :param str version: (required)
        :param str path: (required)
        :param str filter:
        :param str charset_:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'group_name',
            'package_name',
            'version',
            'path',
            'filter',
            'charset_'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_package_update" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'group_name' is set
        if self.api_client.client_side_validation and ('group_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_name` when calling `post_package_update`")  # noqa: E501
        # verify the required parameter 'package_name' is set
        if self.api_client.client_side_validation and ('package_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['package_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `package_name` when calling `post_package_update`")  # noqa: E501
        # verify the required parameter 'version' is set
        if self.api_client.client_side_validation and ('version' not in local_var_params or  # noqa: E501
                                                        local_var_params['version'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `version` when calling `post_package_update`")  # noqa: E501
        # verify the required parameter 'path' is set
        if self.api_client.client_side_validation and ('path' not in local_var_params or  # noqa: E501
                                                        local_var_params['path'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `path` when calling `post_package_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_name' in local_var_params and local_var_params['group_name'] is not None:  # noqa: E501
            query_params.append(('groupName', local_var_params['group_name']))  # noqa: E501
        if 'package_name' in local_var_params and local_var_params['package_name'] is not None:  # noqa: E501
            query_params.append(('packageName', local_var_params['package_name']))  # noqa: E501
        if 'version' in local_var_params and local_var_params['version'] is not None:  # noqa: E501
            query_params.append(('version', local_var_params['version']))  # noqa: E501
        if 'path' in local_var_params and local_var_params['path'] is not None:  # noqa: E501
            query_params.append(('path', local_var_params['path']))  # noqa: E501
        if 'filter' in local_var_params and local_var_params['filter'] is not None:  # noqa: E501
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501
        if 'charset_' in local_var_params and local_var_params['charset_'] is not None:  # noqa: E501
            query_params.append(('_charset_', local_var_params['charset_']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['aemAuth']  # noqa: E501

        return self.api_client.call_api(
            '/crx/packmgr/update.jsp', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_set_password(self, old, plain, verify, **kwargs):  # noqa: E501
        """post_set_password  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_set_password(old, plain, verify, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str old: (required)
        :param str plain: (required)
        :param str verify: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.post_set_password_with_http_info(old, plain, verify, **kwargs)  # noqa: E501

    def post_set_password_with_http_info(self, old, plain, verify, **kwargs):  # noqa: E501
        """post_set_password  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_set_password_with_http_info(old, plain, verify, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str old: (required)
        :param str plain: (required)
        :param str verify: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'old',
            'plain',
            'verify'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_set_password" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'old' is set
        if self.api_client.client_side_validation and ('old' not in local_var_params or  # noqa: E501
                                                        local_var_params['old'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `old` when calling `post_set_password`")  # noqa: E501
        # verify the required parameter 'plain' is set
        if self.api_client.client_side_validation and ('plain' not in local_var_params or  # noqa: E501
                                                        local_var_params['plain'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `plain` when calling `post_set_password`")  # noqa: E501
        # verify the required parameter 'verify' is set
        if self.api_client.client_side_validation and ('verify' not in local_var_params or  # noqa: E501
                                                        local_var_params['verify'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `verify` when calling `post_set_password`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'old' in local_var_params and local_var_params['old'] is not None:  # noqa: E501
            query_params.append(('old', local_var_params['old']))  # noqa: E501
        if 'plain' in local_var_params and local_var_params['plain'] is not None:  # noqa: E501
            query_params.append(('plain', local_var_params['plain']))  # noqa: E501
        if 'verify' in local_var_params and local_var_params['verify'] is not None:  # noqa: E501
            query_params.append(('verify', local_var_params['verify']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['aemAuth']  # noqa: E501

        return self.api_client.call_api(
            '/crx/explorer/ui/setpassword.jsp', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
