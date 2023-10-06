from django.urls import re_path
from .consumers import ChatAsyncConsumer, Chat2SyncConsumer

app_name = "channels"

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatAsyncConsumer.as_asgi(), name="chat"),
    re_path(r'ws/chat2/(?P<room_name>\w+)/$', Chat2SyncConsumer.as_asgi(), name="chat2")
]