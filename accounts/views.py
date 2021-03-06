from lib2to3.pgen2.parse import ParseError
from django.shortcuts import redirect
from django.urls import reverse


from allauth.utils import email_address_exists
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

import requests

from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


@api_view()
def account_endpoints(request):
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


def confirm_email_view(request, key):
    """Confirms a user's email and redirects them to the homepage

    Args:
        request (HttpRequest): the request made to this view
        key (String): the verification key to confirm the email

    Returns:
        HttpResponse: a redirect to the login page
    """

    confirm_email_url = request.build_absolute_uri(
        reverse("accounts:account_email_verification_sent")
    )
    requests.post(confirm_email_url, data={"key": key})

    response = redirect("login")
    return response


@api_view(["POST"])
def check_email_exists_view(request):
    email = request.data["email"]
    if not email:
        raise ParseError("email must be included.")

    email_exists = email_address_exists(email)

    return Response({"email_exists": email_exists})
