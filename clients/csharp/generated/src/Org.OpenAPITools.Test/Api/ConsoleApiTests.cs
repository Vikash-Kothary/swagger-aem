/* 
 * Adobe Experience Manager (AEM) API
 *
 * Swagger AEM is an OpenAPI specification for Adobe Experience Manager (AEM) API
 *
 * OpenAPI spec version: 3.2.0-pre.0
 * Contact: opensource@shinesolutions.com
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.IO;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Reflection;
using RestSharp;
using NUnit.Framework;

using Org.OpenAPITools.Client;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Model;

namespace Org.OpenAPITools.Test
{
    /// <summary>
    ///  Class for testing ConsoleApi
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by OpenAPI Generator (https://openapi-generator.tech).
    /// Please update the test case below to test the API endpoint.
    /// </remarks>
    [TestFixture]
    public class ConsoleApiTests
    {
        private ConsoleApi instance;

        /// <summary>
        /// Setup before each unit test
        /// </summary>
        [SetUp]
        public void Init()
        {
            instance = new ConsoleApi();
        }

        /// <summary>
        /// Clean up after each unit test
        /// </summary>
        [TearDown]
        public void Cleanup()
        {

        }

        /// <summary>
        /// Test an instance of ConsoleApi
        /// </summary>
        [Test]
        public void InstanceTest()
        {
            // TODO uncomment below to test 'IsInstanceOfType' ConsoleApi
            //Assert.IsInstanceOfType(typeof(ConsoleApi), instance, "instance is a ConsoleApi");
        }

        
        /// <summary>
        /// Test GetAemProductInfo
        /// </summary>
        [Test]
        public void GetAemProductInfoTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //var response = instance.GetAemProductInfo();
            //Assert.IsInstanceOf<List<string>> (response, "response is List<string>");
        }
        
        /// <summary>
        /// Test GetConfigMgr
        /// </summary>
        [Test]
        public void GetConfigMgrTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //var response = instance.GetConfigMgr();
            //Assert.IsInstanceOf<string> (response, "response is string");
        }
        
        /// <summary>
        /// Test PostBundle
        /// </summary>
        [Test]
        public void PostBundleTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string name = null;
            //string action = null;
            //instance.PostBundle(name, action);
            
        }
        
        /// <summary>
        /// Test PostJmxRepository
        /// </summary>
        [Test]
        public void PostJmxRepositoryTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string action = null;
            //instance.PostJmxRepository(action);
            
        }
        
        /// <summary>
        /// Test PostSamlConfiguration
        /// </summary>
        [Test]
        public void PostSamlConfigurationTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //bool? post = null;
            //bool? apply = null;
            //bool? delete = null;
            //string action = null;
            //string location = null;
            //List<string> path = null;
            //int? serviceRanking = null;
            //string idpUrl = null;
            //string idpCertAlias = null;
            //bool? idpHttpRedirect = null;
            //string serviceProviderEntityId = null;
            //string assertionConsumerServiceURL = null;
            //string spPrivateKeyAlias = null;
            //string keyStorePassword = null;
            //string defaultRedirectUrl = null;
            //string userIDAttribute = null;
            //bool? useEncryption = null;
            //bool? createUser = null;
            //bool? addGroupMemberships = null;
            //string groupMembershipAttribute = null;
            //List<string> defaultGroups = null;
            //string nameIdFormat = null;
            //List<string> synchronizeAttributes = null;
            //bool? handleLogout = null;
            //string logoutUrl = null;
            //int? clockTolerance = null;
            //string digestMethod = null;
            //string signatureMethod = null;
            //string userIntermediatePath = null;
            //List<string> propertylist = null;
            //var response = instance.PostSamlConfiguration(post, apply, delete, action, location, path, serviceRanking, idpUrl, idpCertAlias, idpHttpRedirect, serviceProviderEntityId, assertionConsumerServiceURL, spPrivateKeyAlias, keyStorePassword, defaultRedirectUrl, userIDAttribute, useEncryption, createUser, addGroupMemberships, groupMembershipAttribute, defaultGroups, nameIdFormat, synchronizeAttributes, handleLogout, logoutUrl, clockTolerance, digestMethod, signatureMethod, userIntermediatePath, propertylist);
            //Assert.IsInstanceOf<SamlConfigurationInfo> (response, "response is SamlConfigurationInfo");
        }
        
    }

}