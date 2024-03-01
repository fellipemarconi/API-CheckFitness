from django.urls import path, include


urlpatterns = [
    path('', include('apps.core.api.urls')),
]