from dj_rest_auth.app_settings import api_settings
from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView, ResendEmailVerificationView
from dj_rest_auth.views import UserDetailsView, PasswordResetView, PasswordResetConfirmView, \
    PasswordChangeView, LoginView
from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView
from accounts.views import CustomLogoutView , FacebookLogin, TwitterLogin, GoogleLogin

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

    path('auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('auth/twitter/', TwitterLogin.as_view(), name='twitter_login'),
    path('auth/google/', GoogleLogin.as_view(), name='google_login')

]


if api_settings.USE_JWT:

    urlpatterns += [
        path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
        path('token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
    ]

