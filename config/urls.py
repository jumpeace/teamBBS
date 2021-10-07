from django.urls import include, path

from django.contrib import admin
from index.views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('team/', include('team.urls')),
    path('django/user/', include('django.contrib.auth.urls')),
]
