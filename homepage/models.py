from django.contrib.auth.models import User
from django.db.models import OneToOneField
from django.db import models
from django.views.generic import DetailView

from accounts.models import genders, UserProfile

# Create your models here.


class DisplayAccounts(models.Model):
    username = models.CharField(max_length=100)


class Room(models.Model):
    user1 = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)


class Message(models.Model):
    text = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

