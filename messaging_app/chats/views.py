from rest_framework import viewsets ,status , filters
from .models import Users, Message , Conversation
from .serializers import Users, MessageSerializer, ConversationSerializer


# Create your views here.
class ConservationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [filters.SearchFilter]
    earch_fields = ['participants_username']

     

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['message_body']

