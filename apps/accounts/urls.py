from django.urls import path

from . import views
from . import interactors


app_name = "accounts"


# Views

urlpatterns = [
    path("", views.index, name="index")
]

# Interactors

urlpatterns += []
