from __future__ import unicode_literals
from django.db import models
from .models import User
from rest_framework import serializers, status
from rest_framework.exceptions import APIException

# Serializers define the API representation
# Expose the model and their fields


class UserSerializer(serializers.ModelSerializer):
    #username = models.CharField()

    '''
    def setup_eager_loading(queryset):
      queryset = queryset.select_related('team',)
    '''
    # http://stackoverflow.com/questions/27586095/why-isnt-my-django-user-models-password-hashed/27586289
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


    '''
    # http://stackoverflow.com/questions/28389321/django-rest-framework-not-encrypting-passwords-when-being-logged-into-the-datab
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            age=validated_data['age'],
            sex=validated_data['sex'],
            photo=validated_data['photo'],
            is_player=validated_data['is_player'],
            team=validated_data['team'],
            position=validated_data['position'],
            is_staff=validated_data['is_staff'],
            is_active=validated_data['is_active'],
            is_superuser=validated_data['is_superuser'],
            weight=validated_data['weight'],
            height=validated_data['height'],
            nickname=validated_data['nickname'],
            number_matches=validated_data['number_matches'],
            accomplished_matches=validated_data['accomplished_matches'],
            time_available=validated_data['time_available'],
            leg_profile=validated_data['leg_profile'],
            number_shirt_preferred=validated_data['number_shirt_preferred'],
            team_support=validated_data['team_support'],
            player_preferred=validated_data['player_preferred'],
            last_login=validated_data['last_login'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    '''

    class Meta:
        model = User
        fields = ('url', 'username', 'password', 'first_name','last_name',
                  'age', 'sex', 'photo', 'email', 'is_player', 'team',
                  'position', 'is_staff', 'is_active', 'is_superuser',
                  'is_player', 'weight', 'height', 'nickname',
                  'number_matches', 'accomplished_matches',
                  'time_available', 'leg_profile', 'number_shirt_preferred',
                  'team_support', 'player_preferred', 'last_login',)

        # depth=1


class NameDuplicationError(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = u'Duplicate Username'
