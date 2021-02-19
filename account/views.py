from django.contrib.auth.models import User
from django.http import request
from django.http.response import JsonResponse
from rest_framework import generics, permissions, serializers
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, ModeratorSerializer
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from .models import Moderator
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

def showUsers(request):
    if request.method =='GET':
        user= User.objects.all()
        serializer= UserSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def moderatorRead(request):
    if request.method =='GET':
        moderator=Moderator.objects.all()
        serializar = ModeratorSerializer(moderator, many=True)
        return JsonResponse(serializar.data, safe=False)
    elif request.method =='POST':
        data= JSONParser().parse(request)
        serializar=ModeratorSerializer(data=data)
        if serializar.is_valid():
            serializar.save()
            return JsonResponse(serializar.data, status=201)
        return JsonResponse(serializar.errors, status=400)
