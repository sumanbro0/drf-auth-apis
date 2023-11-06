from django.contrib import admin
from django.urls import path,include
from .views import Index,RegisterUserView,UserDetailsView,CustomObtainAuthToken,LogoutView
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('home/',Index.as_view(),name='home'),
    path('register/',RegisterUserView.as_view(),name='register'),
    # path('auth/',obtain_auth_token),
    path('login/',CustomObtainAuthToken.as_view(),name='login'),
    path('user/',UserDetailsView.as_view(),name='user'),
    path('logout/',LogoutView.as_view(),name='logout'),
]

