from django.contrib import admin
from .models import Field, Team, Match, TrainingCompetitionCenter
# Register your models here.

@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('id','name','location','field_type','modality',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','image','modality','place_origin', 'game_day')

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('id','home_team','away_team','field', 'match_date')

@admin.register(TrainingCompetitionCenter)
class TrainingCompetitionCenterAdmin(admin.ModelAdmin):
    list_display = ('id','name','location', 'owner')
