from django.urls import path, include
from .views import channel_view

app_name = 'channel'
urlpatterns = [
    path('', channel_view.List.as_view(), name='list'),
    path('create/', channel_view.Create.as_view(), name='create'),
    path('<int:channel_id>/', channel_view.Detail.as_view(), name='detail'),
    path('<int:channel_id>/update', channel_view.update, name='update'),
    path('<int:channel_id>/delete', channel_view.delete, name='delete'),
    path('<int:channel_id>/post/', include('post.urls')),
]