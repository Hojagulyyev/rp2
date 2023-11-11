from django.dispatch import receiver

from apps.diaries.models import DiaryCommit
from apps.diaries.signals import diary_commit_created
from apps.xps.models import XP
from apps.diaries.services import calculate_diary_commit_xp


@receiver(diary_commit_created)
def create_xp_model_by_diary_commit(
    sender,
    instance: DiaryCommit,
    **kwargs,
):
    total_xp_from_diary_commit = calculate_diary_commit_xp(instance)

    xp = XP()
    xp.diary = instance.diary
    xp.account = instance.diary.account
    xp.amount = total_xp_from_diary_commit
    xp.earn_type = XP.EarnTypes.DIARY_COMMIT.value
    xp.save()
