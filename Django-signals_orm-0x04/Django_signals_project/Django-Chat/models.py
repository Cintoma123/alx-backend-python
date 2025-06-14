from django.db import models
# Create your models here.
class Message(models.Model):
    sender = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    def __str__(self):
        return f"Message from {self.sender} to {self.recipient} at {self.timestamp}"

class MessageHistory(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='history')
    old_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    changed_by = models.CharField(max_length=100)
    def __str__(self):
        return f"History for message {self.message.id} at {self.timestamp}"
