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


package com.shinesolutions.swaggeraem4j.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

/**
 * TruststoreItems
 */
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2018-08-30T04:12:03.132Z")
public class TruststoreItems {
  @SerializedName("alias")
  private String alias = null;

  @SerializedName("entryType")
  private String entryType = null;

  @SerializedName("subject")
  private String subject = null;

  @SerializedName("issuer")
  private String issuer = null;

  @SerializedName("notBefore")
  private String notBefore = null;

  @SerializedName("notAfter")
  private String notAfter = null;

  @SerializedName("serialNumber")
  private Integer serialNumber = null;

  public TruststoreItems alias(String alias) {
    this.alias = alias;
    return this;
  }

   /**
   * Truststore alias name
   * @return alias
  **/
  @ApiModelProperty(value = "Truststore alias name")
  public String getAlias() {
    return alias;
  }

  public void setAlias(String alias) {
    this.alias = alias;
  }

  public TruststoreItems entryType(String entryType) {
    this.entryType = entryType;
    return this;
  }

   /**
   * Get entryType
   * @return entryType
  **/
  @ApiModelProperty(value = "")
  public String getEntryType() {
    return entryType;
  }

  public void setEntryType(String entryType) {
    this.entryType = entryType;
  }

  public TruststoreItems subject(String subject) {
    this.subject = subject;
    return this;
  }

   /**
   * e.g. \&quot;CN&#x3D;localhost\&quot;
   * @return subject
  **/
  @ApiModelProperty(value = "e.g. \"CN=localhost\"")
  public String getSubject() {
    return subject;
  }

  public void setSubject(String subject) {
    this.subject = subject;
  }

  public TruststoreItems issuer(String issuer) {
    this.issuer = issuer;
    return this;
  }

   /**
   * e.g. \&quot;CN&#x3D;Admin\&quot;
   * @return issuer
  **/
  @ApiModelProperty(value = "e.g. \"CN=Admin\"")
  public String getIssuer() {
    return issuer;
  }

  public void setIssuer(String issuer) {
    this.issuer = issuer;
  }

  public TruststoreItems notBefore(String notBefore) {
    this.notBefore = notBefore;
    return this;
  }

   /**
   * e.g. \&quot;Sun Jul 01 12:00:00 AEST 2018\&quot;
   * @return notBefore
  **/
  @ApiModelProperty(value = "e.g. \"Sun Jul 01 12:00:00 AEST 2018\"")
  public String getNotBefore() {
    return notBefore;
  }

  public void setNotBefore(String notBefore) {
    this.notBefore = notBefore;
  }

  public TruststoreItems notAfter(String notAfter) {
    this.notAfter = notAfter;
    return this;
  }

   /**
   * e.g. \&quot;Sun Jun 30 23:59:50 AEST 2019\&quot;
   * @return notAfter
  **/
  @ApiModelProperty(value = "e.g. \"Sun Jun 30 23:59:50 AEST 2019\"")
  public String getNotAfter() {
    return notAfter;
  }

  public void setNotAfter(String notAfter) {
    this.notAfter = notAfter;
  }

  public TruststoreItems serialNumber(Integer serialNumber) {
    this.serialNumber = serialNumber;
    return this;
  }

   /**
   * 18165099476682912368
   * @return serialNumber
  **/
  @ApiModelProperty(value = "18165099476682912368")
  public Integer getSerialNumber() {
    return serialNumber;
  }

  public void setSerialNumber(Integer serialNumber) {
    this.serialNumber = serialNumber;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TruststoreItems truststoreItems = (TruststoreItems) o;
    return Objects.equals(this.alias, truststoreItems.alias) &&
        Objects.equals(this.entryType, truststoreItems.entryType) &&
        Objects.equals(this.subject, truststoreItems.subject) &&
        Objects.equals(this.issuer, truststoreItems.issuer) &&
        Objects.equals(this.notBefore, truststoreItems.notBefore) &&
        Objects.equals(this.notAfter, truststoreItems.notAfter) &&
        Objects.equals(this.serialNumber, truststoreItems.serialNumber);
  }

  @Override
  public int hashCode() {
    return Objects.hash(alias, entryType, subject, issuer, notBefore, notAfter, serialNumber);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TruststoreItems {\n");
    
    sb.append("    alias: ").append(toIndentedString(alias)).append("\n");
    sb.append("    entryType: ").append(toIndentedString(entryType)).append("\n");
    sb.append("    subject: ").append(toIndentedString(subject)).append("\n");
    sb.append("    issuer: ").append(toIndentedString(issuer)).append("\n");
    sb.append("    notBefore: ").append(toIndentedString(notBefore)).append("\n");
    sb.append("    notAfter: ").append(toIndentedString(notAfter)).append("\n");
    sb.append("    serialNumber: ").append(toIndentedString(serialNumber)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

