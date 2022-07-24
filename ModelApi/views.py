from django.contrib.auth.models import User

from rest_framework.generics import (CreateAPIView,
                                     ListAPIView, 
                                     RetrieveAPIView,
                                     DestroyAPIView,
                                     GenericAPIView
                                    )

from rest_framework.mixins import (ListModelMixin,
                                   RetrieveModelMixin,
                                   CreateModelMixin
                                  )


from .models import AlgorithmRequest

from django.contrib.auth.models import User

from .apps import ModelapiConfig

from.serializers import (
    AlgorithmRequestListSerializer,
    AlgorithmRequestDetailSerializer,
    UserRequestsListSerializer,
    UserSerializer,
    UserDetailSerializer,

    )



# Request to Algorithm view
class AlgoRequestMixinView(
    RetrieveModelMixin,
    ListModelMixin, 
    CreateModelMixin,
    GenericAPIView
    ):

    queryset = AlgorithmRequest.objects.all()
    serializer_class = AlgorithmRequestListSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = self.request.user
        request_message = serializer.validated_data.get("request_message")
        pretiction = ModelapiConfig.predictor.translate(request_message)
        serializer.save(user=user, response=pretiction)

        
class AlgoRequestDetailView(RetrieveAPIView):
    queryset = AlgorithmRequest.objects.all()
    serializer_class = AlgorithmRequestDetailSerializer
    lookup_field = "pk"
    

# User views--------
# List all Algorithm request for given user
class UserPredictionListView(ListAPIView):
    queryset = AlgorithmRequest.objects.all()
    serializer_class = UserRequestsListSerializer
    lookup_field = "pk"

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        user_pk = self.kwargs["pk"]
        print(user_pk)
        filtered_qs = qs.filter(user=user_pk)
        return filtered_qs


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
    
