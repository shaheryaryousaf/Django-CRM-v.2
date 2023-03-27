from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (LoginView,
                                       LogoutView,
                                       PasswordResetView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetCompleteView,
                                       PasswordChangeView,
                                       PasswordChangeDoneView)

urlpatterns = [
    path('signin', auth_views.LoginView.as_view(
         redirect_authenticated_user=True), name='signin'),
    path("logout", LogoutView.as_view(), name='logout'),
    path("", views.dashboard, name='dashboard'),
]
