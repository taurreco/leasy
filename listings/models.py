from django.db import models
from django.utils import timezone

from accounts.models import CustomUser


class Listing(models.Model):

    # temporary fields / organization ?
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    rent = models.IntegerField()
    description = models.CharField(max_length=40000)
    lister = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name
