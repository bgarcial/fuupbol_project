from django import forms
from .models import Field

class FieldForm(forms.ModelForm):
    modality = forms.MultipleChoiceField(
        label='Modalidad de juego',
        widget=forms.CheckboxSelectMultiple(),
        choices=Field.MODALITY_CHOICES, initial=None)

    class Meta:
        model = Field
        fields = ('name','field_type','modality','photo','location')
