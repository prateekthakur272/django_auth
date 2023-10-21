from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.authtoken.views import obtain_auth_token

User = get_user_model()

@api_view(['POST'])
def login(request, *args, **kwargs):
    data = JSONParser().parse(request)
    user = get_object_or_404(User, username=data['username'])
    user_serializer = UserSerializer(user)
    return JsonResponse(user_serializer.data)

@api_view(['POST'])
def register(request, *args, **kwargs):
    data = JSONParser().parse(request)
    user_serializer = UserSerializer(data=data)
    if(user_serializer.is_valid()):
        user_serializer.save()
        user = User.objects.get(username=data['username'])
        try:
            user.set_password(data['password'])
            user.save()
        except KeyError:
            user.delete()
            return JsonResponse({"password":["This field is required"]})
        return JsonResponse(user_serializer.data)
    return JsonResponse(user_serializer.errors)