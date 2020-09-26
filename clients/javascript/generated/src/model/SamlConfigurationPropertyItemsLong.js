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

import ApiClient from '../ApiClient';

/**
 * The SamlConfigurationPropertyItemsLong model module.
 * @module model/SamlConfigurationPropertyItemsLong
 * @version 0.9.0
 */
class SamlConfigurationPropertyItemsLong {
    /**
     * Constructs a new <code>SamlConfigurationPropertyItemsLong</code>.
     * @alias module:model/SamlConfigurationPropertyItemsLong
     */
    constructor() { 
        
        SamlConfigurationPropertyItemsLong.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SamlConfigurationPropertyItemsLong</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SamlConfigurationPropertyItemsLong} obj Optional instance to populate.
     * @return {module:model/SamlConfigurationPropertyItemsLong} The populated <code>SamlConfigurationPropertyItemsLong</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SamlConfigurationPropertyItemsLong();

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('optional')) {
                obj['optional'] = ApiClient.convertToType(data['optional'], 'Boolean');
            }
            if (data.hasOwnProperty('is_set')) {
                obj['is_set'] = ApiClient.convertToType(data['is_set'], 'Boolean');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'Number');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], 'Number');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
        }
        return obj;
    }


}

/**
 * property name
 * @member {String} name
 */
SamlConfigurationPropertyItemsLong.prototype['name'] = undefined;

/**
 * True if optional
 * @member {Boolean} optional
 */
SamlConfigurationPropertyItemsLong.prototype['optional'] = undefined;

/**
 * True if property is set
 * @member {Boolean} is_set
 */
SamlConfigurationPropertyItemsLong.prototype['is_set'] = undefined;

/**
 * Property type, 1=String, 3=long, 11=boolean, 12=Password
 * @member {Number} type
 */
SamlConfigurationPropertyItemsLong.prototype['type'] = undefined;

/**
 * Property value
 * @member {Number} value
 */
SamlConfigurationPropertyItemsLong.prototype['value'] = undefined;

/**
 * Property description
 * @member {String} description
 */
SamlConfigurationPropertyItemsLong.prototype['description'] = undefined;






export default SamlConfigurationPropertyItemsLong;

