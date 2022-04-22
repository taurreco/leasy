from rest_framework import serializers
from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            "name",
            "address",
            "rent",
            "move_in",
            "move_out",
            "description",
        ]
