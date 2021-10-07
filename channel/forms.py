from django import forms
from .models import Channel

class CreateChannelForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = ['name']

    # TODO チーム内で同じチャンネル名を禁止する
