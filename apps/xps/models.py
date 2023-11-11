from enum import Enum

from django.db import models
from django.utils import timezone

from apps.accounts.models import Account
from apps.diaries.models import Diary


class XP(models.Model):

    class EarnTypes(Enum):
        DIARY_COMMIT = "diary_commit"

    EARN_TYPES = (
        (EarnTypes.DIARY_COMMIT.value, "Diary Commit"),
    )

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="xps")
    amount = models.PositiveSmallIntegerField(default=1)
    created_date = models.DateField(default=timezone.now)
    earn_type = models.CharField(max_length=64, choices=EARN_TYPES)
    diary = models.ForeignKey(Diary, on_delete=models.SET_NULL, null=True, related_name="xps")

    class Meta:
        verbose_name = "XP"
        verbose_name_plural = "XPs"

    def __str__(self):
        return f"{self.account} - {self.amount} XP"
