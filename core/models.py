# -*-coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    #avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    hcp = models.FloatField(default=0.0, blank=True, null=True)

