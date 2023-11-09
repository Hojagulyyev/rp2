from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse

from rp2.business_logic import COMMIT_MIN_LENGTH

from .models import Diary, DiaryCommit
from .signals import diary_commit_created


@login_required
def commit(request, diary_id: int):

    # ===== DTO

    message = request.POST.get("message", "").strip()
    diary = Diary.objects.get(id=diary_id)

    # ===== VALIDATION

    if len(message) < COMMIT_MIN_LENGTH:
        messages.error(request, f"message length is less than {COMMIT_MIN_LENGTH} character")
        return redirect(
            f"{reverse('diaries:detail_view', kwargs={'id': diary.id})}"
            f"?message={message}"
        )

    # ===== PROCESS

    diary_commit = DiaryCommit()
    diary_commit.diary = diary
    diary_commit.message = message
    diary_commit.save()

    diary_commit_created.send(sender=DiaryCommit, instance=diary_commit)

    return redirect("diaries:detail_view", diary.id)
