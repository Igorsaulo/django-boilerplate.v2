from django.urls import path
from .views import RegistrationView, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers


router = routers.DefaultRouter()

router.register('register', RegistrationView, basename='register')


users_urls = [
    path('login/', CustomTokenObtainPairSerializer.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
]
users_urls += router.urls