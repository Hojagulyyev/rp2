from celery import shared_task

from apps.accounts.models import  Account

from .models import Diary


@shared_task
def create_daily_diary_for_every_account():
    for account in Account.objects.all():
        diary = Diary()
        ...
