
from .models import Field, TrainingCompetitionCenter, Team, Match
from rest_framework import serializers
from userprofiles.serializers import UserSerializer

class FieldSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name='field-list',)

    class Meta:
        model = Field
        fields = ('url', 'id','name','field_type','modality','photo','location')

        #depth = 1

class TeamSerializer(serializers.ModelSerializer):


    #players=UserSerializer(many=True)
    #place_origin = serializers.StringRelatedField()

    '''
    def setup_eager_loading(queryset):
       queryset = queryset.prefetch_related('players',)
       queryset = queryset.select_related('place_origin',)
    '''

    class Meta:
        model = Team
        fields = ('url','name','image','players','modality','place_origin','game_day',)
        #depth = 1

class TrainingCompetitionCenterSerializer(serializers.HyperlinkedModelSerializer):
    fields = FieldSerializer(many=True)

    def setup_eager_loading(queryset):
       queryset = queryset.prefetch_related('fields',)

    class Meta:
        model = TrainingCompetitionCenter
        fields = ('url','id', 'name', 'location','fields','owner',)


class MatchSerializer(serializers.ModelSerializer):

    #field = serializers.StringRelatedField()
    #field=FieldSerializer()
    #field=serializers.HyperlinkedIdentityField(view_name='field-detail')
    field = serializers.SlugRelatedField(queryset=Field.objects.all(),slug_field='name')
    #home_team = serializers.StringRelatedField()
    #away_team = serializers.StringRelatedField()


    '''
    def setup_eager_loading(queryset):
        queryset = queryset.select_related('field','home_team','away_team',)
    '''

    class Meta:
        model = Match
        fields = ('url','id','home_team', 'away_team','field','match_date', 'check_match_away_team','status_challenge')
        #depth=1
