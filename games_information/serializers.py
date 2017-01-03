
from .models import Field,  Team, Match
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
    place_origin = serializers.SlugRelatedField(queryset=Field.objects.all(),slug_field='name')

    '''
    def setup_eager_loading(queryset):
       queryset = queryset.prefetch_related('players',)
       queryset = queryset.select_related('place_origin',)
    '''

    class Meta:
        model = Team
        fields = ('url', 'name', 'image', 'players', 'modality', 'branch',
            'category', 'enterprise_name', 'town_name', 'university_name',
            'school_name', 'place_origin', 'game_day',)
        # depth = 1
'''
class TrainingCompetitionCenterSerializer(serializers.HyperlinkedModelSerializer):
    fields = FieldSerializer(many=True)

    def setup_eager_loading(queryset):
       queryset = queryset.prefetch_related('fields',)

    class Meta:
        model = TrainingCompetitionCenter
        fields = ('url','id', 'name', 'location','fields','owner',)
'''


class MatchSerializer(serializers.ModelSerializer):

    # field = serializers.StringRelatedField()
    # field=FieldSerializer()

    # field = serializers.StringRelatedField() name pero no escribible
    # field=FieldSerializer() url solo
    # field=serializers.HyperlinkedIdentityField(view_name='field-detail')
    field = serializers.SlugRelatedField(queryset=Field.objects.all(),slug_field='name')
    # http://stackoverflow.com/questions/28689281/what-is-the-read-write-equivalent-of-serializers-stringrelatedfield
    # http://www.django-rest-framework.org/api-guide/relations/#slugrelatedfield


    '''
    def setup_eager_loading(queryset):

        queryset = queryset.prefetch_related('field',)


        queryset = queryset.select_related('field','home_team','away_team',)
    '''
    class Meta:
        model = Match
        fields = ('url', 'id', 'home_team', 'away_team','field','match_date',
            'check_match_away_team', 'status_challenge', 'home_team_players_accept', 'away_team_players_accept', 'home_team_players_cancel', 'away_team_players_cancel', 'fichaje_players_match',)
        #depth=1
