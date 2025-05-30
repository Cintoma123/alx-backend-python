from rest_framework import serializers
from .models import Users, Message, Conversation

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['name_of_user','Email_of_user','password','is_online']

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ['participants1','participants2','participants','created_at','last_updated']
        Message = MessageSerializer(many=True, read_only=True)  # Nested book serializer


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['sender','conversation','text','timestamp','is_read','is_deleted']