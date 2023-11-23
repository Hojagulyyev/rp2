from rp2.business_logic import (
    XP_PER_DAIRY_COMMIT,
    MESSAGE_LENGTH_WHICH_BRINGS_XP_IN_DIARY_COMMIT,
    STAR_FILLING_BONUS_VALUE,
    ADDITIONAL_XP_FOR_STAR_FILLING,
    BANNED_WORDS_IN_MORE_DETAILED_MESSAGE,
)

from .models import DiaryCommit


def has_commit_message_banned_words(message: str):
    for word in BANNED_WORDS_IN_MORE_DETAILED_MESSAGE:
        if word in message:
            return True
    return False


def calculate_diary_commit_xp(commit: DiaryCommit):
    total_xp = [
        XP_PER_DAIRY_COMMIT,
    ]

    # additional xp for more detailed message
    if not has_commit_message_banned_words(commit.message):
        additional_xp_for_more_detailed_message = int(
            len(commit.message) / MESSAGE_LENGTH_WHICH_BRINGS_XP_IN_DIARY_COMMIT
        )
        total_xp.append(additional_xp_for_more_detailed_message)

    # additional xp for star filling bonus
    if commit.diary.commits.count() == STAR_FILLING_BONUS_VALUE:
        total_xp.append(ADDITIONAL_XP_FOR_STAR_FILLING)

    return sum(total_xp)
