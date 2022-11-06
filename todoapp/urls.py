from django.contrib import admin
from django.urls import path
from todoapp import views


urlpatterns = [
    path('', views.home ,name='home'),
    path('task',views.task,name='task'),
    path('task/<list_id>', views.delete,name='delete'),
]
