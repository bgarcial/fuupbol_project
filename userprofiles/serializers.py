from __future__ import unicode_literals
from django.db import models
from .models import User
from rest_framework import serializers, status
from rest_framework.exceptions import APIException

# Serializers define the API representation
# Expose the model and their fields


class UserSerializer(serializers.ModelSerializer):
    username = models.CharField()

    '''
    def setup_eager_loading(queryset):
      queryset = queryset.select_related('team',)
    '''
    # http://stackoverflow.com/questions/27586095/why-isnt-my-django-user-models-password-hashed/27586289

    # override perform_update and perform_create and comparision with
    # DRF 2.o version http://stackoverflow.com/questions/27468552/changing-serializer-fields-on-the-fly/#answer-27471503

    # Perform update can be useful when is necessary some actions
    # after or before save an object
    # http://stackoverflow.com/questions/31819156/how-to-create-a-django-user-with-django-rest-framework-drf-3
    # view save and deletion hooks http://www.django-rest-framework.org/api-guide/generic-views/#genericapiview

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


    class Meta:
        model = User
        fields = ('url', 'username', 'password', 'first_name','last_name',
                  'age', 'sex', 'photo', 'email', 'is_player', 'team',
                  'position', 'is_staff', 'is_active', 'is_superuser',
                  'is_player', 'weight', 'height', 'nickname',
                  'number_matches', 'accomplished_matches',
                  'time_available', 'leg_profile', 'number_shirt_preferred',
                  'team_support', 'player_preferred', 'last_login',
        )

        # depth=1



