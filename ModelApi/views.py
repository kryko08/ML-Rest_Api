from urllib import response
from django.shortcuts import get_object_or_404

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

from rest_framework.decorators import api_view

from .apps import ModelapiConfig

from rest_framework.response import Response



# Request to Algorithm view
@api_view(["GET", "POST"])
def request_model_view(request, pk=None, *args, **kwargs):
    # If HTTP method is "POST", run model inference and show results
    if request.method == "POST":
        serializer = AlgorithmRequestSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # Run inference
            validated_data = serializer.validated_data
            message = validated_data["request_message"]
            model_output = ModelapiConfig.predictor.translate(message)
            serializer.save(response=model_output)
        else:
            return Response()

    # If HTTP method is "Get", view all previous algorithm requests
    elif request.method == "GET":
        # Detail view 
        if pk is not None:
            obj = get_object_or_404(AlgorithmRequest, pk=pk)
            data = AlgorithmRequestSerializer(obj, many=False).data
            return Response(data)
        # List view
        queryset = AlgorithmRequest.objects.all()
        data = AlgorithmRequestSerializer(queryset, many=True).data
        return Response(data)



# View for listing all requests 
class RequestListView(ListAPIView):
    queryset = AlgorithmRequest.objects.all()
    serializer_class = AlgorithmRequestSerializer
    

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
