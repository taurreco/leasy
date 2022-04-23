from rest_framework import serializers
from .models import Listing, ListingBooking, ListingImage

from accounts.models import CustomUser


class ListingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingImage
        fields = ["description", "image"]


class ListingBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingBooking
        fields = ["start_date", "end_date"]


class ListingSerializer(serializers.ModelSerializer):
    lister = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    images = ListingImageSerializer(many=True, read_only=True)
    bookings = ListingBookingSerializer(many=True, read_only=True)

    class Meta:
        model = Listing
        fields = [
            "name",
            "address",
            "bookings",
            "rent",
            "description",
            "lister",
            "id",
            "images",
            "start_date",
            "end_date",
        ]
