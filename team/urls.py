from django.urls import path, include
from .views import team_view

app_name = 'team'
urlpatterns = [
    # チーム自体
    path('', team_view.List.as_view(), name='list'),
    path('create/', team_view.Create.as_view(), name='create'),
    path('user/create', team_view.user.Create.as_view(), name='user_create'),
    path('<int:team_id>/', team_view.Detail.as_view(), name='detail'),
    path('<int:team_id>/update/', team_view.update, name='update'),
    path('<int:team_id>/delete/', team_view.delete, name='delete'),
    path('<int:team_id>/user/', team_view.user.List.as_view(), name='user_list'),
    path('<int:team_id>/user/delete', team_view.user.delete, name='user_delete'),

    path('<int:team_id>/channel/', include('channel.urls')),
    path('<int:team_id>/role/', include('role.urls')),
]