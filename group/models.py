from django.contrib.auth.models import User
from django.db import models


class Group(models.Model):
    name         = models.CharField(max_length=255)
    slug         = models.SlugField(allow_unicode=True, unique=True)
    creator      = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='created_groups')
    members      = models.ManyToManyField(User, related_name='subscribed_groups')
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name