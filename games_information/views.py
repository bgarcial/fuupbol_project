from django.shortcuts import render

from rest_framework import viewsets, generics
from .serializers import (FieldSerializer, TeamSerializer, MatchSerializer)
from .models import Field, Team, Match
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


class FieldViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Field.objects.all()
    serializer_class = FieldSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    #lookup_field = 'name'
    lookup_value_regex = '[\w.ñ@+-]+'
    #lookup_value_regex = '[\d\/. ()\-+]+'
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_fields = ('name', 'branch', 'category', 'game_day', 'place_origin',)
    # lookup_field = 'slug_name'
    # if Team.category != "":
    #    print("The categoryssss is:",Team.category)
    '''
    def list(self, request):
        """GET - Show all users"""
        print (request.version)
        api_result = team_list.lists_all_teams()
        return Response(api_result)
    '''
    '''
    def get_queryset(self):
        team = self.kwargs['team']
        return User
    '''

'''
class ListCreateMatch(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    filter_fields = ('home_team','away_team', 'status_challenge', 'fichaje_players_match', )
'''


class MatchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    filter_fields = ('home_team','away_team', 'status_challenge',
        'fichaje_players_match', )

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super(MatchViewSet, self).update(request, *args, **kwargs)



