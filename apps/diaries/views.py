from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from rp2.pagination import paginate

from .models import Diary


@login_required
def diaries(request):
    pass


@login_required
def detail(request, id: int):

    # ===== DTO

    diary = Diary.objects.get(id=id)

    # ===== CONTEXT

    context = {
        "diary": diary,
    }
    return render(request, "diaries/detail.html", context)

