from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse

from apps.accounts.models import Account
from apps.issues.models import Issue


@login_required
def create(request):

    # ===== DTO

    title = request.POST.get('title', '').strip()
    category = request.POST.get('category', '').strip()
    priority = request.POST.get('priority', '').strip()
    status = request.POST.get('status', '').strip()
    description = request.POST.get('description', '').strip()

    account = request.user.account

    # ===== VALIDATION

    pass

    # ===== PROCESS

    issue = Issue()
    issue.author = account
    issue.clan = account.clan
    issue.title = title
    issue.category = category
    issue.priority = priority
    issue.status = status
    issue.description = description
    issue.save()

    issue.assignees.set([])
    issue.reviewers.set([])

    return redirect('issues:issues_view')
