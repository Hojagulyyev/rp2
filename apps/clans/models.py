from django.db import models


class Clan(models.Model):

    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
