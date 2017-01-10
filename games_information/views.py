from django.shortcuts import render

from rest_framework import viewsets
from .serializers import (FieldSerializer, TeamSerializer, MatchSerializer)
from .models import Field, Team, Match

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
    #lookup_value_regex = '[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}'
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_fields = ('name', 'players', 'category', 'game_day', 'place_origin',)
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
class TrainingCompetitionCenterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TrainingCompetitionCenter.objects.all()
    serializer_class = TrainingCompetitionCenterSerializer
'''


class MatchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    filter_fields = ('home_team','away_team', 'status_challenge', 'fichaje_players_match', )
