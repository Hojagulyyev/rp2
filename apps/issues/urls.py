from django.urls import path

from . import views
from . import interactors


app_name = "issues"


# Views

urlpatterns = [
    path("create-view", views.create, name="create_view")
]

# Interactors

urlpatterns += [
    # path('create/', interactors.create, name="create"),
    # path('<int:id>/update/', interactors.update, name="update"),
]
