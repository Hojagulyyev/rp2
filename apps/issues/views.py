from django.shortcuts import render

from rp2.pagination import paginate

from ..issues.models import Issue


def issues(request):

    account = request.user.account

    # ===== Input DTO

    page = request.GET.get("page", 1)
    title = request.GET.get("title", "")

    # ===== Output DTO

    issue_queryset = Issue.objects.filter(
        clan=account.clan,
        title__icontains=title,
    )
    paginated_issue_queryset = paginate(issue_queryset, page)

    context = {
        "issues": paginated_issue_queryset,
    }

    return render(request, "issues/issues.html", context)


def create(request):
    return render(request, "issues/create.html")

