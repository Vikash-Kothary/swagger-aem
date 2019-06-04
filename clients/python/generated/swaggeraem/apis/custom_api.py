# coding: utf-8

"""
    Adobe Experience Manager (AEM) API

    Swagger AEM is an OpenAPI specification for Adobe Experience Manager (AEM) API

    OpenAPI spec version: 2.2.0
    Contact: opensource@shinesolutions.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..api_client import ApiClient


class CustomApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_aem_health_check(self, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_aem_health_check(async=True)
        >>> result = thread.get()

        :param async bool
        :param str tags:
        :param bool combine_tags_or:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_aem_health_check_with_http_info(**kwargs)
        else:
            (data) = self.get_aem_health_check_with_http_info(**kwargs)
            return data

    def get_aem_health_check_with_http_info(self, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_aem_health_check_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str tags:
        :param bool combine_tags_or:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tags', 'combine_tags_or']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_aem_health_check" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tags' in params:
            query_params.append(('tags', params['tags']))
        if 'combine_tags_or' in params:
            query_params.append(('combineTagsOr', params['combine_tags_or']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['aemAuth']

        return self.api_client.call_api('/system/health', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='str',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_config_aem_health_check_servlet(self, runmode, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_config_aem_health_check_servlet(runmode, async=True)
        >>> result = thread.get()

        :param async bool
        :param str runmode: (required)
        :param list[str] bundles_ignored:
        :param str bundles_ignored_type_hint:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_config_aem_health_check_servlet_with_http_info(runmode, **kwargs)
        else:
            (data) = self.post_config_aem_health_check_servlet_with_http_info(runmode, **kwargs)
            return data

    def post_config_aem_health_check_servlet_with_http_info(self, runmode, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_config_aem_health_check_servlet_with_http_info(runmode, async=True)
        >>> result = thread.get()

        :param async bool
        :param str runmode: (required)
        :param list[str] bundles_ignored:
        :param str bundles_ignored_type_hint:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['runmode', 'bundles_ignored', 'bundles_ignored_type_hint']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_config_aem_health_check_servlet" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'runmode' is set
        if ('runmode' not in params) or (params['runmode'] is None):
            raise ValueError("Missing the required parameter `runmode` when calling `post_config_aem_health_check_servlet`")


        collection_formats = {}

        path_params = {}
        if 'runmode' in params:
            path_params['runmode'] = params['runmode']

        query_params = []
        if 'bundles_ignored' in params:
            query_params.append(('bundles.ignored', params['bundles_ignored']))
            collection_formats['bundles.ignored'] = 'multi'
        if 'bundles_ignored_type_hint' in params:
            query_params.append(('bundles.ignored@TypeHint', params['bundles_ignored_type_hint']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/plain'])

        # Authentication setting
        auth_settings = ['aemAuth']

        return self.api_client.call_api('/apps/system/config/com.shinesolutions.healthcheck.hc.impl.ActiveBundleHealthCheck', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_config_aem_password_reset(self, runmode, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_config_aem_password_reset(runmode, async=True)
        >>> result = thread.get()

        :param async bool
        :param str runmode: (required)
        :param list[str] pwdreset_authorizables:
        :param str pwdreset_authorizables_type_hint:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_config_aem_password_reset_with_http_info(runmode, **kwargs)
        else:
            (data) = self.post_config_aem_password_reset_with_http_info(runmode, **kwargs)
            return data

    def post_config_aem_password_reset_with_http_info(self, runmode, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_config_aem_password_reset_with_http_info(runmode, async=True)
        >>> result = thread.get()

        :param async bool
        :param str runmode: (required)
        :param list[str] pwdreset_authorizables:
        :param str pwdreset_authorizables_type_hint:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['runmode', 'pwdreset_authorizables', 'pwdreset_authorizables_type_hint']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_config_aem_password_reset" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'runmode' is set
        if ('runmode' not in params) or (params['runmode'] is None):
            raise ValueError("Missing the required parameter `runmode` when calling `post_config_aem_password_reset`")


        collection_formats = {}

        path_params = {}
        if 'runmode' in params:
            path_params['runmode'] = params['runmode']

        query_params = []
        if 'pwdreset_authorizables' in params:
            query_params.append(('pwdreset.authorizables', params['pwdreset_authorizables']))
            collection_formats['pwdreset.authorizables'] = 'multi'
        if 'pwdreset_authorizables_type_hint' in params:
            query_params.append(('pwdreset.authorizables@TypeHint', params['pwdreset_authorizables_type_hint']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/plain'])

        # Authentication setting
        auth_settings = ['aemAuth']

        return self.api_client.call_api('/apps/system/config/com.shinesolutions.aem.passwordreset.Activator', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)