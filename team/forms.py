from django import forms

from .models import Team
from manytomany.models import User_Team

class CreateTeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']        

