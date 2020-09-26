/**
 * Adobe Experience Manager (AEM) API
 * Swagger AEM is an OpenAPI specification for Adobe Experience Manager (AEM) API
 *
 * The version of the OpenAPI document: 3.4.0
 * Contact: opensource@shinesolutions.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";

/**
* Granite service.
* @module api/GraniteApi
* @version 0.9.0
*/
export default class GraniteApi {

    /**
    * Constructs a new GraniteApi. 
    * @alias module:api/GraniteApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the sslSetup operation.
     * @callback module:api/GraniteApi~sslSetupCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} keystorePassword 
     * @param {String} keystorePasswordConfirm 
     * @param {String} truststorePassword 
     * @param {String} truststorePasswordConfirm 
     * @param {String} httpsHostname 
     * @param {String} httpsPort 
     * @param {Object} opts Optional parameters
     * @param {File} opts.privatekeyFile 
     * @param {File} opts.certificateFile 
     * @param {module:api/GraniteApi~sslSetupCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    sslSetup(keystorePassword, keystorePasswordConfirm, truststorePassword, truststorePasswordConfirm, httpsHostname, httpsPort, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'keystorePassword' is set
      if (keystorePassword === undefined || keystorePassword === null) {
        throw new Error("Missing the required parameter 'keystorePassword' when calling sslSetup");
      }
      // verify the required parameter 'keystorePasswordConfirm' is set
      if (keystorePasswordConfirm === undefined || keystorePasswordConfirm === null) {
        throw new Error("Missing the required parameter 'keystorePasswordConfirm' when calling sslSetup");
      }
      // verify the required parameter 'truststorePassword' is set
      if (truststorePassword === undefined || truststorePassword === null) {
        throw new Error("Missing the required parameter 'truststorePassword' when calling sslSetup");
      }
      // verify the required parameter 'truststorePasswordConfirm' is set
      if (truststorePasswordConfirm === undefined || truststorePasswordConfirm === null) {
        throw new Error("Missing the required parameter 'truststorePasswordConfirm' when calling sslSetup");
      }
      // verify the required parameter 'httpsHostname' is set
      if (httpsHostname === undefined || httpsHostname === null) {
        throw new Error("Missing the required parameter 'httpsHostname' when calling sslSetup");
      }
      // verify the required parameter 'httpsPort' is set
      if (httpsPort === undefined || httpsPort === null) {
        throw new Error("Missing the required parameter 'httpsPort' when calling sslSetup");
      }

      let pathParams = {
      };
      let queryParams = {
        'keystorePassword': keystorePassword,
        'keystorePasswordConfirm': keystorePasswordConfirm,
        'truststorePassword': truststorePassword,
        'truststorePasswordConfirm': truststorePasswordConfirm,
        'httpsHostname': httpsHostname,
        'httpsPort': httpsPort
      };
      let headerParams = {
      };
      let formParams = {
        'privatekeyFile': opts['privatekeyFile'],
        'certificateFile': opts['certificateFile']
      };

      let authNames = ['aemAuth'];
      let contentTypes = ['multipart/form-data'];
      let accepts = ['text/plain'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/libs/granite/security/post/sslSetup.html', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
