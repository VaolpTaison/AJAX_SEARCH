from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from rooms import views

urlpatterns = [
    path('', views.search, name='search')
]