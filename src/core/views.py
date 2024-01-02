from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


class Health(APIView):
    """Health Check"""

    def get(self, _: Request) -> Response:
        # return healthy response
        return Response(
            data={
                "status": "healthy",
            },
            status=status.HTTP_200_OK,
        )
