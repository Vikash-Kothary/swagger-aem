/**
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech) (3.2.1-SNAPSHOT).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
package org.openapitools.api;

import org.openapitools.model.KeystoreInfo;
import org.springframework.core.io.Resource;
import io.swagger.annotations.*;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RequestPart;
import org.springframework.web.context.request.NativeWebRequest;
import org.springframework.web.multipart.MultipartFile;

import javax.validation.Valid;
import javax.validation.constraints.*;
import java.util.List;
import java.util.Map;
import java.util.Optional;
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2019-08-04T23:44:43.219Z[GMT]")

@Validated
@Api(value = "{intermediatePath}", description = "the {intermediatePath} API")
public interface IntermediatePathApi {

    default Optional<NativeWebRequest> getRequest() {
        return Optional.empty();
    }

    @ApiOperation(value = "", nickname = "getAuthorizableKeystore", notes = "", response = KeystoreInfo.class, authorizations = {
        @Authorization(value = "aemAuth")
    }, tags={ "sling", })
    @ApiResponses(value = { 
        @ApiResponse(code = 200, message = "Retrieved Authorizable Keystore info", response = KeystoreInfo.class),
        @ApiResponse(code = 200, message = "Default response", response = String.class) })
    @RequestMapping(value = "/{intermediatePath}/{authorizableId}.ks.json",
        produces = { "text/plain" }, 
        method = RequestMethod.GET)
    default ResponseEntity<KeystoreInfo> getAuthorizableKeystore(@ApiParam(value = "",required=true) @PathVariable("intermediatePath") String intermediatePath,@ApiParam(value = "",required=true) @PathVariable("authorizableId") String authorizableId) {
        getRequest().ifPresent(request -> {
            for (MediaType mediaType: MediaType.parseMediaTypes(request.getHeader("Accept"))) {
                if (mediaType.isCompatibleWith(MediaType.valueOf(""))) {
                    ApiUtil.setExampleResponse(request, "", "");
                    break;
                }
            }
        });
        return new ResponseEntity<>(HttpStatus.NOT_IMPLEMENTED);

    }


    @ApiOperation(value = "", nickname = "getKeystore", notes = "", response = Resource.class, authorizations = {
        @Authorization(value = "aemAuth")
    }, tags={ "sling", })
    @ApiResponses(value = { 
        @ApiResponse(code = 200, message = "Default response", response = Resource.class) })
    @RequestMapping(value = "/{intermediatePath}/{authorizableId}/keystore/store.p12",
        produces = { "application/octet-stream" }, 
        method = RequestMethod.GET)
    default ResponseEntity<Resource> getKeystore(@ApiParam(value = "",required=true) @PathVariable("intermediatePath") String intermediatePath,@ApiParam(value = "",required=true) @PathVariable("authorizableId") String authorizableId) {
        return new ResponseEntity<>(HttpStatus.NOT_IMPLEMENTED);

    }


    @ApiOperation(value = "", nickname = "postAuthorizableKeystore", notes = "", response = KeystoreInfo.class, authorizations = {
        @Authorization(value = "aemAuth")
    }, tags={ "sling", })
    @ApiResponses(value = { 
        @ApiResponse(code = 200, message = "Retrieved Authorizable Keystore info", response = KeystoreInfo.class),
        @ApiResponse(code = 200, message = "Default response", response = String.class) })
    @RequestMapping(value = "/{intermediatePath}/{authorizableId}.ks.html",
        produces = { "text/plain" }, 
        consumes = { "multipart/form-data" },
        method = RequestMethod.POST)
    default ResponseEntity<KeystoreInfo> postAuthorizableKeystore(@ApiParam(value = "",required=true) @PathVariable("intermediatePath") String intermediatePath,@ApiParam(value = "",required=true) @PathVariable("authorizableId") String authorizableId,@ApiParam(value = "") @Valid @RequestParam(value = ":operation", required = false) String colonOperation,@ApiParam(value = "") @Valid @RequestParam(value = "currentPassword", required = false) String currentPassword,@ApiParam(value = "") @Valid @RequestParam(value = "newPassword", required = false) String newPassword,@ApiParam(value = "") @Valid @RequestParam(value = "rePassword", required = false) String rePassword,@ApiParam(value = "") @Valid @RequestParam(value = "keyPassword", required = false) String keyPassword,@ApiParam(value = "") @Valid @RequestParam(value = "keyStorePass", required = false) String keyStorePass,@ApiParam(value = "") @Valid @RequestParam(value = "alias", required = false) String alias,@ApiParam(value = "") @Valid @RequestParam(value = "newAlias", required = false) String newAlias,@ApiParam(value = "") @Valid @RequestParam(value = "removeAlias", required = false) String removeAlias,@ApiParam(value = "file detail") @Valid @RequestPart("file") MultipartFile cert-chain,@ApiParam(value = "file detail") @Valid @RequestPart("file") MultipartFile pk,@ApiParam(value = "file detail") @Valid @RequestPart("file") MultipartFile keyStore) {
        getRequest().ifPresent(request -> {
            for (MediaType mediaType: MediaType.parseMediaTypes(request.getHeader("Accept"))) {
                if (mediaType.isCompatibleWith(MediaType.valueOf(""))) {
                    ApiUtil.setExampleResponse(request, "", "");
                    break;
                }
            }
        });
        return new ResponseEntity<>(HttpStatus.NOT_IMPLEMENTED);

    }

}
