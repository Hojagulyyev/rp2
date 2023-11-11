from django.dispatch import receiver

from rp2.business_logic import XP_PER_DAIRY_COMMIT, MESSAGE_LENGTH_WHICH_BRINGS_XP_IN_DIARY_COMMIT

from apps.diaries.models import DiaryCommit
from apps.diaries.signals import diary_commit_created


@receiver(diary_commit_created)
def increase_xp_by_diary_commit(
    sender,
    instance: DiaryCommit,
    **kwargs,
):
    additional_xp_for_more_detailed_message = int(instance.message / MESSAGE_LENGTH_WHICH_BRINGS_XP_IN_DIARY_COMMIT)
    total_xp = [
        XP_PER_DAIRY_COMMIT,
        additional_xp_for_more_detailed_message,
    ]
    instance.diary.account.increase_xp(sum(total_xp))
