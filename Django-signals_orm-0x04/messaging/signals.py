from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import Message , Notification , User
@receiver(presave, sender=Message)
def pre_save_message(sender, instance, **kwargs):
    print(f"Pre-save signal triggered for message: {instance}")

@receiver(post_save, sender=Message)
def post_save_message(sender, instance, created, **kwargs):
    if created:
        print(f"Post-save signal triggered for new message: {instance}")
    else:
        print(f"Post-save signal triggered for updated message: {instance}")

@receiver(post_save , sender=Message)
def create_notification_for_message(sender, instance, created, **kwargs):
    if created:
        try:
            recipient = User.objects.get(username=instance.recipient)
            reciever_recipient = recipient.User
            print(f"Creating notification for recipient: {recipient.username}")
        except User.DoesNotExist:
            print(f"Recipient {instance.recipient} does not exist. Message not sent.")
            return 
        # Create a notification for the recipient to inform them about the new message.
        # # This notification is initially marked as unread.
        Notification.objects.create(
            user=instance.recipient,
            message=instance,
            is_read=False
        )
    else:
        print(f"Message updated: {instance}. No notification created for updates.")

    
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


@receiver(post_delete, sender=User)
def delete_related_objects(sender, instance, **kwargs):
    # Delete all messages sent or received by the user
    Message.objects.filter(sender=instance.username).delete()
    Message.objects.filter(recipient=instance.username).delete()
    # Delete all notifications for the user
    Notification.objects.filter(user=instance).delete()
    # Delete all message histories where changed_by matches the username
    MessageHistory.objects.filter(changed_by=instance.username).delete()


        


