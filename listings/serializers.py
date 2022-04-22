from rest_framework import serializers
from .models import Listing

from accounts.models import CustomUser


class ListingSerializer(serializers.ModelSerializer):
    lister = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
    )

    class Meta:
        model = Listing
        fields = [
            "name",
            "address",
            "rent",
            "move_in",
            "move_out",
            "description",
            "lister",
        ]
