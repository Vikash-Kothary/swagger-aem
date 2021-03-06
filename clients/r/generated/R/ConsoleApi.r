# Adobe Experience Manager (AEM) API
#
# Swagger AEM is an OpenAPI specification for Adobe Experience Manager (AEM) API
#
# OpenAPI spec version: 3.2.0-pre.0
# Contact: opensource@shinesolutions.com
# Generated by: https://openapi-generator.tech

#' @title Console operations
#' @description openapi.Console
#'
#' @field path Stores url path of the request.
#' @field apiClient Handles the client-server communication.
#' @field userAgent Set the user agent of the request.
#'
#' @importFrom R6 R6Class
#'
#' @section Methods:
#' \describe{
#'
#' get_aem_product_info 
#'
#'
#' get_config_mgr 
#'
#'
#' post_bundle 
#'
#'
#' post_jmx_repository 
#'
#'
#' post_saml_configuration 
#'
#' }
#'
#' @export
ConsoleApi <- R6::R6Class(
  'ConsoleApi',
  public = list(
    userAgent = "OpenAPI-Generator/1.0.0/r",
    apiClient = NULL,
    initialize = function(apiClient){
      if (!missing(apiClient)) {
        self$apiClient <- apiClient
      }
      else {
        self$apiClient <- ApiClient$new()
      }
    },
    get_aem_product_info = function(...){
      args <- list(...)
      queryParams <- list()
      headerParams <- character()

      urlPath <- "/system/console/status-productinfo.json"
      resp <- self$apiClient$callApi(url = paste0(self$apiClient$basePath, urlPath),
                                 method = "GET",
                                 queryParams = queryParams,
                                 headerParams = headerParams,
                                 body = body,
                                 ...)
      
      if (httr::status_code(resp) >= 200 && httr::status_code(resp) <= 299) {
        returnObject <- Character$new()
        result <- returnObject$fromJSON(httr::content(resp, "text", encoding = "UTF-8"))
        Response$new(returnObject, resp)
      } else if (httr::status_code(resp) >= 400 && httr::status_code(resp) <= 499) {
        Response$new("API client error", resp)
      } else if (httr::status_code(resp) >= 500 && httr::status_code(resp) <= 599) {
        Response$new("API server error", resp)
      }

    },
    get_config_mgr = function(...){
      args <- list(...)
      queryParams <- list()
      headerParams <- character()

      urlPath <- "/system/console/configMgr"
      resp <- self$apiClient$callApi(url = paste0(self$apiClient$basePath, urlPath),
                                 method = "GET",
                                 queryParams = queryParams,
                                 headerParams = headerParams,
                                 body = body,
                                 ...)
      
      if (httr::status_code(resp) >= 200 && httr::status_code(resp) <= 299) {
        returnObject <- Character$new()
        result <- returnObject$fromJSON(httr::content(resp, "text", encoding = "UTF-8"))
        Response$new(returnObject, resp)
      } else if (httr::status_code(resp) >= 400 && httr::status_code(resp) <= 499) {
        Response$new("API client error", resp)
      } else if (httr::status_code(resp) >= 500 && httr::status_code(resp) <= 599) {
        Response$new("API server error", resp)
      }

    },
    post_bundle = function(name, action, ...){
      args <- list(...)
      queryParams <- list()
      headerParams <- character()

      if (!missing(`action`)) {
        queryParams['action'] <- action
      }

      urlPath <- "/system/console/bundles/{name}"
      if (!missing(`name`)) {
        urlPath <- gsub(paste0("\\{", "name", "\\}"), `name`, urlPath)
      }

      resp <- self$apiClient$callApi(url = paste0(self$apiClient$basePath, urlPath),
                                 method = "POST",
                                 queryParams = queryParams,
                                 headerParams = headerParams,
                                 body = body,
                                 ...)
      
      if (httr::status_code(resp) >= 200 && httr::status_code(resp) <= 299) {
        # void response, no need to return anything
      } else if (httr::status_code(resp) >= 400 && httr::status_code(resp) <= 499) {
        Response$new("API client error", resp)
      } else if (httr::status_code(resp) >= 500 && httr::status_code(resp) <= 599) {
        Response$new("API server error", resp)
      }

    },
    post_jmx_repository = function(action, ...){
      args <- list(...)
      queryParams <- list()
      headerParams <- character()

      urlPath <- "/system/console/jmx/com.adobe.granite:type&#x3D;Repository/op/{action}"
      if (!missing(`action`)) {
        urlPath <- gsub(paste0("\\{", "action", "\\}"), `action`, urlPath)
      }

      resp <- self$apiClient$callApi(url = paste0(self$apiClient$basePath, urlPath),
                                 method = "POST",
                                 queryParams = queryParams,
                                 headerParams = headerParams,
                                 body = body,
                                 ...)
      
      if (httr::status_code(resp) >= 200 && httr::status_code(resp) <= 299) {
        # void response, no need to return anything
      } else if (httr::status_code(resp) >= 400 && httr::status_code(resp) <= 499) {
        Response$new("API client error", resp)
      } else if (httr::status_code(resp) >= 500 && httr::status_code(resp) <= 599) {
        Response$new("API server error", resp)
      }

    },
    post_saml_configuration = function(post, apply, delete, action, location, path, service_ranking, idp_url, idp_cert_alias, idp_http_redirect, service_provider_entity_id, assertion_consumer_service_url, sp_private_key_alias, key_store_password, default_redirect_url, user_id_attribute, use_encryption, create_user, add_group_memberships, group_membership_attribute, default_groups, name_id_format, synchronize_attributes, handle_logout, logout_url, clock_tolerance, digest_method, signature_method, user_intermediate_path, propertylist, ...){
      args <- list(...)
      queryParams <- list()
      headerParams <- character()

      if (!missing(`post`)) {
        queryParams['post'] <- post
      }

      if (!missing(`apply`)) {
        queryParams['apply'] <- apply
      }

      if (!missing(`delete`)) {
        queryParams['delete'] <- delete
      }

      if (!missing(`action`)) {
        queryParams['action'] <- action
      }

      if (!missing(`location`)) {
        queryParams['$location'] <- location
      }

      if (!missing(`path`)) {
        queryParams['path'] <- path
      }

      if (!missing(`service_ranking`)) {
        queryParams['service.ranking'] <- service_ranking
      }

      if (!missing(`idp_url`)) {
        queryParams['idpUrl'] <- idp_url
      }

      if (!missing(`idp_cert_alias`)) {
        queryParams['idpCertAlias'] <- idp_cert_alias
      }

      if (!missing(`idp_http_redirect`)) {
        queryParams['idpHttpRedirect'] <- idp_http_redirect
      }

      if (!missing(`service_provider_entity_id`)) {
        queryParams['serviceProviderEntityId'] <- service_provider_entity_id
      }

      if (!missing(`assertion_consumer_service_url`)) {
        queryParams['assertionConsumerServiceURL'] <- assertion_consumer_service_url
      }

      if (!missing(`sp_private_key_alias`)) {
        queryParams['spPrivateKeyAlias'] <- sp_private_key_alias
      }

      if (!missing(`key_store_password`)) {
        queryParams['keyStorePassword'] <- key_store_password
      }

      if (!missing(`default_redirect_url`)) {
        queryParams['defaultRedirectUrl'] <- default_redirect_url
      }

      if (!missing(`user_id_attribute`)) {
        queryParams['userIDAttribute'] <- user_id_attribute
      }

      if (!missing(`use_encryption`)) {
        queryParams['useEncryption'] <- use_encryption
      }

      if (!missing(`create_user`)) {
        queryParams['createUser'] <- create_user
      }

      if (!missing(`add_group_memberships`)) {
        queryParams['addGroupMemberships'] <- add_group_memberships
      }

      if (!missing(`group_membership_attribute`)) {
        queryParams['groupMembershipAttribute'] <- group_membership_attribute
      }

      if (!missing(`default_groups`)) {
        queryParams['defaultGroups'] <- default_groups
      }

      if (!missing(`name_id_format`)) {
        queryParams['nameIdFormat'] <- name_id_format
      }

      if (!missing(`synchronize_attributes`)) {
        queryParams['synchronizeAttributes'] <- synchronize_attributes
      }

      if (!missing(`handle_logout`)) {
        queryParams['handleLogout'] <- handle_logout
      }

      if (!missing(`logout_url`)) {
        queryParams['logoutUrl'] <- logout_url
      }

      if (!missing(`clock_tolerance`)) {
        queryParams['clockTolerance'] <- clock_tolerance
      }

      if (!missing(`digest_method`)) {
        queryParams['digestMethod'] <- digest_method
      }

      if (!missing(`signature_method`)) {
        queryParams['signatureMethod'] <- signature_method
      }

      if (!missing(`user_intermediate_path`)) {
        queryParams['userIntermediatePath'] <- user_intermediate_path
      }

      if (!missing(`propertylist`)) {
        queryParams['propertylist'] <- propertylist
      }

      urlPath <- "/system/console/configMgr/com.adobe.granite.auth.saml.SamlAuthenticationHandler"
      resp <- self$apiClient$callApi(url = paste0(self$apiClient$basePath, urlPath),
                                 method = "POST",
                                 queryParams = queryParams,
                                 headerParams = headerParams,
                                 body = body,
                                 ...)
      
      if (httr::status_code(resp) >= 200 && httr::status_code(resp) <= 299) {
        returnObject <- SamlConfigurationInfo$new()
        result <- returnObject$fromJSON(httr::content(resp, "text", encoding = "UTF-8"))
        Response$new(returnObject, resp)
      } else if (httr::status_code(resp) >= 400 && httr::status_code(resp) <= 499) {
        Response$new("API client error", resp)
      } else if (httr::status_code(resp) >= 500 && httr::status_code(resp) <= 599) {
        Response$new("API server error", resp)
      }

    }
  )
)
