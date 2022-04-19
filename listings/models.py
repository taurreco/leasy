from django.db import models

from accounts.models import CustomUser

class Listing(models.Model):

    # temporary fields / organization ?
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    rent = models.IntegerField()
    move_in = models.CharField(max_length=250)
    move_out = models.CharField(max_length=250)
    desc = models.CharField(max_length=40000)
    lister = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
