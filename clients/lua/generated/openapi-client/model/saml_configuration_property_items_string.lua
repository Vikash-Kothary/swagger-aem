--[[
  Adobe Experience Manager (AEM) API
 
  Swagger AEM is an OpenAPI specification for Adobe Experience Manager (AEM) API
 
  OpenAPI spec version: 3.2.0-pre.0
  Contact: opensource@shinesolutions.com
  Generated by: https://openapi-generator.tech
]]

-- saml_configuration_property_items_string class
local saml_configuration_property_items_string = {}
local saml_configuration_property_items_string_mt = {
	__name = "saml_configuration_property_items_string";
	__index = saml_configuration_property_items_string;
}

local function cast_saml_configuration_property_items_string(t)
	return setmetatable(t, saml_configuration_property_items_string_mt)
end

local function new_saml_configuration_property_items_string(name, optional, is_set, type, value, description)
	return cast_saml_configuration_property_items_string({
		["name"] = name;
		["optional"] = optional;
		["is_set"] = is_set;
		["type"] = type;
		["value"] = value;
		["description"] = description;
	})
end

return {
	cast = cast_saml_configuration_property_items_string;
	new = new_saml_configuration_property_items_string;
}