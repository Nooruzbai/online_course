from dj_rest_auth.app_settings import api_settings
from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView, ResendEmailVerificationView
from dj_rest_auth.views import LoginView, UserDetailsView, PasswordResetView, PasswordResetConfirmView, \
    PasswordChangeView
from django.urls import path, re_path
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenVerifyView

from accounts.views import CustomLogoutView

app_name = 'accounts'

urlpatterns = [
    path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),

    path("register/", RegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", CustomLogoutView.as_view(), name="rest_logout"),


    path("user/", UserDetailsView.as_view(), name="rest_user_details"),
    path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    path('resend-email/', ResendEmailVerificationView.as_view(), name="rest_resend_email"),

]


if api_settings.USE_JWT:

    urlpatterns += [
        path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
        path('token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
    ]
