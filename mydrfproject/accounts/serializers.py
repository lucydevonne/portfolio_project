from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']  # Include any additional fields here
        extra_kwargs = {'password': {'write_only': True}}  # Password should be write-only

    def create(self, validated_data):
        # Hash the password before saving
        user = CustomUser.objects.create_user(**validated_data)
        return user
