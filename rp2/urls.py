from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect


def default_view(request):
    return redirect("clans:overview")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("authentication/", include("apps.authentication.urls", namespace="authentication")),
    path("accounts/", include("apps.accounts.urls", namespace="accounts")),
    path("issues/", include("apps.issues.urls", namespace="issues")),
    path("clans/", include("apps.clans.urls", namespace="clans")),
    path("diaries/", include("apps.diaries.urls", namespace="diaries")),
    path("", default_view),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
