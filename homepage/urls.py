from django.urls import path, include
from homepage.views import Home, Detail, RoomView, create_room, create_message
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('<int:pk>', Detail.as_view(), name='detail'),
    path('room/<int:pk>', RoomView.as_view(), name='room_detail'),
    path('room', create_room, name='create_room'),
    path('message/<int:room_id>', create_message, name='message'),

]
