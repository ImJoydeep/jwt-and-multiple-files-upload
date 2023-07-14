from .forms import UploadForm
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import SendPasswordResetEmailSerializer, UserChangePasswordSerializer, UserLoginSerializer, UserPasswordResetSerializer, UserProfileSerializer, UserRegistrationSerializer
from .models import User, Document
from django.contrib.auth import authenticate
from account.renderer import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
import json
import random
from django.http import JsonResponse, HttpResponse

# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class UserRegistrationView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token = get_tokens_for_user(user)
    return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    password = serializer.data.get('password')
    captcha = serializer.data.get('captcha')
    if str_num == str(captcha):
      print(captcha)
      user = authenticate(email=email, password=password)
      if user is not None:
        token = get_tokens_for_user(user)
        userObj = User.objects.get(email=user)
        userData = {
          "name": userObj.name,
          "email": userObj.email,
        }
        return Response({'token':token,'userData':userData, 'msg':'Login Success'}, status=status.HTTP_200_OK)
      else:
        return Response({'errors':{'fields':'Email or Password is not Valid'}}, status=status.HTTP_404_NOT_FOUND)
    else:
      return Response({"errors": {'fields': 'Captcha Does not Match'}}, status=status.HTTP_403_FORBIDDEN)

class UserProfileView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    serializer = UserProfileSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)

class UserChangePasswordView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def post(self, request, format=None):
    serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)

class SendPasswordResetEmailView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = SendPasswordResetEmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user_email = serializer.data['email']
    return Response({'msg':f'Password Reset link send at {user_email}. Please check your Email'}, status=status.HTTP_200_OK)

class UserPasswordResetView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, uid, token, format=None):
    serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)
  
class UploadView(APIView):
  def post(self, request):
      form = UploadForm()
      if request.FILES:
          form = UploadForm(request.POST, request.FILES)
          if form.is_valid():
              file = Document()
              file.document = request.FILES.get('document')
              file.save()
      
      return Response({'success': True})
  
class CaptchaView(APIView):
    def get(self, request):
        num = random.randrange(10874, 98939)
        global str_num
        str_num = str(num)
        return HttpResponse(str_num)
    

