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
/*
 * CustomApi.h
 *
 * 
 */

#ifndef CustomApi_H_
#define CustomApi_H_


#include <pistache/endpoint.h>
#include <pistache/http.h>
#include <pistache/router.h>
#include <pistache/http_headers.h>

#include <pistache/optional.h>

#include <string>

namespace org {
namespace openapitools {
namespace server {
namespace api {

using namespace org::openapitools::server::model;

class  CustomApi {
public:
    CustomApi(Pistache::Address addr);
    virtual ~CustomApi() {};
    void init(size_t thr);
    void start();
    void shutdown();

    const std::string base = "/";

private:
    void setupRoutes();

    void get_aem_health_check_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void post_config_aem_health_check_servlet_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void post_config_aem_password_reset_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void custom_api_default_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);

    Pistache::Http::Endpoint httpEndpoint;
    Pistache::Rest::Router router;


    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// 
    /// </remarks>
    /// <param name="tags"> (optional)</param>
    /// <param name="combineTagsOr"> (optional)</param>
    virtual void get_aem_health_check(const Pistache::Optional<std::string> &tags, const Pistache::Optional<bool> &combineTagsOr, Pistache::Http::ResponseWriter &response) = 0;

    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// 
    /// </remarks>
    /// <param name="bundlesPeriodignored"> (optional)</param>
    /// <param name="bundlesPeriodignoredAtTypeHint"> (optional)</param>
    virtual void post_config_aem_health_check_servlet(const Pistache::Optional<std::string> &bundlesPeriodignored, const Pistache::Optional<std::string> &bundlesPeriodignoredAtTypeHint, Pistache::Http::ResponseWriter &response) = 0;

    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// 
    /// </remarks>
    /// <param name="pwdresetPeriodauthorizables"> (optional)</param>
    /// <param name="pwdresetPeriodauthorizablesAtTypeHint"> (optional)</param>
    virtual void post_config_aem_password_reset(const Pistache::Optional<std::string> &pwdresetPeriodauthorizables, const Pistache::Optional<std::string> &pwdresetPeriodauthorizablesAtTypeHint, Pistache::Http::ResponseWriter &response) = 0;

};

}
}
}
}

#endif /* CustomApi_H_ */
