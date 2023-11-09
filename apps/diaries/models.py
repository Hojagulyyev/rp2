from django.db import models
from django.utils import timezone

from apps.accounts.models import Account


class Diary(models.Model):

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.account} - {self.created_date}"


class DiaryCommit(models.Model):

    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.message


class DiaryComment(models.Model):

    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.body
