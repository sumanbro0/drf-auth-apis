from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import authenticate
from rest_framework.permissions import BasePermission

from .serializers import UserAuthenticationSerializer, UserSerializer
# Create your views here.
class Index(APIView):
    def get(self,request):
        return Response({"message":"Hello World"}) 
    

# class RegisterUserView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class RegisterUserView(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        password = serializer.validated_data.pop('password', None)

        self.perform_create(serializer)
        user = User.objects.create(**serializer.validated_data)
        user = serializer.instance

        if password:
            user.set_password(password)
            user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

          
    
# class RegisterUserView(APIView):
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             self.perform_create(serializer)
#             user = serializer.instance

#             # Create a token for the user
#             token, created = Token.objects.get_or_create(user=user)

#             # Assuming you want to return the token key upon successful registration
#             return Response({'token': token.key}, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        # Access user details
        user_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            # Include other user data as needed
        }
        return Response(user_data)
    


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = UserAuthenticationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        # Customizing the response to include user details
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'email': user.email  # Add other user details here
        })
    
class LogoutView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        if request.user and request.user.auth_token:
            request.user.auth_token.delete()  
            return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'No token found for this user.'}, status=status.HTTP_400_BAD_REQUEST)
        


class CustomPermissionClass(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'admin':
            return True
        else:
            return False