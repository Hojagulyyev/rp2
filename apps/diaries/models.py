from django.db import models
from django.utils import timezone

from rp2.business_logic import XP_PER_DAIRY_COMMIT

from apps.accounts.models import Account


class Diary(models.Model):

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_date = models.DateField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Diaries"

    def __str__(self):
        return f"{self.account} - {self.created_date}"

    def get_earned_xp(self):
        print("Hello")
        xp_amount_list = self.xps.values_list("amount", flat=True)
        print(xp_amount_list)
        return sum(xp_amount_list)


class DiaryCommit(models.Model):

    diary = models.ForeignKey(Diary, on_delete=models.CASCADE, related_name="commits")
    message = models.TextField()
    created_datetime = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Diary Commits"

    def __str__(self):
        return self.message


class DiaryComment(models.Model):

    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    body = models.TextField()
    created_datetime = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Diary Comments"

    def __str__(self):
        return self.body
