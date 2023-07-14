from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenVerifyView
from . import views
from account.views import CaptchaView, SendPasswordResetEmailView, UserChangePasswordView, UserLoginView, UserProfileView, UserRegistrationView, UserPasswordResetView, UploadView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('upload/', UploadView.as_view(), name='upload'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('get_captcha/', CaptchaView.as_view(), name='get_captcha'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
