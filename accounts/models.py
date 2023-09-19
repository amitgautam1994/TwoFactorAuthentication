from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.


class User(AbstractUser):
    mobile_no = models.CharField(max_length=12, unique=True)
    is_mobile_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, unique=True)

    USERNAME_FIELD = 'mobile_no'
    REQUIRED_FIELDS = []
    objects = UserManager()
