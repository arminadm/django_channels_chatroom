from rest_framework import serializers
from website.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields= ['__str__', 'content', 'timestamp']