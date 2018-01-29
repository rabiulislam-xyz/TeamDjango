from rest_framework import serializers

from .models import Group
from message.models import GroupMessage

class GroupSerializer(serializers.ModelSerializer):
    members_count = serializers.SerializerMethodField()
    def get_members_count(self, obj):
        return obj.members.count()

    class Meta:
        model =  Group
        fields = ('name',
                  'slug',
                  'creator',
                  'created_at',
                  'members_count')

class GroupMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMessage
        fields = ('content',
                  'created_at',
                  'updated_at',
                  'sender',
                  'group')
