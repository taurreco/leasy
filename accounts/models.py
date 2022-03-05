from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    # TODO figure out how to remove username as field
    username = models.CharField(unique=False, max_length=100)
    email = models.EmailField(("email address"), unique=True)
    # TODO add unique phone number as well?

    @property
    def api_detail_url(self):
        return reverse("accounts:users-detail", args=[self.pk])
