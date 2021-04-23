from django import forms
from .models import Groups

class NewGroupForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ['name_of_group', 'members']


