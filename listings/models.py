from django.db import models
from django.utils import timezone

from accounts.models import CustomUser


class Listing(models.Model):
    """A sublease listing."""

    # temporary fields / organization ?
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    rent = models.IntegerField()
    description = models.CharField(max_length=40000)
    lister = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def dates_booked(self):
        Listing.objects.get(id=self.id)


def listing_image_path(instance, image):
    """Returns the upload path for listing images."""
    return f"images/listings/{instance.id}/{image}"


class ListingImage(models.Model):
    """An image associated with a listing."""

    description = models.CharField(max_length=500)
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, null=False, related_name="images"
    )
    image = models.ImageField(upload_to=listing_image_path)


class ListingBooking(models.Model):
    """Dates that the listing is booked."""

    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, null=False, related_name="bookings"
    )
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=False)
    renter = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True, blank=True
    )
