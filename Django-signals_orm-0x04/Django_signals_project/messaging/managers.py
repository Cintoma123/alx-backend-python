from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import Message , Notification , User

class UnreadMessageManager(models.Manager):
    '''
    Custom manager for Message model to handle unread messages and counts.'''
    def for_user(self):
        return super(UnreadMessagesManager, self).get_queryset().filter(active=True)
'''
    Returns a queryset of unread messages for the recipient.'''
    def unread_count(self):
        return self.objects.filter(recipient=self.recipient, read=False).count()
    def unread_messages(self):
        return self.objects.filter(recipient=self.recipient, read=False)

    def mark_as_read(self, message_id):
        return self.filter(id=message_id).update(read=True)
    
        # Create message your models here.
class Message(models.Model):
    sender = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    content = models.TextField()
    read = models.BooleanField(default=False)  # Add this field
    timestamp = models.DateTimeField(auto_now_add=True)
    parent_message = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    objects = UnreadMessageManager()
    active_object = UnreadMessageManager()
    Message.active_objects.all()
    
    Message.active_objects.count()

    def __str__(self):
        return f"Message from {self.sender} to {self.recipient} at {self.timestamp}"
        # Get all unread messages for a user with username 'john'
    unread_messages = Message.unread.for_user('john')
