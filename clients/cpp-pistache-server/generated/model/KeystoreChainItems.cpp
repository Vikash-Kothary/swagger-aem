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


#include "KeystoreChainItems.h"

namespace org {
namespace openapitools {
namespace server {
namespace model {

KeystoreChainItems::KeystoreChainItems()
{
    m_Subject = "";
    m_SubjectIsSet = false;
    m_Issuer = "";
    m_IssuerIsSet = false;
    m_NotBefore = "";
    m_NotBeforeIsSet = false;
    m_NotAfter = "";
    m_NotAfterIsSet = false;
    m_SerialNumber = 0;
    m_SerialNumberIsSet = false;
    
}

KeystoreChainItems::~KeystoreChainItems()
{
}

void KeystoreChainItems::validate()
{
    // TODO: implement validation
}

nlohmann::json KeystoreChainItems::toJson() const
{
    nlohmann::json val = nlohmann::json::object();

    if(m_SubjectIsSet)
    {
        val["subject"] = ModelBase::toJson(m_Subject);
    }
    if(m_IssuerIsSet)
    {
        val["issuer"] = ModelBase::toJson(m_Issuer);
    }
    if(m_NotBeforeIsSet)
    {
        val["notBefore"] = ModelBase::toJson(m_NotBefore);
    }
    if(m_NotAfterIsSet)
    {
        val["notAfter"] = ModelBase::toJson(m_NotAfter);
    }
    if(m_SerialNumberIsSet)
    {
        val["serialNumber"] = m_SerialNumber;
    }
    

    return val;
}

void KeystoreChainItems::fromJson(nlohmann::json& val)
{
    if(val.find("subject") != val.end())
    {
        setSubject(val.at("subject"));
    }
    if(val.find("issuer") != val.end())
    {
        setIssuer(val.at("issuer"));
    }
    if(val.find("notBefore") != val.end())
    {
        setNotBefore(val.at("notBefore"));
    }
    if(val.find("notAfter") != val.end())
    {
        setNotAfter(val.at("notAfter"));
    }
    if(val.find("serialNumber") != val.end())
    {
        setSerialNumber(val.at("serialNumber"));
    }
    
}


std::string KeystoreChainItems::getSubject() const
{
    return m_Subject;
}
void KeystoreChainItems::setSubject(std::string const& value)
{
    m_Subject = value;
    m_SubjectIsSet = true;
}
bool KeystoreChainItems::subjectIsSet() const
{
    return m_SubjectIsSet;
}
void KeystoreChainItems::unsetSubject()
{
    m_SubjectIsSet = false;
}
std::string KeystoreChainItems::getIssuer() const
{
    return m_Issuer;
}
void KeystoreChainItems::setIssuer(std::string const& value)
{
    m_Issuer = value;
    m_IssuerIsSet = true;
}
bool KeystoreChainItems::issuerIsSet() const
{
    return m_IssuerIsSet;
}
void KeystoreChainItems::unsetIssuer()
{
    m_IssuerIsSet = false;
}
std::string KeystoreChainItems::getNotBefore() const
{
    return m_NotBefore;
}
void KeystoreChainItems::setNotBefore(std::string const& value)
{
    m_NotBefore = value;
    m_NotBeforeIsSet = true;
}
bool KeystoreChainItems::notBeforeIsSet() const
{
    return m_NotBeforeIsSet;
}
void KeystoreChainItems::unsetNotBefore()
{
    m_NotBeforeIsSet = false;
}
std::string KeystoreChainItems::getNotAfter() const
{
    return m_NotAfter;
}
void KeystoreChainItems::setNotAfter(std::string const& value)
{
    m_NotAfter = value;
    m_NotAfterIsSet = true;
}
bool KeystoreChainItems::notAfterIsSet() const
{
    return m_NotAfterIsSet;
}
void KeystoreChainItems::unsetNotAfter()
{
    m_NotAfterIsSet = false;
}
int32_t KeystoreChainItems::getSerialNumber() const
{
    return m_SerialNumber;
}
void KeystoreChainItems::setSerialNumber(int32_t const value)
{
    m_SerialNumber = value;
    m_SerialNumberIsSet = true;
}
bool KeystoreChainItems::serialNumberIsSet() const
{
    return m_SerialNumberIsSet;
}
void KeystoreChainItems::unsetSerialNumber()
{
    m_SerialNumberIsSet = false;
}

}
}
}
}
