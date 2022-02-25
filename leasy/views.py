from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def frontend(request, resource):
    return HttpResponse(render(request, "vue_index.html"))


def api_redirect(request):
    response = redirect("/api/v1/docs/")
    return response
