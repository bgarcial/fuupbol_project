from django.contrib import admin
from .models import Field, Team
# Register your models here.

@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('id','name','location','field_type','modality',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','name','image','modality','place_origin', 'game_day')
