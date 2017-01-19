from .models import User
from rest_framework import serializers

'''
class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension
'''

# Serializers define the API representation
# Expose the model and their fields


class UserSerializer(serializers.ModelSerializer):
    # team = serializers.StringRelatedField()
    '''
    photo = Base64ImageField(
        max_length=None, use_url=True,
    )
    '''

    '''
    def setup_eager_loading(queryset):
      queryset = queryset.select_related('team',)
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
