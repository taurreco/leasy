from rest_framework import serializers
from .models import Listing, ListingImage

from accounts.models import CustomUser


class ListingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingImage
        fields = ["description", "image"]


class ListingSerializer(serializers.ModelSerializer):
    lister = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
    )
    images = ListingImageSerializer(many=True, read_only=True)

    class Meta:
        model = Listing
        fields = ["name", "address", "rent", "description", "lister", "id", "images"]
