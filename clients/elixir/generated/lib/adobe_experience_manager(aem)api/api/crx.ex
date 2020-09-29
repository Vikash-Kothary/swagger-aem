# NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
# https://openapi-generator.tech
# Do not edit the class manually.

defmodule AdobeExperienceManager(AEM)API.Api.Crx do
  @moduledoc """
  API calls for all endpoints tagged `Crx`.
  """

  alias AdobeExperienceManager(AEM)API.Connection
  import AdobeExperienceManager(AEM)API.RequestBuilder


  @doc """

  ## Parameters

  - connection (AdobeExperienceManager(AEM)API.Connection): Connection to server
  - opts (KeywordList): [optional] Optional parameters
  ## Returns

  {:ok, %AdobeExperienceManager(AEM)API.Model.String.t{}} on success
  {:error, info} on failure
  """
  @spec get_crxde_status(Tesla.Env.client, keyword()) :: {:ok, String.t} | {:error, Tesla.Env.t}
  def get_crxde_status(connection, _opts \\ []) do
    %{}
    |> method(:get)
    |> url("/crx/server/crx.default/jcr:root/.1.json")
    |> Enum.into([])
    |> (&Connection.request(connection, &1)).()
    |> decode(false)
  end

  @doc """

  ## Parameters

  - connection (AdobeExperienceManager(AEM)API.Connection): Connection to server
  - opts (KeywordList): [optional] Optional parameters
  ## Returns

  {:ok, %AdobeExperienceManager(AEM)API.Model.InstallStatus{}} on success
  {:error, info} on failure
  """
  @spec get_install_status(Tesla.Env.client, keyword()) :: {:ok, AdobeExperienceManager(AEM)API.Model.InstallStatus.t} | {:error, Tesla.Env.t}
  def get_install_status(connection, _opts \\ []) do
    %{}
    |> method(:get)
    |> url("/crx/packmgr/installstatus.jsp")
    |> Enum.into([])
    |> (&Connection.request(connection, &1)).()
    |> decode(%AdobeExperienceManager(AEM)API.Model.InstallStatus{})
  end

  @doc """

  ## Parameters

  - connection (AdobeExperienceManager(AEM)API.Connection): Connection to server
  - opts (KeywordList): [optional] Optional parameters
  ## Returns

  {:ok, %{}} on success
  {:error, info} on failure
  """
  @spec get_package_manager_servlet(Tesla.Env.client, keyword()) :: {:ok, nil} | {:error, Tesla.Env.t}
  def get_package_manager_servlet(connection, _opts \\ []) do
    %{}
    |> method(:get)
    |> url("/crx/packmgr/service/script.html")
    |> Enum.into([])
    |> (&Connection.request(connection, &1)).()
    |> decode(false)
  end

  @doc """

  ## Parameters

  - connection (AdobeExperienceManager(AEM)API.Connection): Connection to server
  - cmd (String.t): 
  - opts (KeywordList): [optional] Optional parameters
  ## Returns

  {:ok, %AdobeExperienceManager(AEM)API.Model.String.t{}} on success
  {:error, info} on failure
  """
  @spec post_package_service(Tesla.Env.client, String.t, keyword()) :: {:ok, String.t} | {:error, Tesla.Env.t}
  def post_package_service(connection, cmd, _opts \\ []) do
    %{}
    |> method(:post)
    |> url("/crx/packmgr/service.jsp")
    |> add_param(:query, :"cmd", cmd)
    |> Enum.into([])
    |> (&Connection.request(connection, &1)).()
    |> decode(false)
  end

  @doc """

  ## Parameters

  - connection (AdobeExperienceManager(AEM)API.Connection): Connection to server
  - path (String.t): 
  - cmd (String.t): 
  - opts (KeywordList): [optional] Optional parameters
    - :group_name (String.t): 
    - :package_name (String.t): 
    - :package_version (String.t): 
    - :charset (String.t): 
    - :force (boolean()): 
    - :recursive (boolean()): 
    - :package (String.t): 
  ## Returns

  {:ok, %AdobeExperienceManager(AEM)API.Model.String.t{}} on success
  {:error, info} on failure
  """
  @spec post_package_service_json(Tesla.Env.client, String.t, String.t, keyword()) :: {:ok, String.t} | {:error, Tesla.Env.t}
  def post_package_service_json(connection, path, cmd, opts \\ []) do
    optional_params = %{
      :"groupName" => :query,
      :"packageName" => :query,
      :"packageVersion" => :query,
      :"_charset_" => :query,
      :"force" => :query,
      :"recursive" => :query,
      :"package" => :form
    }
    %{}
    |> method(:post)
    |> url("/crx/packmgr/service/.json/#{path}")
    |> add_param(:query, :"cmd", cmd)
    |> add_optional_params(optional_params, opts)
    |> Enum.into([])
    |> (&Connection.request(connection, &1)).()
    |> decode(false)
  end

  @doc """

  ## Parameters

  - connection (AdobeExperienceManager(AEM)API.Connection): Connection to server
  - group_name (String.t): 
  - package_name (String.t): 
  - version (String.t): 
  - path (String.t): 
  - opts (KeywordList): [optional] Optional parameters
    - :filter (String.t): 
    - :charset (String.t): 
  ## Returns

  {:ok, %AdobeExperienceManager(AEM)API.Model.String.t{}} on success
  {:error, info} on failure
  """
  @spec post_package_update(Tesla.Env.client, String.t, String.t, String.t, String.t, keyword()) :: {:ok, String.t} | {:error, Tesla.Env.t}
  def post_package_update(connection, group_name, package_name, version, path, opts \\ []) do
    optional_params = %{
      :"filter" => :query,
      :"_charset_" => :query
    }
    %{}
    |> method(:post)
    |> url("/crx/packmgr/update.jsp")
    |> add_param(:query, :"groupName", group_name)
    |> add_param(:query, :"packageName", package_name)
    |> add_param(:query, :"version", version)
    |> add_param(:query, :"path", path)
    |> add_optional_params(optional_params, opts)
    |> Enum.into([])
    |> (&Connection.request(connection, &1)).()
    |> decode(false)
  end

  @doc """

  ## Parameters

  - connection (AdobeExperienceManager(AEM)API.Connection): Connection to server
  - old (String.t): 
  - plain (String.t): 
  - verify (String.t): 
  - opts (KeywordList): [optional] Optional parameters
  ## Returns

  {:ok, %AdobeExperienceManager(AEM)API.Model.String.t{}} on success
  {:error, info} on failure
  """
  @spec post_set_password(Tesla.Env.client, String.t, String.t, String.t, keyword()) :: {:ok, String.t} | {:error, Tesla.Env.t}
  def post_set_password(connection, old, plain, verify, _opts \\ []) do
    %{}
    |> method(:post)
    |> url("/crx/explorer/ui/setpassword.jsp")
    |> add_param(:query, :"old", old)
    |> add_param(:query, :"plain", plain)
    |> add_param(:query, :"verify", verify)
    |> Enum.into([])
    |> (&Connection.request(connection, &1)).()
    |> decode(false)
  end
end