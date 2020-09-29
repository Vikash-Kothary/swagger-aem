/**
 * Adobe Experience Manager (AEM) API
 * Swagger AEM is an OpenAPI specification for Adobe Experience Manager (AEM) API
 *
 * OpenAPI spec version: 3.2.0-pre.0
 * Contact: opensource@shinesolutions.com
 *
 * NOTE: This class is auto generated by OpenAPI-Generator 3.2.1-SNAPSHOT.
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */



#include "KeystoreChainItems.h"

#include <string>
#include <sstream>
#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/json_parser.hpp>

using boost::property_tree::ptree;
using boost::property_tree::read_json;
using boost::property_tree::write_json;

namespace org {
namespace openapitools {
namespace server {
namespace model {

KeystoreChainItems::KeystoreChainItems()
{
    m_Subject = "";
    m_Issuer = "";
    m_NotBefore = "";
    m_NotAfter = "";
    m_SerialNumber = 0;
    
}

KeystoreChainItems::~KeystoreChainItems()
{
}

std::string KeystoreChainItems::toJsonString()
{
	std::stringstream ss;
	ptree pt;
	pt.put("Subject", m_Subject);
	pt.put("Issuer", m_Issuer);
	pt.put("NotBefore", m_NotBefore);
	pt.put("NotAfter", m_NotAfter);
	pt.put("SerialNumber", m_SerialNumber);
	write_json(ss, pt, false);
	return ss.str();
}

void KeystoreChainItems::fromJsonString(std::string const& jsonString)
{
	std::stringstream ss(jsonString);
	ptree pt;
	read_json(ss,pt);
	m_Subject = pt.get("Subject", "");
	m_Issuer = pt.get("Issuer", "");
	m_NotBefore = pt.get("NotBefore", "");
	m_NotAfter = pt.get("NotAfter", "");
	m_SerialNumber = pt.get("SerialNumber", 0);
}

std::string KeystoreChainItems::getSubject() const
{
    return m_Subject;
}
void KeystoreChainItems::setSubject(std::string value)
{
    m_Subject = value;
}
std::string KeystoreChainItems::getIssuer() const
{
    return m_Issuer;
}
void KeystoreChainItems::setIssuer(std::string value)
{
    m_Issuer = value;
}
std::string KeystoreChainItems::getNotBefore() const
{
    return m_NotBefore;
}
void KeystoreChainItems::setNotBefore(std::string value)
{
    m_NotBefore = value;
}
std::string KeystoreChainItems::getNotAfter() const
{
    return m_NotAfter;
}
void KeystoreChainItems::setNotAfter(std::string value)
{
    m_NotAfter = value;
}
int32_t KeystoreChainItems::getSerialNumber() const
{
    return m_SerialNumber;
}
void KeystoreChainItems::setSerialNumber(int32_t value)
{
    m_SerialNumber = value;
}

}
}
}
}
