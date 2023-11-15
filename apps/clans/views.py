from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Count

from rp2.pagination import paginate

from apps.accounts.models import Account
from apps.diaries.models import DiaryCommit


@login_required
def overview(request):

    # ===== DTO

    page = request.GET.get("page", None)
    page_size = request.GET.get("page_size", None)
    account = request.user.account

    # ===== PROCESS

    diary_commits_count = (
        DiaryCommit.objects
        .filter(diary__account__clan=account.clan)
        .count()
    )

    account_queryset = (
        Account.objects
        .filter(clan=account.clan)
        .annotate(
            diaries_count=Count("diaries", distinct=True),
            diary_commits_count=Count("diaries__commits", distinct=True),
        )
        .order_by("-diary_commits_count")
    )
    paginated_account_queryset = paginate(account_queryset, page, page_size)

    # ===== CONTEXT

    context = {
        "accounts": paginated_account_queryset,
        "diary_commits_count": diary_commits_count,
    }

    return render(request, "clans/overview.html", context)
