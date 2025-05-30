from django.db import models
from django.contrib.auth.models import AbstractUser
 
# Create your models here.
class Users(AbstractUser):
    '''Model representing a chat in the messaging app.'''
    Name_of_user = models.CharField(max_length=100, unique=True)
    Email_of_user = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100, unique=True)
    is_online = models.EmailField(max_length=100, unique=True)
    bio = models.TextField(blank= True , null= True)
    user_profile = models.ImageField(upload_to='profile/', blank= True , null = True)

    def __str__(self):
        return self.username
    

class Conversation (models.Model):
    '''model representing a conversation in the messaging app.'''
    participant1 = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='participant1')
    participant2 = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='participant2')
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Conversation between {self.participant1.Name_of_user} and {self.participant2.Name_of_user} created at {self.created_at}"


class Message(models.Model):
    '''model representing a message in the messaging app.'''
    sender = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='sender')
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='conversation')
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.sender.Name_of_user} in conversation {self.conversation.id} at {self.timestamp}: {self.text[:20]}..."
