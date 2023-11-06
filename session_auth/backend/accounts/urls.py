# myapp/urls.py
from django.urls import path
from .views import ProductListView, RegisterView, LoginView, LogoutView,MyProtectedView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', MyProtectedView.as_view(), name='profile'),
    path('products/', ProductListView.as_view(), name='product-list'),

]