from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import generics,status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from .serializers import UserProfileSerializer, UserSerializer
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.views import TokenBlacklistView



class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserLoginView(TokenObtainPairView):
    pass


class Index(views.APIView):
    def get(self,request):
        return Response({"msg":"Hello,World!"})
    
# easy method to get user
# class UserProfileView(views.APIView):
#   permission_classes = [IsAuthenticated]
#   def get(self, request, format=None):
#     serializer = UserProfileSerializer(request.user)
#     return Response(serializer.data, status=status.HTTP_200_OK)


def get_user_from_token(request):
    authorization_header = request.headers.get('Authorization', '')
    if not authorization_header.startswith('Bearer'):
        return None

    token = authorization_header.split(' ')[1]

    try:
        access_token = AccessToken(token)
        token_user = JWTAuthentication().get_user(access_token)
        return token_user
    except Exception as e:
        return None

class UserProfileView(views.APIView):
  
  def get(self, request):
    user = get_user_from_token(request)
    if user:
        user_data = {
            'id': user.id,
            'username': user.username,
        }
        return Response(user_data)
    else:
        return Response({'error': 'Invalid or missing token'}, status=401)
    

class LogoutView(views.APIView):
    def post(self, request):
        token = request.data.get('token')  # Fetch token from the request data

        if token:
            # Add token to the blacklist
            BlacklistedToken.objects.create(token=token)
            return Response({'message': 'Token successfully blacklisted'}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid token or no token provided'}, status=status.HTTP_400_BAD_REQUEST)