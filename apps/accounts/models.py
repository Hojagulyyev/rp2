from django.db import models
from django.contrib.auth.models import User

from rp2.business_logic import ADDITIONAL_GROWING_XP_PER_LEVEL
from apps.clans.models import Clan


class Account(models.Model):

    user: User = models.OneToOneField(User, on_delete=models.CASCADE)
    clan = models.ForeignKey(Clan, on_delete=models.CASCADE, blank=True, null=True)

    level = models.IntegerField(default=1)
    xp = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def get_required_xp_for_next_level(self):
        return self.level * ADDITIONAL_GROWING_XP_PER_LEVEL

    def increase_xp(self, xp_amount):
        self.xp += xp_amount
        required_xp_for_next_level = self.get_required_xp_for_next_level()

        if self.xp > required_xp_for_next_level:
            self.level += 1
            self.xp = required_xp_for_next_level - self.xp

        self.save()
