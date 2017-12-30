from django.contrib import admin

from .models import Message, PrivateMessage, GroupMessage

admin.site.register(Message)
admin.site.register(PrivateMessage)
admin.site.register(GroupMessage)