from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from rp2.pagination import paginate

from apps.accounts.models import Account


@login_required
def overview(request):

    # ===== DTO

    page = request.GET.get("page", None)
    page_size = request.GET.get("page_size", None)
    account = request.user.account

    # ===== PROCESS

    account_queryset = (
        Account.objects
        .filter(clan=account.clan)
        .order_by("-level")
    )
    paginated_account_queryset = paginate(account_queryset, page, page_size)

    # ===== CONTEXT

    context = {
        "accounts": paginated_account_queryset,
    }

    return render(request, "clans/overview.html", context)
