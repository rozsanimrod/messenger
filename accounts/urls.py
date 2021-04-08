from django.urls import path
from .views import LoginViewCustom, SignUp
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView \
    , PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView


# app_name = 'accounts'

urlpatterns = [
    path('login/', LoginViewCustom.as_view(), name="login"),
    path('signup/', SignUp.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change', PasswordChangeView.as_view(
        template_name='accounts/password_change.html'
    ), name='password_change'),
    path('password_change_done', PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='accounts/password_reset_form.html'
    ), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete')
]
