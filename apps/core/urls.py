from django.urls import include, path
from apps.core.views import home

urlpatterns = [
    path('', home, name='home'),
]