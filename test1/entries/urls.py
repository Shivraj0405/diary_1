# entries/urls.py

from django.urls import path

from . import views

urlpatterns = [

    path(
        "",
        views.EntryListView.as_view(),
        name="entry_list"
    ),
    path(
        "entry/<int:pk>",
        views.EntryDetailsView.as_view(),
        name="entry_detail"
    ),
]
