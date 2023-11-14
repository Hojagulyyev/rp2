from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from django.contrib import messages
from django.urls import reverse

from apps.accounts.models import Account


def signup(request):

    # ===== DTO

    username = request.POST.get('signup_username', '').strip()
    password = request.POST.get('signup_password', '').strip()
    repeat_password = request.POST.get('signup_repeat_password', '').strip()
    first_name = request.POST.get('signup_first_name', '').strip()
    last_name = request.POST.get('signup_last_name', '').strip()

    # ===== VALIDATION

    if password != repeat_password:
        messages.error(request, "Passwords are mismatching")
        return redirect(
            f"{reverse('authentication:authentication_view')}"
            f"?username={username}"
        )

    # ===== PROCESS

    try:
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
    except Exception as e:
        messages.error(request, str(e))
        return redirect(
            f"{reverse('authentication:authentication_view')}"
        )

    Account.objects.create(user=user)

    return redirect('authentication:authentication_view')


def signin(request):
    username = request.POST.get('signin_username', '').strip()
    password = request.POST.get('signin_password', '').strip()

    user = authenticate(username=username, password=password)

    if user is None:
        messages.error(request, "These credentials are incorrect")
        return redirect(
            f"{reverse('authentication:authentication_view')}"
            f"?username={username}"
        )

    login(request, user)
    return redirect('clans:overview')


@login_required
def signout(request):
    logout(request)
    return redirect('authentication:authentication_view')
