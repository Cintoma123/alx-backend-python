from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
.models import Message, Notification, User
from .serializers import MessageSerializer, NotificationSerializer, UserSerializer
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

# Create your views here.
class delete_user(APIView):
    def delete(self,request, user_id):
        try:
            user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
                user.delete()
                return Response({"message": "User deleted successfully"}, status=status.HTTP_284_NO_CONTENT)

messages = (Message.object.fliter(parent_mesage__isnull =True)
.select_related('sender','recipient')
.prefetch_related('replies')
)
for msg in messages:
     print(f"From: {msg.sender.username}, To: {msg.recipient.username}, Message: {msg.content}")
  for reply in msg.replies.all()
      print(f'Reply:{reply.content}')


def get_threaded_replies(message):
    replies = message.replies.all()
    result = []
    for reply in replies:
        # Each reply is a dict with the reply and its own replies
        result.append({
            'reply': reply,
            'children': get_threaded_replies(reply)
        })
    return result

class MessageThreadView(APIView):
    def get(self, request, message_id):
        message = get_object_or_404(Message, id=message_id)
        thread = get_threaded_replies(message)
        data = {
            'message': MessageSerializer(message).data,
            'thread': self.serialize_thread(thread)
        }
        return Response(data)

    def serialize_thread(self, thread):
        # Recursively serialize the thread for JSON response
        result = []
        for item in thread:
            result.append({
                'reply': MessageSerializer(item['reply']).data,
                'children': self.serialize_thread(item['children'])
            })
        return result

class UnreadInboxView(APIView):
        unread = UnreadMessageManager()
    def get(self, request, username):
        unread_messages = Message.unread.for_user(username).only('id','sender','recipient' ,'read','timestamp')
        serializer = MessageSerializer(unread_messages, many=True)
        return Response(serializer.data)

@method_decorator(cache_page(60), name='dispatch')  # 60 seconds cache
class MessageThreadView(APIView):
    def get(self, request, conversation_id):
        """
        Retrieve all messages in a conversation.
        """
    # ... your get method ...
messages = Message.objects.filter(conversation_id=conversation_id).order_by('timestamp')
content = []
for msg in messages:
    content.append({
        "sender": msg.sender,
        "body": msg.content,
        "timestamp": msg.timestamp,
    })
return Response(content , status=status.HTTP_200_OK)     