from django.shortcuts import render

from ..issues.models import Issue


def issues(request):

    account = request.user.account

    # ===== Output DTO

    issue_queryset = Issue.objects.filter(
        clan=account.clan,
    )

    context = {
        "issues": issue_queryset,
    }

    return render(request, "issues/issues.html", context)


def create(request):
    return render(request, "issues/create.html")

