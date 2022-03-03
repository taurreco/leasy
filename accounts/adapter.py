# https://django-allauth.readthedocs.io/en/latest/advanced.html#custom-redirects
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from allauth.account.adapter import DefaultAccountAdapter
from allauth.utils import build_absolute_uri


class CustomAccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        """Constructs the email confirmation (activation) url.

        Note that if you have architected your system such that email
        confirmations are sent outside of the request context `request`
        can be `None` here.
        """
        url = reverse("accounts:account_confirm_email", args=[emailconfirmation.key])
        ret = build_absolute_uri(request, url)
        return ret

    def respond_email_verification_sent(self, request, user):
        return HttpResponseRedirect(reverse("accounts:account_email_verification_sent"))
