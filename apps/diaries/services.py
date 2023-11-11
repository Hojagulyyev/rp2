from rp2.business_logic import XP_PER_DAIRY_COMMIT, MESSAGE_LENGTH_WHICH_BRINGS_XP_IN_DIARY_COMMIT

from .models import DiaryCommit


def calculate_diary_commit_xp(commit: DiaryCommit):
    additional_xp_for_more_detailed_message = int(
        len(commit.message) / MESSAGE_LENGTH_WHICH_BRINGS_XP_IN_DIARY_COMMIT
    )
    total_xp = [
        XP_PER_DAIRY_COMMIT,
        additional_xp_for_more_detailed_message,
    ]
    return sum(total_xp)
