from django.dispatch import receiver

from rp2.business_logic import XP_PER_DAIRY_COMMIT

from apps.diaries.models import DiaryCommit
from apps.diaries.signals import diary_commit_created
from apps.accounts.models import Account


@receiver(diary_commit_created)
def increase_xp_by_diary_commit(
    sender,
    instance: DiaryCommit,
    **kwargs,
):
    instance.diary.account.increase_xp(XP_PER_DAIRY_COMMIT)
