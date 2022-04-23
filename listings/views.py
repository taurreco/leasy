from django.views.generic import ListView


from listings.serializers import ListingSerializer
from .models import Listing
from rest_framework.viewsets import ModelViewSet


class ListingsView(ListView):
    model = Listing
    template_name = "listings.html"


class ListingsViewSet(ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
