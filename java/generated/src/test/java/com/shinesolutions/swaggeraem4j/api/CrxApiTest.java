/*
 * Adobe Experience Manager (AEM) API
 * Swagger AEM is an OpenAPI specification for Adobe Experience Manager (AEM) API
 *
 * OpenAPI spec version: 2.2.0
 * Contact: opensource@shinesolutions.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package com.shinesolutions.swaggeraem4j.api;

import com.shinesolutions.swaggeraem4j.ApiException;
import java.io.File;
import com.shinesolutions.swaggeraem4j.model.InstallStatus;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CrxApi
 */
@Ignore
public class CrxApiTest {

    private final CrxApi api = new CrxApi();

    
    /**
     * 
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getCrxdeStatusTest() throws ApiException {
        String response = api.getCrxdeStatus();

        // TODO: test validations
    }
    
    /**
     * 
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getInstallStatusTest() throws ApiException {
        InstallStatus response = api.getInstallStatus();

        // TODO: test validations
    }
    
    /**
     * 
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void postPackageServiceTest() throws ApiException {
        String cmd = null;
        String response = api.postPackageService(cmd);

        // TODO: test validations
    }
    
    /**
     * 
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void postPackageServiceJsonTest() throws ApiException {
        String path = null;
        String cmd = null;
        String groupName = null;
        String packageName = null;
        String packageVersion = null;
        String charset_ = null;
        Boolean force = null;
        Boolean recursive = null;
        File _package = null;
        String response = api.postPackageServiceJson(path, cmd, groupName, packageName, packageVersion, charset_, force, recursive, _package);

        // TODO: test validations
    }
    
    /**
     * 
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void postPackageUpdateTest() throws ApiException {
        String groupName = null;
        String packageName = null;
        String version = null;
        String path = null;
        String filter = null;
        String charset_ = null;
        String response = api.postPackageUpdate(groupName, packageName, version, path, filter, charset_);

        // TODO: test validations
    }
    
    /**
     * 
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void postSetPasswordTest() throws ApiException {
        String old = null;
        String plain = null;
        String verify = null;
        String response = api.postSetPassword(old, plain, verify);

        // TODO: test validations
    }
    
}
