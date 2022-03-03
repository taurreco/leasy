from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from django.urls import reverse


import requests


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
