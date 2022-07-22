from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


urlpatterns = [
    path('', include('ModelApi.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
