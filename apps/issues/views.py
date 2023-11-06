from django.shortcuts import render

from rp2.pagination import paginate

from ..issues.models import Issue


def issues(request):

    # ===== DTO

    page = request.GET.get("page", 1)
    title = request.GET.get("title", "")

    # ===== PROCESS

    account = request.user.account
    issue_queryset = (
        Issue.objects
        .filter(
            clan=account.clan,
            title__icontains=title,
        )
        .order_by("-id")
    )
    paginated_issue_queryset = paginate(issue_queryset, page)

    # ===== CONTEXT

    context = {
        "issues": paginated_issue_queryset,
    }

    return render(request, "issues/issues.html", context)


def create(request):
    return render(request, "issues/create.html")

