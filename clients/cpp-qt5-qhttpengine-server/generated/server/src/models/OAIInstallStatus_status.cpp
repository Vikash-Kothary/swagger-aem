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


#include "OAIInstallStatus_status.h"

#include "OAIHelpers.h"

#include <QJsonDocument>
#include <QJsonArray>
#include <QObject>
#include <QDebug>

namespace OpenAPI {

OAIInstallStatus_status::OAIInstallStatus_status(QString json) {
    this->fromJson(json);
}

OAIInstallStatus_status::OAIInstallStatus_status() {
    this->init();
}

OAIInstallStatus_status::~OAIInstallStatus_status() {
    
}

void
OAIInstallStatus_status::init() {
    m_finished_isSet = false;
    m_item_count_isSet = false;
}

void
OAIInstallStatus_status::fromJson(QString jsonString) {
    QByteArray array (jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void
OAIInstallStatus_status::fromJsonObject(QJsonObject json) {
    ::OpenAPI::fromJsonValue(finished, json[QString("finished")]);
    
    ::OpenAPI::fromJsonValue(item_count, json[QString("itemCount")]);
    
}

QString
OAIInstallStatus_status::asJson () const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject
OAIInstallStatus_status::asJsonObject() const {
    QJsonObject obj;
	if(m_finished_isSet){
        obj.insert(QString("finished"), ::OpenAPI::toJsonValue(finished));
    }
	if(m_item_count_isSet){
        obj.insert(QString("itemCount"), ::OpenAPI::toJsonValue(item_count));
    }
    return obj;
}

bool
OAIInstallStatus_status::isFinished() const {
    return finished;
}
void
OAIInstallStatus_status::setFinished(const bool &finished) {
    this->finished = finished;
    this->m_finished_isSet = true;
}

qint32
OAIInstallStatus_status::getItemCount() const {
    return item_count;
}
void
OAIInstallStatus_status::setItemCount(const qint32 &item_count) {
    this->item_count = item_count;
    this->m_item_count_isSet = true;
}


bool
OAIInstallStatus_status::isSet() const {
    bool isObjectUpdated = false;
    do{ 
        if(m_finished_isSet){ isObjectUpdated = true; break;}
    
        if(m_item_count_isSet){ isObjectUpdated = true; break;}
    }while(false);
    return isObjectUpdated;
}

}
