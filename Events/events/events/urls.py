from django.contrib import admin
from eventTest import views
from django.urls import path
from django.urls import include
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'events', views.EventsViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace="rest_framework")),

]
