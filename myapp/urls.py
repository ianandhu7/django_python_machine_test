from django.urls import path
from .views import RegisterView, UserListCreateView, UserRetrieveUpdateDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register_user'),
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRetrieveUpdateDeleteView.as_view(), name='user-detail'),
]
