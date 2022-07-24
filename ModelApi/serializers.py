from dataclasses import fields
from numpy import source
from rest_framework import serializers
from .models import AlgorithmRequest
from django.contrib.auth.models import User

from rest_framework.reverse import reverse


# Request Serializers 
class AlgorithmRequestListSerializer(serializers.ModelSerializer):
    request_detail = serializers.HyperlinkedIdentityField(
        view_name="algorithmrequest-detail",
        lookup_field="pk",
        read_only=True,
        )
    class Meta:
        model = AlgorithmRequest
        fields = ["request_detail", 
        "request_message", 
        ]


class AlgorithmRequestDetailSerializer(serializers.ModelSerializer):
    requested_by = serializers.CharField(read_only=True, source="user.username")
    class Meta:
        model = AlgorithmRequest
        fields = [
            "requested_by",
            "request_message",
            "response",
            "requested"
        ]


class UserRequestsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlgorithmRequest
        fields = [
            "request_message",
            "response"
            ]
        read_only_fiels = fields


class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        lookup_field="pk",
        view_name="user-detail", 
        read_only=True
    )
    class Meta:
        model = User
        fields = ["url", "username"]


class UserRequestInlineSerializer(serializers.Serializer):
    request_message = serializers.CharField()
    request_url = serializers.HyperlinkedIdentityField(
        view_name="algorithmrequest-detail",
        lookup_field="pk",
    )


class UserDetailSerializer(serializers.ModelSerializer):
    last_request = serializers.SerializerMethodField(read_only=True)
    requests_total = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            "username", 
            "last_login",
            "date_joined",
            "last_request",
            "requests_total"
            ]

    def get_last_request(self, obj):
        user = obj
        qs = user.algorithmrequest_set.order_by('-requested').first()
        return UserRequestInlineSerializer(qs, many=False, context=self.context).data

    def get_requests_total(self, obj):
        user = obj
        num_records = user.algorithmrequest_set.all().count()
        return num_records
        
