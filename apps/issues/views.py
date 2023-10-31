from django.shortcuts import render


def issues(request):
    return render(request, "issues/issues.html")


def create(request):
    return render(request, "issues/create.html")

