# listings/urls.py

from django.urls import path, include

from .views import ListingsViewSet, listings_endpoints

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("listings", ListingsViewSet, basename="listings")

app_name = "listings"
urlpatterns = [
    path("", include(router.urls)),
    path(
        "endpoints/", listings_endpoints
    ),  # TODO: endpoints/listings, endpoints/accounts
]
