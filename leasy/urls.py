"""leasy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views import frontend, api_redirect

api_urls = [
    path("", api_redirect),  # redirects "" to "docs/"
    # spectacular
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
    # accounts
    path("accounts/", include("accounts.urls")),
]

frontend_urls = [
    path("", frontend, name="homepage"),
    path("login/", frontend, name="login"),
    path("logout/", frontend, name="logout"),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(api_urls), name="api"),
    path("", include(frontend_urls), {"resource": ""}),
    path("<path:resource>", include(frontend_urls)),
]
