from django.urls import path
from .views import (
    RegistrationAPIView,
    LoginAPIView,
    GETALLUser,
    user_profile_detail,
)

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('all-users/', GETALLUser.as_view(), name='all-users'),
    path('profile/', user_profile_detail, name='user-profile-detail'),
]
