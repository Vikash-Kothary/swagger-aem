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


class GraniteApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def ssl_setup(self, keystore_password, keystore_password_confirm, truststore_password, truststore_password_confirm, https_hostname, https_port, **kwargs):  # noqa: E501
        """ssl_setup  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ssl_setup(keystore_password, keystore_password_confirm, truststore_password, truststore_password_confirm, https_hostname, https_port, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str keystore_password: (required)
        :param str keystore_password_confirm: (required)
        :param str truststore_password: (required)
        :param str truststore_password_confirm: (required)
        :param str https_hostname: (required)
        :param str https_port: (required)
        :param file privatekey_file:
        :param file certificate_file:
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
        return self.ssl_setup_with_http_info(keystore_password, keystore_password_confirm, truststore_password, truststore_password_confirm, https_hostname, https_port, **kwargs)  # noqa: E501

    def ssl_setup_with_http_info(self, keystore_password, keystore_password_confirm, truststore_password, truststore_password_confirm, https_hostname, https_port, **kwargs):  # noqa: E501
        """ssl_setup  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ssl_setup_with_http_info(keystore_password, keystore_password_confirm, truststore_password, truststore_password_confirm, https_hostname, https_port, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str keystore_password: (required)
        :param str keystore_password_confirm: (required)
        :param str truststore_password: (required)
        :param str truststore_password_confirm: (required)
        :param str https_hostname: (required)
        :param str https_port: (required)
        :param file privatekey_file:
        :param file certificate_file:
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
            'keystore_password',
            'keystore_password_confirm',
            'truststore_password',
            'truststore_password_confirm',
            'https_hostname',
            'https_port',
            'privatekey_file',
            'certificate_file'
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
                    " to method ssl_setup" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'keystore_password' is set
        if self.api_client.client_side_validation and ('keystore_password' not in local_var_params or  # noqa: E501
                                                        local_var_params['keystore_password'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `keystore_password` when calling `ssl_setup`")  # noqa: E501
        # verify the required parameter 'keystore_password_confirm' is set
        if self.api_client.client_side_validation and ('keystore_password_confirm' not in local_var_params or  # noqa: E501
                                                        local_var_params['keystore_password_confirm'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `keystore_password_confirm` when calling `ssl_setup`")  # noqa: E501
        # verify the required parameter 'truststore_password' is set
        if self.api_client.client_side_validation and ('truststore_password' not in local_var_params or  # noqa: E501
                                                        local_var_params['truststore_password'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `truststore_password` when calling `ssl_setup`")  # noqa: E501
        # verify the required parameter 'truststore_password_confirm' is set
        if self.api_client.client_side_validation and ('truststore_password_confirm' not in local_var_params or  # noqa: E501
                                                        local_var_params['truststore_password_confirm'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `truststore_password_confirm` when calling `ssl_setup`")  # noqa: E501
        # verify the required parameter 'https_hostname' is set
        if self.api_client.client_side_validation and ('https_hostname' not in local_var_params or  # noqa: E501
                                                        local_var_params['https_hostname'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `https_hostname` when calling `ssl_setup`")  # noqa: E501
        # verify the required parameter 'https_port' is set
        if self.api_client.client_side_validation and ('https_port' not in local_var_params or  # noqa: E501
                                                        local_var_params['https_port'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `https_port` when calling `ssl_setup`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keystore_password' in local_var_params and local_var_params['keystore_password'] is not None:  # noqa: E501
            query_params.append(('keystorePassword', local_var_params['keystore_password']))  # noqa: E501
        if 'keystore_password_confirm' in local_var_params and local_var_params['keystore_password_confirm'] is not None:  # noqa: E501
            query_params.append(('keystorePasswordConfirm', local_var_params['keystore_password_confirm']))  # noqa: E501
        if 'truststore_password' in local_var_params and local_var_params['truststore_password'] is not None:  # noqa: E501
            query_params.append(('truststorePassword', local_var_params['truststore_password']))  # noqa: E501
        if 'truststore_password_confirm' in local_var_params and local_var_params['truststore_password_confirm'] is not None:  # noqa: E501
            query_params.append(('truststorePasswordConfirm', local_var_params['truststore_password_confirm']))  # noqa: E501
        if 'https_hostname' in local_var_params and local_var_params['https_hostname'] is not None:  # noqa: E501
            query_params.append(('httpsHostname', local_var_params['https_hostname']))  # noqa: E501
        if 'https_port' in local_var_params and local_var_params['https_port'] is not None:  # noqa: E501
            query_params.append(('httpsPort', local_var_params['https_port']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'privatekey_file' in local_var_params:
            local_var_files['privatekeyFile'] = local_var_params['privatekey_file']  # noqa: E501
        if 'certificate_file' in local_var_params:
            local_var_files['certificateFile'] = local_var_params['certificate_file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['aemAuth']  # noqa: E501

        return self.api_client.call_api(
            '/libs/granite/security/post/sslSetup.html', 'POST',
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
