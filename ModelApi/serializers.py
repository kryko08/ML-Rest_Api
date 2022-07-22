from dataclasses import fields
from rest_framework import serializers
from .models import AlgorithmRequest
from django.contrib.auth.models import User


# Request Serializers 
class AlgorithmRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlgorithmRequest
        fields = [ "request",
                   "response",
                   "requested_at"
                ]
        read_only_fiels = "requested_at"

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super(AlgorithmRequest, self).create(validated_data)


# Users serializers 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password",
                   "is_superuser",
                   "is_staff",
                   "is_active",
                ]


