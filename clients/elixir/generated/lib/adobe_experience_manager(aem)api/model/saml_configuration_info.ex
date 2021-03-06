# NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
# https://openapi-generator.tech
# Do not edit the class manually.

defmodule AdobeExperienceManager(AEM)API.Model.SamlConfigurationInfo do
  @moduledoc """
  
  """

  @derive [Poison.Encoder]
  defstruct [
    :"pid",
    :"title",
    :"description",
    :"bundle_location",
    :"service_location",
    :"properties"
  ]

  @type t :: %__MODULE__{
    :"pid" => String.t,
    :"title" => String.t,
    :"description" => String.t,
    :"bundle_location" => String.t,
    :"service_location" => String.t,
    :"properties" => SamlConfigurationProperties
  }
end

defimpl Poison.Decoder, for: AdobeExperienceManager(AEM)API.Model.SamlConfigurationInfo do
  import AdobeExperienceManager(AEM)API.Deserializer
  def decode(value, options) do
    value
    |> deserialize(:"properties", :struct, AdobeExperienceManager(AEM)API.Model.SamlConfigurationProperties, options)
  end
end

