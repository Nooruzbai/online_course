from dj_rest_auth.jwt_auth import set_jwt_cookies
from django.contrib.auth import login as django_login
from dj_rest_auth.app_settings import api_settings
from dj_rest_auth.models import get_token_model
from dj_rest_auth.utils import jwt_encode
from dj_rest_auth.views import LogoutView, LoginView, sensitive_post_parameters_m
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from online_course import settings
from django.contrib.auth import logout as django_logout
from django.utils import timezone
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.social_serializers import TwitterLoginSerializer

user = get_user_model


class CustomLogoutView(LogoutView):
    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        if api_settings.SESSION_LOGIN:
            django_logout(request)

        response = Response(
            {'detail': 'Successfully logged out.'},
            status=status.HTTP_200_OK,
        )

        if api_settings.USE_JWT:
            # NOTE: this import occurs here rather than at the top level
            # because JWT support is optional, and if `USE_JWT` isn't
            # True we shouldn't need the dependency
            from rest_framework_simplejwt.exceptions import TokenError
            from rest_framework_simplejwt.tokens import RefreshToken

            from dj_rest_auth.jwt_auth import unset_jwt_cookies
            cookie_name = api_settings.JWT_AUTH_COOKIE

            unset_jwt_cookies(response)

            if 'rest_framework_simplejwt.token_blacklist' in settings.INSTALLED_APPS:
                # add refresh token to blacklist
                try:
                    token = RefreshToken(request.COOKIES['refresh'])
                    token.blacklist()
                except KeyError:
                    response.data = {'detail': 'Refresh token was not included in request data.'}
                    response.status_code =status.HTTP_401_UNAUTHORIZED
                except (TokenError, AttributeError, TypeError) as error:
                    if hasattr(error, 'args'):
                        if 'Token is blacklisted' in error.args or 'Token is invalid or expired' in error.args:
                            response.data = {'detail': (error.args[0])}
                            response.status_code = status.HTTP_401_UNAUTHORIZED
                        else:
                            response.data = {'detail': 'An error has occurred.'}
                            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

                    else:
                        response.data = {'detail': 'An error has occurred.'}
                        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

            elif not cookie_name:
                message = (
                    'Neither cookies or blacklist are enabled, so the token '
                    'has not been deleted server side. Please make sure the token is deleted client side.',
                )
                response.data = {'detail': message}
                response.status_code = status.HTTP_200_OK
        return response

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    # callback_url = CALLBACK_URL_YOU_SET_ON_GOOGLE
    client_class = OAuth2Client

