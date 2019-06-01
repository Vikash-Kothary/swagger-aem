package com.shinesolutions.swaggeraem4j;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

import com.shinesolutions.swaggeraem4j.api.CqApi;

public class AemTest {

	private CqApi cq;

	@Before
	public void init() {
		cq = TestHelper.createCqApi();
	}

	@Test
	public void testGetLoginPage() throws ApiException {
		ApiResponse<String> response = cq.getLoginPageWithHttpInfo();
		assertEquals(200, response.getStatusCode());
    assertTrue(response.getData().contains("QUICKSTART_HOMEPAGE"));
	}

}
