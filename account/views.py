from django.contrib.auth.models import User
from django.http import request
from django.http.response import HttpResponse, JsonResponse
from rest_framework import generics, permissions, serializers
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, ModeratorSerializer, StagesSerializer, EventsSerializer
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from .models import Moderator, Stage, Event
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

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

def oneUser(request):
    if request.user.is_authenticated:
        current_user= request.user
        user= User.objects.get(id=current_user.id)
        serializer= UserSerializer(user)
        return JsonResponse(serializer.data, safe=False)
    
def deleteModerator(request,pk):
    moderator= Moderator.objects.get(id=pk)
    moderator.delete()
    return HttpResponse(status=200)

def deleteUser(request,pk):
    user= User.objects.get(id=pk)
    user.delete()
    return HttpResponse(status=200)

def switchModerator(request,pk):
    moderator= Moderator.objects.get(id=pk)

    user = User.objects.create_user(moderator.username, moderator.email, moderator.password,first_name=moderator.first_name, last_name=moderator.last_name, is_staff=True)
    user.save()
    moderator.delete()
    return HttpResponse(status=200)

@csrf_exempt
def eventRead(request):
    if request.method =='GET':
        event=Event.objects.all()
        serializar = EventsSerializer(event, many=True)
        return JsonResponse(serializar.data, safe=False)
    elif request.method =='POST':
        data= JSONParser().parse(request)
        serializar=EventsSerializer(data=data)
        if serializar.is_valid():
            serializar.save()
            return JsonResponse(serializar.data, status=201)
        return JsonResponse(serializar.errors, status=400)

@csrf_exempt
def stageRead(request):
    if request.method =='GET':
        stage=Stage.objects.all()
        serializar = StagesSerializer(stage, many=True)
        return JsonResponse(serializar.data, safe=False)
    elif request.method =='POST':
        data= JSONParser().parse(request)
        serializar=StagesSerializer(data=data)
        if serializar.is_valid():
            serializar.save()
            return JsonResponse(serializar.data, status=201)
        return JsonResponse(serializar.errors, status=400)

def oneEvent(request,pk):
    event= Event.objects.get(id=pk)
    serializer= EventsSerializer(event)
    return JsonResponse(serializer.data, safe=False)

def deleteEvent(request,pk):
    if request.user.is_authenticated:
        event= Event.objects.get(id=pk)
        event.delete()
        return HttpResponse(status=200)

'''
@csrf_exempt
def updateEvent(request,pk):
    if request.user.is_authenticated:
        event= Event.objects.get(id=pk)
        data= JSONParser().parse(request)
        serializar=EventsSerializer(event,data=data)
        if serializar.is_valid():
            serializar.update()
            return JsonResponse(serializar.data, status=201)
        return JsonResponse(serializar.errors, status=400)
    return HttpResponse(status=200)
'''

class EventFilter(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category']
       

