from django import forms
from django.contrib.auth.forms import (UserChangeForm,UserCreationForm)

from .models import User
#from checkboxselectmultiple.widgets import CheckboxSelectMultiple

# Django use special forms to create and edit UserAdmin forms
# due to these was thinked only for the django original user model
# and here  we are using a custom django user model with Abstract
class CustomUserChangeForm(UserChangeForm):

    position = forms.MultipleChoiceField(
        label='Posición en la que juega',
        widget=forms.CheckboxSelectMultiple(),
        choices=User.POSITION_CHOICES, initial=None)

    class Meta(UserChangeForm.Meta):
        model = User
        widgets = {
            'sex': forms.RadioSelect,
            #'position': CheckboxSelectMultiple,
        }
        fields= ('position',)

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
