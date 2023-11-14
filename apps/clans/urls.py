from django.urls import path

from . import views
from . import interactors


app_name = "clans"


# Views

urlpatterns = [
    path("overview/", views.overview, name="overview"),
]

# Interactors

urlpatterns += [
]
