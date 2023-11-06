# myapp/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from accounts.models import Product
from .serializers import ProductSerializer, UserLoginSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.authentication import SessionAuthentication
from django.views.decorators.csrf import csrf_protect

class RegisterView(APIView):
    def post(self, request):
       
        serializer = UserSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "User created successfully."})
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    authentication_classes=[SessionAuthentication]
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            login(request, user)
            return Response({"detail": "Login successful for user: {}".format(user.username)})
        else:
            print(serializer.error_messages)
            return Response(serializer.error_messages, status=400)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    # authentication_classes=[SessionAuthentication]
    def get(self, request):
        print(request.user)
        logout(request)
        return Response({"detail": "User logged out successfully."})

# class MyProtectedView(APIView):
#     def get(self, request):
#         headers = request.META
#         csrf_token = headers.get('HTTP_X_CSRFTOKEN')
#         print(csrf_token)
#         if request.user.is_authenticated:
#             return Response({"detail": "Authenticated user: {}".format(request.user.username)})
#         else:
#             return Response({"detail": "User is not authenticated"}, status=401)

class MyProtectedView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes=[SessionAuthentication]
    def get(self, request):
        return Response({"detail": "Authenticated user: {}".format(request.user.username)})
    

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class ProductListView(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#         # return Response({"msg":"hello"})