"""
    Adobe Experience Manager (AEM) API

    Swagger AEM is an OpenAPI specification for Adobe Experience Manager (AEM) API  # noqa: E501

    The version of the OpenAPI document: 3.5.0-pre.0
    Contact: opensource@shinesolutions.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "swaggeraem"
VERSION = "1.2.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
  "nulltype",
]

setup(
    name=NAME,
    version=VERSION,
    description="Adobe Experience Manager (AEM) API",
    author="Shine Solutions",
    author_email="opensource@shinesolutions.com",
    url="https://github.com/shinesolutions/swagger-aem/tree/master/python",
    keywords=["OpenAPI", "OpenAPI-Generator", "Adobe Experience Manager (AEM) API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    Swagger AEM is an OpenAPI specification for Adobe Experience Manager (AEM) API  # noqa: E501
    """
)
