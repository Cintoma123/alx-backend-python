from rest_framework import viewsets
from .models import Users, Message , Conversation
from .serializers import Users, MessageSerializer, ConversationSerializer


# Create your views here.
class ConservationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
     

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

