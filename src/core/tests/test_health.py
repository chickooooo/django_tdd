from rest_framework import status
from rest_framework.test import APIClient, APISimpleTestCase
from rest_framework.response import Response


# create api client
client = APIClient()


class TestHealth(APISimpleTestCase):
    """Test Health Check"""

    def test_get_health(self):
        """Test get request"""

        # make get request to the endpoint
        response: Response = client.get("/api/health/")  # type: ignore

        # assert status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # assert data
        self.assertEqual(response.data, {"status": "healthy"})
