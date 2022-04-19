from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse
from rest_framework.response import Response


from listings.serializers import ListingSerializer
from .models import Listing
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view


class ListingsView(ListView):
    model = Listing
    template_name = "listings.html"


class ListingsViewSet(ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


@api_view()
def listings_endpoints(request):
    endpoints = {
        "listings-list": reverse("listings:listings-list"),
    }

    return Response(endpoints)
