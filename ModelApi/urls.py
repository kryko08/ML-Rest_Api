from django.urls import path
from .views import (ListUserView, 
                    UserDetailView,
                    AlgoRequestMixinView,
                    AlgoRequestDetailView,
                    UserPredictionListView,
                   )

urlpatterns = [
    # Users 
    path("users/", ListUserView.as_view()),
    path("users/<int:pk>/detail", UserDetailView.as_view(), name="user-detail"),
    path("users/<int:pk>/predictions", UserPredictionListView.as_view(), name="user-prediction-list"),
    # Request machine learning model prediction 
    path("predict/", AlgoRequestMixinView.as_view()),
    path("predict/<int:pk>/detail/", AlgoRequestDetailView.as_view(), name="algorithmrequest-detail"),
    # Predictions views 
]
