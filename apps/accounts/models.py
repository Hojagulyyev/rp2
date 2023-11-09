from django.db import models
from django.contrib.auth.models import User

from apps.clans.models import Clan


class Account(models.Model):

    user: User = models.OneToOneField(User, on_delete=models.CASCADE)
    clan = models.ForeignKey(Clan, on_delete=models.CASCADE, blank=True, null=True)

    level = models.IntegerField(default=1)
    xp = models.IntegerField(default=0)
    required_xp_for_next_level = models.IntegerField(default=100)

    def __str__(self):
        return self.user.username
