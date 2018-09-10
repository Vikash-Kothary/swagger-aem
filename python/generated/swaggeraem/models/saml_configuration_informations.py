# coding: utf-8

"""
    Adobe Experience Manager (AEM) API

    Swagger AEM is an OpenAPI specification for Adobe Experience Manager (AEM) API

    OpenAPI spec version: 2.2.0
    Contact: opensource@shinesolutions.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SamlConfigurationInformations(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'pid': 'str',
        'title': 'str',
        'description': 'str',
        'bundle_location': 'str',
        'service_location': 'str',
        'properties': 'object'
    }

    attribute_map = {
        'pid': 'pid',
        'title': 'title',
        'description': 'description',
        'bundle_location': 'bundle_location',
        'service_location': 'service_location',
        'properties': 'properties'
    }

    def __init__(self, pid=None, title=None, description=None, bundle_location=None, service_location=None, properties=None):
        """
        SamlConfigurationInformations - a model defined in Swagger
        """

        self._pid = None
        self._title = None
        self._description = None
        self._bundle_location = None
        self._service_location = None
        self._properties = None
        self.discriminator = None

        if pid is not None:
          self.pid = pid
        if title is not None:
          self.title = title
        if description is not None:
          self.description = description
        if bundle_location is not None:
          self.bundle_location = bundle_location
        if service_location is not None:
          self.service_location = service_location
        if properties is not None:
          self.properties = properties

    @property
    def pid(self):
        """
        Gets the pid of this SamlConfigurationInformations.
        Persistent Identity (PID)

        :return: The pid of this SamlConfigurationInformations.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """
        Sets the pid of this SamlConfigurationInformations.
        Persistent Identity (PID)

        :param pid: The pid of this SamlConfigurationInformations.
        :type: str
        """

        self._pid = pid

    @property
    def title(self):
        """
        Gets the title of this SamlConfigurationInformations.
        Title

        :return: The title of this SamlConfigurationInformations.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this SamlConfigurationInformations.
        Title

        :param title: The title of this SamlConfigurationInformations.
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """
        Gets the description of this SamlConfigurationInformations.
        Title

        :return: The description of this SamlConfigurationInformations.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SamlConfigurationInformations.
        Title

        :param description: The description of this SamlConfigurationInformations.
        :type: str
        """

        self._description = description

    @property
    def bundle_location(self):
        """
        Gets the bundle_location of this SamlConfigurationInformations.
        needed for configuration binding

        :return: The bundle_location of this SamlConfigurationInformations.
        :rtype: str
        """
        return self._bundle_location

    @bundle_location.setter
    def bundle_location(self, bundle_location):
        """
        Sets the bundle_location of this SamlConfigurationInformations.
        needed for configuration binding

        :param bundle_location: The bundle_location of this SamlConfigurationInformations.
        :type: str
        """

        self._bundle_location = bundle_location

    @property
    def service_location(self):
        """
        Gets the service_location of this SamlConfigurationInformations.
        needed for configuraiton binding

        :return: The service_location of this SamlConfigurationInformations.
        :rtype: str
        """
        return self._service_location

    @service_location.setter
    def service_location(self, service_location):
        """
        Sets the service_location of this SamlConfigurationInformations.
        needed for configuraiton binding

        :param service_location: The service_location of this SamlConfigurationInformations.
        :type: str
        """

        self._service_location = service_location

    @property
    def properties(self):
        """
        Gets the properties of this SamlConfigurationInformations.

        :return: The properties of this SamlConfigurationInformations.
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this SamlConfigurationInformations.

        :param properties: The properties of this SamlConfigurationInformations.
        :type: object
        """

        self._properties = properties

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, SamlConfigurationInformations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
