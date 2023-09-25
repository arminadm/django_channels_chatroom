from django.urls import path
from .views import IndexView, RoomView


app_name = "website"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("chat/<str:room_name>/", RoomView.as_view(), name="room"),
]
