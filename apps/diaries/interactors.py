import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse

from rp2.business_logic import COMMIT_MIN_LENGTH

from .models import Diary, DiaryCommit, DiaryComment
from .signals import diary_commit_created


@login_required
def create_commit(request, diary_id: int):

    # ===== DTO

    message = request.POST.get("message", "").strip()
    diary = Diary.objects.get(id=diary_id)

    # ===== VALIDATION

    if diary.account != request.user.account:
        messages.error(request, f"others' diaries are readonly")
        return redirect(
            f"{reverse('diaries:detail_view', kwargs={'id': diary.id})}"
        )

    if len(message) < COMMIT_MIN_LENGTH:
        messages.error(request, f"message length is less than {COMMIT_MIN_LENGTH} character")
        return redirect(
            f"{reverse('diaries:detail_view', kwargs={'id': diary.id})}"
            f"?message={message}"
        )

    if (
        DiaryCommit.objects
        .filter(
            diary=diary,
            message=message,
            created_datetime__date=datetime.date.today()
        )
        .exists()
    ):
        messages.error(request, message="this message already exists for today")
        return redirect(
            f"{reverse(viewname='diaries:detail_view', kwargs={'id': diary.id})}"
            f"?message={message}"
        )

    # ===== PROCESS

    diary_commit = DiaryCommit()
    diary_commit.diary = diary
    diary_commit.message = message
    diary_commit.save()

    diary_commit_created.send(sender=DiaryCommit, instance=diary_commit)

    return redirect("diaries:detail_view", diary.id)


@login_required
def create_comment(request, diary_id: int):

    # ===== DTO

    body = request.POST.get("body", "").strip()
    diary = Diary.objects.get(id=diary_id)

    # ===== VALIDATION

    if (
        DiaryComment.objects
        .filter(
            diary=diary,
            body=body,
            created_datetime__date=datetime.date.today()
        )
        .exists()
    ):
        messages.error(request, message="this comment already exists for today")
        return redirect(
            f"{reverse(viewname='diaries:detail_view', kwargs={'id': diary.id})}"
            f"?body={body}"
        )

    # ===== PROCESS

    diary_comment = DiaryComment()
    diary_comment.diary = diary
    diary_comment.author = request.user.account
    diary_comment.body = body
    diary_comment.save()

    diary.comments_last_read_by = request.user.account
    diary.save(update_fields=["comments_last_read_by"])

    return redirect(
        f"{reverse(viewname='diaries:detail_view', kwargs={'id': diary.id})}"
        f"?on_comments_tab=1"
    )
