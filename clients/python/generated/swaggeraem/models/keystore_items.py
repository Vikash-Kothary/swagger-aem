# coding: utf-8

"""
    Adobe Experience Manager (AEM) API

    Swagger AEM is an OpenAPI specification for Adobe Experience Manager (AEM) API  # noqa: E501

    The version of the OpenAPI document: 3.4.0
    Contact: opensource@shinesolutions.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from swaggeraem.configuration import Configuration


class KeystoreItems(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'alias': 'str',
        'entry_type': 'str',
        'algorithm': 'str',
        'format': 'str',
        'chain': 'list[KeystoreChainItems]'
    }

    attribute_map = {
        'alias': 'alias',
        'entry_type': 'entryType',
        'algorithm': 'algorithm',
        'format': 'format',
        'chain': 'chain'
    }

    def __init__(self, alias=None, entry_type=None, algorithm=None, format=None, chain=None, local_vars_configuration=None):  # noqa: E501
        """KeystoreItems - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alias = None
        self._entry_type = None
        self._algorithm = None
        self._format = None
        self._chain = None
        self.discriminator = None

        if alias is not None:
            self.alias = alias
        if entry_type is not None:
            self.entry_type = entry_type
        if algorithm is not None:
            self.algorithm = algorithm
        if format is not None:
            self.format = format
        if chain is not None:
            self.chain = chain

    @property
    def alias(self):
        """Gets the alias of this KeystoreItems.  # noqa: E501

        Keystore alias name  # noqa: E501

        :return: The alias of this KeystoreItems.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this KeystoreItems.

        Keystore alias name  # noqa: E501

        :param alias: The alias of this KeystoreItems.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def entry_type(self):
        """Gets the entry_type of this KeystoreItems.  # noqa: E501

        e.g. \"privateKey\"  # noqa: E501

        :return: The entry_type of this KeystoreItems.  # noqa: E501
        :rtype: str
        """
        return self._entry_type

    @entry_type.setter
    def entry_type(self, entry_type):
        """Sets the entry_type of this KeystoreItems.

        e.g. \"privateKey\"  # noqa: E501

        :param entry_type: The entry_type of this KeystoreItems.  # noqa: E501
        :type: str
        """

        self._entry_type = entry_type

    @property
    def algorithm(self):
        """Gets the algorithm of this KeystoreItems.  # noqa: E501

        e.g. \"RSA\"  # noqa: E501

        :return: The algorithm of this KeystoreItems.  # noqa: E501
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this KeystoreItems.

        e.g. \"RSA\"  # noqa: E501

        :param algorithm: The algorithm of this KeystoreItems.  # noqa: E501
        :type: str
        """

        self._algorithm = algorithm

    @property
    def format(self):
        """Gets the format of this KeystoreItems.  # noqa: E501

        e.g. \"PKCS#8\"  # noqa: E501

        :return: The format of this KeystoreItems.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this KeystoreItems.

        e.g. \"PKCS#8\"  # noqa: E501

        :param format: The format of this KeystoreItems.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def chain(self):
        """Gets the chain of this KeystoreItems.  # noqa: E501


        :return: The chain of this KeystoreItems.  # noqa: E501
        :rtype: list[KeystoreChainItems]
        """
        return self._chain

    @chain.setter
    def chain(self, chain):
        """Sets the chain of this KeystoreItems.


        :param chain: The chain of this KeystoreItems.  # noqa: E501
        :type: list[KeystoreChainItems]
        """

        self._chain = chain

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, KeystoreItems):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KeystoreItems):
            return True

        return self.to_dict() != other.to_dict()
