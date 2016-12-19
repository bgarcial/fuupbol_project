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
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_fields = ('name','players','game_day','place_origin',)

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
    filter_fields = ('home_team','away_team', 'status_challenge',)
