from django.urls import path, re_path
from .consumers import ChatAsyncConsumer

app_name = "channels"

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatAsyncConsumer.as_asgi(), name="chat")
]