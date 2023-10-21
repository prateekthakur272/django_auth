from django.urls import path
from .views import login, register
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', register),
    path('login/', obtain_auth_token),
]