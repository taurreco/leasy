from django.http import HttpResponse
from django.shortcuts import render, redirect

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
