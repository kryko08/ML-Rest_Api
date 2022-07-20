from django.urls import path
from .views import (ListUserView, 
                    UserDetailView,
                    RequestCreateView,
                    RequestListView,
                   )

urlpatterns = [
    # Users 
    path("users/", ListUserView.as_view()),
    path("users/<int:pk>/", UserDetailView.as_view()),
    # Request machine learning model prediction 
    path("predict/", RequestCreateView.as_view()),
    # View all requests to predictor 
    path("predictions/", RequestListView.as_view())
]
