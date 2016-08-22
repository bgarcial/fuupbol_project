from django.shortcuts import render

from rest_framework import viewsets
from .serializers import (FieldSerializer, TrainingCompetitionCenterSerializer, TeamSerializer)
from .models import Field, TrainingCompetitionCenter, Team

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

class TrainingCompetitionCenterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TrainingCompetitionCenter.objects.all()
    serializer_class = TrainingCompetitionCenterSerializer