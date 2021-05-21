from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiVew(APIView):
    """Test APIView"""

    def get(self, reques, format=None):
        """Returns a list of APIView Features"""

        an_apiview=[
        'Uses HTTP Methods as functions ("get, "post", "put", "patch", "delete")',
        'Is similar to traditional Django View',
        'Gives you the most control over your app logic',
        'is mapped manually to URLs'
        ]

        return Response({'message' : 'Hello!', 'an_apiview':an_apiview})
