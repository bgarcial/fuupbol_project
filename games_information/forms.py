from django import forms
from .models import Field, Team



class FieldForm(forms.ModelForm):
    modality = forms.MultipleChoiceField(
        label='Modalidad de juego',
        widget=forms.CheckboxSelectMultiple(),
        choices=Field.MODALITY_CHOICES, initial=None)

    class Meta:
        model = Field
        fields = ('name','field_type','modality','photo','location')


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        widgets = {
            'branch': forms.RadioSelect,
        }

        exclude = ('branch',)
