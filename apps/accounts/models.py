from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed


class User(AbstractUser):
    bio = models.CharField(
        max_length=256,
        blank=True,null=True
    )
    profile_image = models.ImageField(upload_to='instagram/profiles/',blank=True,null=True)
    full_name = models.CharField(max_length=128,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def get_tokens(self):
        if not self.is_active:
            raise AuthenticationFailed("User is not active")

        refresh = RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def __str__(self):
        return self.username
