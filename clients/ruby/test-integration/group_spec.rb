require_relative 'spec_helper'

describe 'Group' do
  before do
    init_client
    @sling = SwaggerAemClient::SlingApi.new
    @cq = SwaggerAemClient::CqApi.new

    # ensure group doesn't exist prior to testing
    authorizable_id = find_authorizable_id(@sling, '/home/groups/s', 'somegroup')
    if authorizable_id
      data, status_code, headers = @sling.delete_node_with_http_info(
        path = 'home/groups/s',
        name = authorizable_id
      )
      expect(status_code).to eq(204)
    end

    # create group
    data, status_code, headers = @sling.post_authorizables_with_http_info(
      authorizable_id = 'somegroup',
      intermediate_path = '/home/groups/s',
      {
        :create_group => '',
        :profilegiven_name => 'somegroup'
      }
    )
    expect(status_code).to eq(201)

    @authorizable_id = find_authorizable_id(@sling, '/home/groups/s', 'somegroup')

  end

  after do
  end

  describe 'test group create' do

    it 'should succeed existence check' do
      begin
        data, status_code, headers = @sling.get_node_with_http_info(
          path = 'home/groups/s',
          name = @authorizable_id
        )
        fail
      rescue SwaggerAemClient::ApiError => err
        expect(err.code).to eq(302)
      end
    end

    it 'should succeed permission setting' do
      data, status_code, headers = @cq.post_cq_actions_with_http_info(
        authorizable_id = 'somegroup',
        changelog = 'path:/etc/replication,read:true,modify:true'
      )
      expect(status_code).to eq(200)
    end

    it 'should succeed being added to another group' do

      # ensure member group doesn't exist prior to testing
      member_authorizable_id = find_authorizable_id(@sling, '/home/groups/s', 'somemembergroup')
      if member_authorizable_id
        data, status_code, headers = @sling.delete_node_with_http_info(
          path = 'home/groups/s',
          name = member_authorizable_id
        )
        expect(status_code).to eq(204)
      end

      # create member group
      data, status_code, headers = @sling.post_authorizables_with_http_info(
        authorizable_id = 'somemembergroup',
        intermediate_path = '/home/groups/s',
        {
          :create_group => '',
          :profilegiven_name => 'somemembergroup'
        }
      )
      expect(status_code).to eq(201)

      # add member group to the main group
      data, status_code, headers = @sling.post_node_rw_with_http_info(
        path = 'home/groups/s',
        name = @authorizable_id,
        {
          :add_members => 'somemembergroup'
        }
      )
      expect(status_code).to eq(200)

    end

  end
end
