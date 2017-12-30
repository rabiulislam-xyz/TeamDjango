from rest_framework import serializers

from .models import PrivateMessage


class PrivateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateMessage
        fields = ('content',
                  'created_at',
                  'updated_at',
                  'sender',
                  'receiver')
