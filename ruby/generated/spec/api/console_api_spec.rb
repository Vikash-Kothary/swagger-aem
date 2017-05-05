=begin
#Adobe Experience Manager (AEM) API

#Swagger AEM is an OpenAPI specification for Adobe Experience Manager (AEM) API

OpenAPI spec version: 1.2.0
Contact: opensource@shinesolutions.com
Generated by: https://github.com/swagger-api/swagger-codegen.git

=end

require 'spec_helper'
require 'json'

# Unit tests for SwaggerAemClient::ConsoleApi
# Automatically generated by swagger-codegen (github.com/swagger-api/swagger-codegen)
# Please update as you see appropriate
describe 'ConsoleApi' do
  before do
    # run before each test
    @instance = SwaggerAemClient::ConsoleApi.new
  end

  after do
    # run after each test
  end

  describe 'test an instance of ConsoleApi' do
    it 'should create an instact of ConsoleApi' do
      expect(@instance).to be_instance_of(SwaggerAemClient::ConsoleApi)
    end
  end

  # unit tests for post_bundle
  # 
  # 
  # @param name 
  # @param action 
  # @param [Hash] opts the optional parameters
  # @return [nil]
  describe 'post_bundle test' do
    it "should work" do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for post_jmx_repository
  # 
  # 
  # @param action 
  # @param [Hash] opts the optional parameters
  # @return [nil]
  describe 'post_jmx_repository test' do
    it "should work" do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

end
