from django.urls import path

from . import views
from . import interactors


app_name = "diaries"


# Views

urlpatterns = [
    path("diaries-view/", views.diaries, name="diaries_view"),
    path("newsfeed-view/", views.newsfeed, name="newsfeed_view"),
    path("<int:id>/detail-view/", views.detail, name="detail_view")
]

# Interactors

urlpatterns += [
    path('<int:diary_id>/commit/', interactors.create_commit, name="commit"),
    # path('<int:id>/update/', interactors.update, name="update"),
]
