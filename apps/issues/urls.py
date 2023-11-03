from django.urls import path

from . import views
from . import interactors


app_name = "issues"


# Views

urlpatterns = [
    path("issues-view", views.issues, name="issues_view"),
    path("create-view", views.create, name="create_view")
]

# Interactors

urlpatterns += [
    path('create/', interactors.create, name="create"),
    # path('<int:id>/update/', interactors.update, name="update"),
]
