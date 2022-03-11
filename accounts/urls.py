from django.urls import path, re_path, include
from dj_rest_auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
)
from dj_rest_auth.registration.views import (
    RegisterView,
    ResendEmailVerificationView,
    VerifyEmailView,
)

from rest_framework.routers import DefaultRouter

from .views import (
    CustomUserViewSet,
    account_endpoints,
    confirm_email_view,
    check_email_exists_view,
)


user_auth_urls = [
    # dj-rest-auth endpoints
    # https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html
    path("password/change/", PasswordChangeView.as_view(), name="rest_password_change"),
    path("password/reset/", PasswordResetView.as_view(), name="rest_password_reset"),
    path(
        "password/reset/confirm/",
        PasswordResetConfirmView.as_view(),
        name="rest_password_reset_confirm",
    ),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    # dj-rest-auth registration endpoints
    # https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html#registration
    path("register/", RegisterView.as_view(), name="rest_register"),
    path(
        "resend-email/", ResendEmailVerificationView.as_view(), name="rest_resend_email"
    ),
    path(
        "account-email-verification-sent/",
        VerifyEmailView.as_view(),
        name="account_email_verification_sent",
    ),
    re_path(
        r"^account-confirm-email/(?P<key>[-:\w]+)/$",
        confirm_email_view,
        name="account_confirm_email",
    ),
    # checks if a specific email address exists
    path("check-email-exists/", check_email_exists_view, name="check_email_exists"),
]

router = DefaultRouter()
router.register("users", CustomUserViewSet, basename="users")

app_name = "accounts"
urlpatterns = [
    path("endpoints/", account_endpoints),
    path("", include(user_auth_urls)),
    path("", include(router.urls)),
]
