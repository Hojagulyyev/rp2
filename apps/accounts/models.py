from django.db import models
from django.contrib.auth.models import User

from apps.clans.models import Clan


class Account(models.Model):

    user: User = models.OneToOneField(User, on_delete=models.CASCADE)
    clan = models.ForeignKey(Clan, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username
