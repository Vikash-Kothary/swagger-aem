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

#include <QJsonArray>
#include <QJsonDocument>
#include <QJsonObject>
#include <QVariantMap>
#include <QDebug>

#include "OAICqApiHandler.h"
#include "OAICqApiRequest.h"

namespace OpenAPI {

OAICqApiHandler::OAICqApiHandler(){

}

OAICqApiHandler::~OAICqApiHandler(){

}

void OAICqApiHandler::getLoginPage() {
    auto reqObj = qobject_cast<OAICqApiRequest*>(sender());
    if( reqObj != nullptr ) 
    { 
        QString res;
        reqObj->getLoginPageResponse(res);
    }    
}
void OAICqApiHandler::postCqActions(QString authorizable_id, QString changelog) {
    Q_UNUSED(authorizable_id);
    Q_UNUSED(changelog);
    auto reqObj = qobject_cast<OAICqApiRequest*>(sender());
    if( reqObj != nullptr ) 
    { 
        
        reqObj->postCqActionsResponse();
    }    
}


}