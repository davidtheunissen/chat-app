from django.urls import path

from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('<slug:room_name>/', views.room, name='room'),
]