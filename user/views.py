from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.views import (
    PasswordChangeView, 
    PasswordChangeDoneView,
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView, 
    PasswordResetCompleteView
)
from django.urls import reverse

from .apis_write import *

from .models import User

from .forms import CreateUserForm, AuthUserForm

from props.user import props
from django.contrib.auth.mixins import LoginRequiredMixin

def register(request):
    user = request.user

    if user.is_authenticated:
        return redirect('index')

    context = {
        'props': props.register,
    }

    if request.method != 'POST':
        return render(request, "page/form.html", context)


    form = CreateUserForm(request.POST)

    if not form.is_valid():
        context['form'] = form
        return render(request, "page/form.html", context)

    form.save()

    user = User.objects.get(email=request.POST['email'])

    # ログイン処理
    login(request, user, backend='user.backends.AuthUserBackend')

    # 成功
    return redirect('index')


def login_(request):

    user = request.user

    if user.is_authenticated:
        return redirect('index')

    context = {
        'props': props.login,
    }

    if request.method != 'POST':
        return render(request, "page/form.html", context)

    form = AuthUserForm(request.POST)

    if not form.is_valid():
        context['form'] = form
        return render(request, "page/form.html", context)

    email = request.POST['email']
    password = request.POST['password']
    
    user = authenticate(email=email, password=password)

    login(request, user)

    # 成功
    return redirect('index')


def logout_(request):
    user = request.user

    if not user.is_authenticated:
        # 元のページに戻る
        return redirect("index")

    logout(request)

    return redirect("index")


def delete(request):
    user = request.user

    if not user.is_authenticated:
        return redirect('index')

    context = {
        'props': props.delete,
    }

    if request.method != 'POST':
        return render(request, 'page/form.html', context)

    user.delete()

    return redirect('index')
