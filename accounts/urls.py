from django.urls import path
from .views import LoginViewCustom

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginViewCustom.as_view(), name="login"),
]
