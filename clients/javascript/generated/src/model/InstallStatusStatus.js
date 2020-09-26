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
 * The InstallStatusStatus model module.
 * @module model/InstallStatusStatus
 * @version 0.9.0
 */
class InstallStatusStatus {
    /**
     * Constructs a new <code>InstallStatusStatus</code>.
     * @alias module:model/InstallStatusStatus
     */
    constructor() { 
        
        InstallStatusStatus.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>InstallStatusStatus</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/InstallStatusStatus} obj Optional instance to populate.
     * @return {module:model/InstallStatusStatus} The populated <code>InstallStatusStatus</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new InstallStatusStatus();

            if (data.hasOwnProperty('finished')) {
                obj['finished'] = ApiClient.convertToType(data['finished'], 'Boolean');
            }
            if (data.hasOwnProperty('itemCount')) {
                obj['itemCount'] = ApiClient.convertToType(data['itemCount'], 'Number');
            }
        }
        return obj;
    }


}

/**
 * @member {Boolean} finished
 */
InstallStatusStatus.prototype['finished'] = undefined;

/**
 * @member {Number} itemCount
 */
InstallStatusStatus.prototype['itemCount'] = undefined;






export default InstallStatusStatus;

