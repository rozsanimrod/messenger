from django.urls import path
from homepage.views import homepage

app_name = 'homepage'

urlpatterns = [
    path('', homepage, name="home"),
]
