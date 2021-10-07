from django.urls import path
from .views import post_view

app_name = 'post'
urlpatterns = [
    path('', post_view.List.as_view(), name='list'),
    path('create/', post_view.create, name='create'),
    path('<int:post_id>/', post_view.Detail.as_view(), name='detail'),
    path('<int:post_id>/update/', post_view.update, name='update'),
    path('<int:post_id>/delete/', post_view.delete, name='delete'),
]
