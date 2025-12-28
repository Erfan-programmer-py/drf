from rest_framework import serializers
from .models import UserModel

# User model serializer
class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"
