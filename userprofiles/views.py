from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import filters
#from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

# from rest_framework.response import Response
# from django.contrib.auth.hashers import make_password

# Viewsets define the behavior of the view


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    lookup_value_regex = '[\w.ñ@+-]+'
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    filter_fields = ('email', 'username', 'is_player', 'first_name',
        'last_name', 'team', 'nickname')

    '''
    def perform_create(self, serializer):
        hashed_password = make_password(serializer.validated_data['password']) # get the hashed password
        serializer.validated_data['password'] = hashed_password
        user = super(UserViewSet, self).perform_create(serializer) # create a user

    def perform_update(self, serializer):
        hashed_password = make_password(serializer.validated_data['password']) # get the hashed password
        serializer.validated_data['password'] = hashed_password
        user = super(UserViewSet, self).perform_update(serializer) # create a user
    '''

