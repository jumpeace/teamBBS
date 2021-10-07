from django.urls import path, include
from .views import role_view

app_name = 'role'
urlpatterns = [
    path('', role_view.List.as_view(), name='list'),
    path('create/', role_view.Create.as_view(), name='create'),
    path('<int:role_id>/', role_view.Detail.as_view(), name='detail'),
    path('<int:role_id>/update/', role_view.update, name='update'),
    path('<int:role_id>/delete/', role_view.delete, name='delete'),

    path('<int:role_id>/user/', role_view.user.List.as_view(), name='user_list'),
    path('<int:role_id>/user/create/', role_view.user.create, name='user_create'),
    path('<int:role_id>/user/delete/', role_view.user.delete, name='user_delete'),
]
