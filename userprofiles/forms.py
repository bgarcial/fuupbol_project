from django import forms
from django.contrib.auth.forms import (UserChangeForm,UserCreationForm)

from .models import User

# Django use special forms to create and edit UserAdmin forms
# due to these was thinked only for the django original user model
# and here  we are using a custom django user model with Abstract
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        widgets = {
            'sex': forms.RadioSelect,
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User