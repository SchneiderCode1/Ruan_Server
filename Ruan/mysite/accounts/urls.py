from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views
from accounts.views import SignUpView, UpdateProfileView

urlpatterns = [
    path('', SignUpView.as_view(), name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile/', UpdateProfileView.as_view(), name='profile'),
    
]
