from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from rp2.pagination import paginate

from .models import Diary


@login_required
def newsfeed(request):

    # ===== DTO

    page = request.GET.get("page", None)
    page_size = request.GET.get("page_size", None)
    account = request.user.account

    # ===== PROCESS

    diary_queryset = (
        Diary.objects
        .filter(account__clan=account.clan)
        .order_by("-created_date")
    )
    paginated_diary_queryset = paginate(diary_queryset, page, page_size)

    # ===== CONTEXT

    context = {
        "diaries": paginated_diary_queryset,
    }

    return render(request, "diaries/newsfeed.html", context)


@login_required
def diaries(request):

    # ===== DTO

    page = request.GET.get("page", None)
    page_size = request.GET.get("page_size", None)
    account = request.user.account

    # ===== PROCESS

    diary_queryset = (
        Diary.objects
        .filter(
            account=account,
        )
        .order_by("-created_date")
    )
    paginated_diary_queryset = paginate(diary_queryset, page, page_size)

    # ===== CONTEXT

    context = {
        "diaries": paginated_diary_queryset,
    }

    return render(request, "diaries/diaries.html", context)


@login_required
def detail(request, id: int):

    # ===== DTO

    diary = Diary.objects.get(id=id)

    # ===== CONTEXT

    context = {
        "diary": diary,
    }
    return render(request, "diaries/detail.html", context)

