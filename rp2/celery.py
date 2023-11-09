import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rp2.settings")
app = Celery("rp2")
app.config_from_object("django.conf:settings", namespace="CELERY")

# add tasks here

app.conf.beat_schedule = {
    "create_daily_diary_for_every_account": {
        "task": "apps.diaries.tasks.create_daily_diary_for_every_account",
        "schedule": crontab(hour="0", minute="0"),
    },
}

app.autodiscover_tasks()
