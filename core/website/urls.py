from django.urls import path
from django.contrib.auth.views import LoginView
from .views import (
    IndexView, RoomView,
    index2, room2
)

app_name = "website"

urlpatterns = [
    # chat room 2: does have database
    path("", index2, name="index2"),
    path("chat2/<str:room_name>/", room2, name="room2"),
    path('login', LoginView.as_view(template_name='chat2/login.html'), name="login"),
    
    # chat room 1: no database
    path("chat/", IndexView.as_view(), name="index"),
    path("chat/<str:room_name>/", RoomView.as_view(), name="room"),
]
