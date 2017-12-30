from rest_framework import serializers

from group.serializers import GroupSerializer

class UserSerializer(serializers.Serializer):
    id           = serializers.IntegerField()
    username     = serializers.CharField()
    first_name   = serializers.CharField()
    last_name    = serializers.CharField()
    email        = serializers.EmailField()
    website      = serializers.SerializerMethodField()
    photo        = serializers.SerializerMethodField()
    location     = serializers.SerializerMethodField()

    subscribed_groups = serializers.SerializerMethodField()

    def get_photo(self, obj):
        return obj.profile.photo

    def get_website(self, obj):
        return obj.profile.website

    def get_location(self, obj):
        return obj.profile.location

    def get_subscribed_groups(self, obj):
        return GroupSerializer(obj.subscribed_groups, many=True).data


