from rest_framework import serializers
from email_tracker.models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"
        read_only_fields = ["count"]
