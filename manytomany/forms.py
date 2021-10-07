from django import forms

from .models import User_Team

class CreateUserTeamForm(forms.ModelForm):
    class Meta:
        model = User_Team
        fields = ['team']
