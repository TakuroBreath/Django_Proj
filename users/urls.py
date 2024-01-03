from django.contrib.auth.views import LoginView, LogoutView, PasswordResetCompleteView, PasswordResetDoneView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, confirm_email, CustomPasswordResetView, \
    CustomUserPasswordResetConfirmView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('confirm/<int:pk>/', confirm_email, name='confirm'),
    path('profile/password_reset/', CustomPasswordResetView.as_view(template_name="users/password_reset.html"),
         name='password_reset'),
    path('profile/password_reset_confirm/<uidb64>/<token>/',
         CustomUserPasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('profile/password_reset_complete/',
         PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('profile/password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
]
