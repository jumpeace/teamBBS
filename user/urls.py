from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_, name='login'),
    path('logout/', views.logout_, name='logout'),
    path('delete/', views.delete, name='delete'),
]