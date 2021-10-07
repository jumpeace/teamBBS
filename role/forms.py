from django import forms

from .models import Role

class CreateRoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name']
