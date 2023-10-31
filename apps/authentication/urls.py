from django.urls import path

from . import views
from . import interactors


app_name = "authentication"


# Views

urlpatterns = [
    path("authentication-view", views.authentication, name="authentication_view"),
]

# Interactors

urlpatterns += [
]
