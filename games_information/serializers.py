from .models import Field, TrainingCompetitionCenter, Team
from rest_framework import serializers

class FieldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Field
        fields = ('url','id', 'name','field_type','modality','photo','location')
        depth = 1

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('url','name','image','players','modality','place_origin','game_day',)
        depth = 1

class TrainingCompetitionCenterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrainingCompetitionCenter
        fields = ('url','id', 'name', 'location','owner',)
        depth = 1