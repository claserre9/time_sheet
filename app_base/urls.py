
from django.urls import path

from app_base import views

urlpatterns = [
    path('',  views.app_base_home, name='app_base_home'),
]