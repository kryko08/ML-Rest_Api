from dataclasses import fields
from rest_framework import serializers
from .models import Algorithm, AlgorithmRequest
from django.contrib.auth.models import User


# Request Serializers 
class AlgorithmRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlgorithmRequest
        fields = [ "algorithm", 
                   "input_image",
                   "response",
                ]

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


