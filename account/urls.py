from .views import RegisterAPI, oneUser, showUsers, moderatorRead, deleteModerator, switchModerator, deleteUser, eventRead, stageRead, oneEvent, deleteEvent, EventFilter
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/showUsers/', showUsers, name='showUsers'),
    path('api/showModerators/', moderatorRead, name='showUsers'),
    path('api/oneUser/', oneUser, name='oneUser'),
    path('api/deleteModerator/<int:pk>', deleteModerator, name='deleteModerator'),
    path('api/deleteUser/<int:pk>', deleteUser, name='deleteUser'),
    path('api/switchModerator/<int:pk>', switchModerator, name='switchModerator'),
    path('api/showEvents/', eventRead, name='showEvents'),
    path('api/showStages/', stageRead, name='showStages'),
    path('api/oneEvent/<int:pk>', oneEvent, name='oneEvent'),
    path('api/deleteEvent/<int:pk>', deleteEvent, name='deleteEvent'),
   # path('api/updateEvent/<int:pk>', updateEvent, name='updateEvent'),
    path('api/eventFilter/', EventFilter.as_view(), name='eventFilter'),
]
