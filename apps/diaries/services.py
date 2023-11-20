from rp2.business_logic import (
    XP_PER_DAIRY_COMMIT,
    MESSAGE_LENGTH_WHICH_BRINGS_XP_IN_DIARY_COMMIT,
    STAR_FILLING_BONUS_VALUE,
    ADDITIONAL_XP_FOR_STAR_FILLING,
)

from .models import DiaryCommit


def calculate_diary_commit_xp(commit: DiaryCommit):
    total_xp = [
        XP_PER_DAIRY_COMMIT,
    ]

    # additional xp for more detailed message
    additional_xp_for_more_detailed_message = int(
        len(commit.message) / MESSAGE_LENGTH_WHICH_BRINGS_XP_IN_DIARY_COMMIT
    )
    total_xp.append(additional_xp_for_more_detailed_message)

    # additional xp for star filling bonus
    if commit.diary.commits.count() == STAR_FILLING_BONUS_VALUE:
        total_xp.append(ADDITIONAL_XP_FOR_STAR_FILLING)

    return sum(total_xp)
