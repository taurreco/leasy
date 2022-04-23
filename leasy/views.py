from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from rest_framework.decorators import api_view
from rest_framework.response import Response


# ENDPOINT VIEWS


@api_view()
def account_endpoints(request):
    """API View to get all account endpoints."""
    user = request.user

    user_detail_url = user.api_detail_url if user.is_authenticated else ""

    endpoints = {
        "current-user-detail": user_detail_url,
        "account-email-verification-sent": reverse(
            "accounts:account_email_verification_sent"
        ),
        "check-email-exists": reverse("accounts:check_email_exists"),
        "login": reverse("accounts:rest_login"),
        "logout": reverse("accounts:rest_logout"),
        "password-change": reverse("accounts:rest_password_change"),
        "password-reset": reverse("accounts:rest_password_reset"),
        "password-reset-confirm": reverse("accounts:rest_password_reset_confirm"),
        "register": reverse("accounts:rest_register"),
        "resend-email": reverse("accounts:rest_resend_email"),
    }

    return Response(endpoints)


@api_view()
def listings_endpoints(request):
    """API View to get all listings endpoints."""
    endpoints = {
        "listings-list": reverse("listings:listings-list"),
    }

    return Response(endpoints)


# Create your views here.
def frontend(request, resource, **kwargs):
    user_id = kwargs.get("uidb64")
    token = kwargs.get("token")
    if user_id and token:
        print(user_id)
        print(token)
    return HttpResponse(render(request, "vue_index.html"))


def api_redirect(request):
    response = redirect("/api/v1/docs/")
    return response
