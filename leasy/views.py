from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .settings import ROOT_URL

import requests

# Create your views here.
def frontend(request, resource):
    return HttpResponse(render(request, "vue_index.html"))


def api_redirect(request):
    response = redirect("/api/v1/docs/")
    return response


def confirm_email_view(request, key):
    """Confirms a user's email and redirects them to the homepage

    Args:
        request (HttpRequest): the request made to this view
        key (String): the verification key to confirm the email

    Returns:
        HttpResponse: a redirect to the login page
    """
    confirm_email_url = ROOT_URL + reverse("account_email_verification_sent")
    requests.post(confirm_email_url, data={"key": key})

    response = redirect("login")
    return response
