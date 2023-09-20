from django.urls import path, include
from rest_framework import routers
from .views import send_otp, verify_otp, resend_otp


urlpatterns = [
    # path('register/', RegisterUserViewSet.as_view({'post': 'create'}), name='register'),
    path('send_otp/', send_otp, name='send_otp'),
    path('resend_otp/', resend_otp, name='resend_otp'),
    path('verify_otp/', verify_otp, name='verify_otp'),
]