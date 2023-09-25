from django.shortcuts import render
from django.views import View


# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, "chat/index.html")
    

class RoomView(View):
    def get(self, request, room_name):
        return render(request, "chat/room.html", {
            "room_name": room_name
        })