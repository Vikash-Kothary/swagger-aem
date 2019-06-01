require_relative 'spec_helper'

describe 'Repository' do
  before do
    init_client
    @console = SwaggerAemClient::ConsoleApi.new
  end

  after do
  end

  describe 'test block repository writes' do

    it 'should succeed' do
      data, status_code, headers = @console.post_jmx_repository_with_http_info(
        action = 'blockRepositoryWrites'
      )
      expect(status_code).to eq(200)
    end

  end

  describe 'test unblock repository writes' do

    it 'should succeed' do
      data, status_code, headers = @console.post_jmx_repository_with_http_info(
        action = 'unblockRepositoryWrites'
      )
      expect(status_code).to eq(200)
    end

  end

end
