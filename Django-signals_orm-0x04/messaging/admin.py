from django.contrib import admin
# Register your models here trib import admin

from .models import Message
admin.site.register(Message)
admin.site.register(User)
admin.site.register(Notification)
admin.site.register(MessageHistory)