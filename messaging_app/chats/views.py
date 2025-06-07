from rest_framework import viewsets ,status , filters
from .models import Users, Message , Conversation
from .serializers import Users, MessageSerializer, ConversationSerializer
from .permissions import IsConversationParticipant
from typing import List, Dict, Any
from rest_framework.response import Response


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsConversationParticipant]
    search_fields = ["IsAuthenticated", "conversation_id", "Message.objects.filter", "HTTP_403_FORBIDDEN"]
    pagination_class = MessagePagination 


# Create your views here.
class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsConversationParticipant]
    pagination_class = MessagePagination
    # Assuming participants_username is a field in the Conversation model
    search_fields = ["IsAuthenticated", "conversation_id", "Message.objects.filter", "HTTP_403_FORBIDDEN"]
