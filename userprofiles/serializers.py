from .models import User
from rest_framework import serializers

# Serializers define the API representation
# Expose the model and their fields
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username','password','first_name','last_name','age','sex', 
        'photo','email','is_player','position','is_staff','is_active','is_superuser',
        'is_player','weight','nickname','number_matches','accomplished_matches',
        'time_available','leg_profile','number_shirt_preferred','team_support',
        'player_preferred','last_login',)

