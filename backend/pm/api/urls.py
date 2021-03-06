from django.conf.urls import url
from django.urls import include
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    url(r'^$', get_schema_view()),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/token/obtain/$', TokenObtainPairView.as_view()),
    url(r'^auth/token/refresh/$', TokenRefreshView.as_view()),
    url(r'^echo/$', EchoView.as_view()),
    url(r'^create/$', CreateView.as_view(), name="create"),
]
