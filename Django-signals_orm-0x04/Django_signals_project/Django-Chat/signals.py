from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import Message , Notification , User

@receiver(pre_save, sender=Message)
def log_old_message_content(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_message = Message.objects.get(pk=instance.pk):
            print(f"Old message content: {old_message.content}")
            MessageHistory.objects.create(
                message=old_message,
                old_content=old_message.content,
                changed_by=old_message.sender
            )
        except Message.DoesNotExist:
            print("This is a new message, no old content to log.")
        else:
            print(f"Pre-save signal triggered for message: {instance}")
