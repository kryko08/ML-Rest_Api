from django.shortcuts import render

from rest_framework.generics import (CreateAPIView,
                                     ListAPIView, 
                                     RetrieveAPIView,
                                    )

from rest_framework.mixins import (CreateModelMixin,
                                  )

from rest_framework.views import APIView

from .models import AlgorithmRequest
from .serializers import AlgorithmRequestSerializer

from .serializers import UserDetailSerializer, UserSerializer
from django.contrib.auth.models import User


# Request to Algorithm view
class RequestCreateView():
    pass

class RequestListView():
    pass

# User views 
class ListUserView(ListAPIView):
    """
    API endpoint that allows users to be viewed
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer 

class UserDetailView(RetrieveAPIView):
    """
    API indpoint to retrieve single user
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
