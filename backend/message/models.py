from django.contrib.auth.models import User
from django.db import models

from group.models import Group


class Message(models.Model):
    sender     = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    content    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-created_at']


class PrivateMessage(Message):
    receiver = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='received_messages')

class GroupMessage(Message):
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING, related_name='messages')