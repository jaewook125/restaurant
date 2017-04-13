from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Restaurant(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    restimage = models.ImageField()
    restname = models.CharField(max_length=20)
    restsite = models.CharField(max_length=200)

    def __str__(self):
        return self.restname
