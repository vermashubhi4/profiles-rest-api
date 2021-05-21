from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


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


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializers_class = serializers.HelloSerializer

    def list(self,request):
        """Returns a Hello Msg"""
        a_viewset = [
        'uses actions (list,create,retieve, update,partial_update,destroy)',
        'Automatically mapsto URLs using routers',
        'provides more functionality with less code'
        ]

        return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self,request):
        """Creates a new hello msg"""
        serialiser = self.serializers_class(data=request.data)
        if(serialiser.is_valid()):
            name = serialiser.validated_data.get('name')
            message=f'Hello {name}!'
            return Response({'message':message})

        return Response(serialiser.errors,
        status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """Returns a specific object"""
        return Response({'message':"GET"})

    def update(self,request,pk=None):
        """Updates the complete Object"""
        return Response({'message':"PUT"})

    def partial_update(self,request,pk=None):
        """Updates the requested resource"""
        return Response({'message':"PATCH"})

    def destroy(self,request,pk=None):
        """Deletes the requested resource"""
        return Response({'message':"DELETE"})



class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    
