from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import User

import re

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    email = forms.EmailField(max_length=255)

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        # ASK 肯定先読み, 後方参照
        if not re.search(r'.{8,32}', password1):
            raise forms.ValidationError("パスワードは8文字以上32文字以下にしてください")
        if not re.search(r'(?=.*[a-z]).+', password1):
            raise forms.ValidationError("パスワードにアルファベット小文字を1文字以上含んでください")
        if not re.search(r'(?=.*[A-Z]).+', password1):
            raise forms.ValidationError("パスワードにアルファベット大文字を1文字以上含んでください")
        if not re.search(r'(?=.*\d).+', password1):
            raise forms.ValidationError("パスワードは数字を1文字以上含んでください")
        if re.search(r'(.)\1\1', password1):
            raise forms.ValidationError("文字を3回以上繰り返さないでください")
        if re.search(r'(.{2,})\1', password1):
            raise forms.ValidationError("2文字以上の文字列を2回以上繰り返さないでください")
        return password1

    def clean_email(self):
        email = self.cleaned_data['email'].lower()

        try:
            user = User.objects.get(email=email)
            if not user:
                raise forms.ValidationError(f"{email} が存在しません")
        except Exception as e:
            return email
        raise forms.ValidationError(f"{email} はすでに使われています")



class AuthUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'password')


    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email'].lower()
            user = User.objects.get(email=email)
            if not user:
                raise forms.ValidationError(f"{email} が存在しません")

            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("パスワードが違います")

