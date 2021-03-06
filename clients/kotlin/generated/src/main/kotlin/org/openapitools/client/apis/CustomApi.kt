/**
* Adobe Experience Manager (AEM) API
* Swagger AEM is an OpenAPI specification for Adobe Experience Manager (AEM) API
*
* OpenAPI spec version: 3.2.0-pre.0
* Contact: opensource@shinesolutions.com
*
* NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
* https://openapi-generator.tech
* Do not edit the class manually.
*/
package org.openapitools.client.apis


import org.openapitools.client.infrastructure.*

class CustomApi(basePath: kotlin.String = "http://localhost") : ApiClient(basePath) {

    /**
    * 
    * 
    * @param tags  (optional)
    * @param combineTagsOr  (optional)
    * @return kotlin.String
    */
    @Suppress("UNCHECKED_CAST")
    fun getAemHealthCheck(tags: kotlin.String, combineTagsOr: kotlin.Boolean) : kotlin.String {
        val localVariableBody: kotlin.Any? = null
        val localVariableQuery: MultiValueMap = mapOf("tags" to listOf("$tags"), "combineTagsOr" to listOf("$combineTagsOr"))
        val localVariableHeaders: kotlin.collections.Map<kotlin.String,kotlin.String> = mapOf()
        val localVariableConfig = RequestConfig(
            RequestMethod.GET,
            "/system/health",
            query = localVariableQuery,
            headers = localVariableHeaders
        )
        val response = request<kotlin.String>(
            localVariableConfig,
            localVariableBody
        )

        return when (response.responseType) {
            ResponseType.Success -> (response as Success<*>).data as kotlin.String
            ResponseType.Informational -> TODO()
            ResponseType.Redirection -> TODO()
            ResponseType.ClientError -> throw ClientException((response as ClientError<*>).body as? String ?: "Client error")
            ResponseType.ServerError -> throw ServerException((response as ServerError<*>).message ?: "Server error")
            else -> throw kotlin.IllegalStateException("Undefined ResponseType.")
        }
    }

    /**
    * 
    * 
    * @param bundlesPeriodignored  (optional)
    * @param bundlesPeriodignoredAtTypeHint  (optional)
    * @return void
    */
    fun postConfigAemHealthCheckServlet(bundlesPeriodignored: kotlin.Array<kotlin.String>, bundlesPeriodignoredAtTypeHint: kotlin.String) : Unit {
        val localVariableBody: kotlin.Any? = null
        val localVariableQuery: MultiValueMap = mapOf("bundles.ignored" to toMultiValue(bundlesPeriodignored.toList(), "multi"), "bundles.ignored@TypeHint" to listOf("$bundlesPeriodignoredAtTypeHint"))
        val localVariableHeaders: kotlin.collections.Map<kotlin.String,kotlin.String> = mapOf()
        val localVariableConfig = RequestConfig(
            RequestMethod.POST,
            "/apps/system/config/com.shinesolutions.healthcheck.hc.impl.ActiveBundleHealthCheck",
            query = localVariableQuery,
            headers = localVariableHeaders
        )
        val response = request<Any?>(
            localVariableConfig,
            localVariableBody
        )

        return when (response.responseType) {
            ResponseType.Success -> Unit
            ResponseType.Informational -> TODO()
            ResponseType.Redirection -> TODO()
            ResponseType.ClientError -> throw ClientException((response as ClientError<*>).body as? String ?: "Client error")
            ResponseType.ServerError -> throw ServerException((response as ServerError<*>).message ?: "Server error")
            else -> throw kotlin.IllegalStateException("Undefined ResponseType.")
        }
    }

    /**
    * 
    * 
    * @param pwdresetPeriodauthorizables  (optional)
    * @param pwdresetPeriodauthorizablesAtTypeHint  (optional)
    * @return void
    */
    fun postConfigAemPasswordReset(pwdresetPeriodauthorizables: kotlin.Array<kotlin.String>, pwdresetPeriodauthorizablesAtTypeHint: kotlin.String) : Unit {
        val localVariableBody: kotlin.Any? = null
        val localVariableQuery: MultiValueMap = mapOf("pwdreset.authorizables" to toMultiValue(pwdresetPeriodauthorizables.toList(), "multi"), "pwdreset.authorizables@TypeHint" to listOf("$pwdresetPeriodauthorizablesAtTypeHint"))
        val localVariableHeaders: kotlin.collections.Map<kotlin.String,kotlin.String> = mapOf()
        val localVariableConfig = RequestConfig(
            RequestMethod.POST,
            "/apps/system/config/com.shinesolutions.aem.passwordreset.Activator",
            query = localVariableQuery,
            headers = localVariableHeaders
        )
        val response = request<Any?>(
            localVariableConfig,
            localVariableBody
        )

        return when (response.responseType) {
            ResponseType.Success -> Unit
            ResponseType.Informational -> TODO()
            ResponseType.Redirection -> TODO()
            ResponseType.ClientError -> throw ClientException((response as ClientError<*>).body as? String ?: "Client error")
            ResponseType.ServerError -> throw ServerException((response as ServerError<*>).message ?: "Server error")
            else -> throw kotlin.IllegalStateException("Undefined ResponseType.")
        }
    }

}
