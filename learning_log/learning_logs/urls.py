from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]