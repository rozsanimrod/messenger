from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, \
    PasswordResetDoneView, PasswordResetCompleteView

from django.views.generic import CreateView
from django.urls import reverse_lazy
from accounts.forms import SignUpForm
from django.contrib.auth import logout


class LoginViewCustom(LoginView):
    template_name = "accounts/login.html"


class SignUp(CreateView):
    template_name = 'form.html'
    success_url = reverse_lazy('homepage:home')
    form_class = SignUpForm



