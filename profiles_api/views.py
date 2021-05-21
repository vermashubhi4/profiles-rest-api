from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiVew(APIView):
    """Test APIView"""

    serializers_class = serializers.HelloSerializer

    def get(self, reques, format=None):
        """Returns a list of APIView Features"""

        an_apiview=[
        'Uses HTTP Methods as functions ("get, "post", "put", "patch", "delete")',
        'Is similar to traditional Django View',
        'Gives you the most control over your app logic',
        'is mapped manually to URLs'
        ]

        return Response({'message' : 'Hello!', 'an_apiview':an_apiview})

    def post(self, request):
        """Creates a hello message with our name"""
        serialiser = self.serializers_class(data = request.data)

        if(serialiser.is_valid()):
            name = serialiser.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})

        return Response(serialiser.errors,
        status = status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handle updating an Object"""
        return Response({'method':'PUT'})

    def patch(self, request,pk=None):
        """Update only a part of object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Deletes an Object"""
        return Response({'method':'DELETE'})
