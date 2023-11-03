from django.db import models

from apps.accounts.models import Account
from apps.clans.models import Clan


class Issue(models.Model):

    author = models.ForeignKey(Account, on_delete=models.SET_NULL, blank=True, null=True)
    assignees = models.ManyToManyField(Account, related_name="issues_from_assignee")
    reviewers = models.ManyToManyField(Account, related_name="issues_from_reviewer")
    clan = models.ForeignKey(Clan, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=255, blank=False, null=False)
    category = models.CharField(max_length=64, blank=True, null=True)
    priority = models.CharField(max_length=64, blank=True, null=True)
    status = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
