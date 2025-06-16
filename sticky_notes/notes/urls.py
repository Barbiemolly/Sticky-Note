from django.urls import path, include
from .views import NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView

urlpatterns = [
    path("", NoteListView.as_view(), name="note-list"),
    path("create/", NoteCreateView.as_view(), name="note-create"),
    path("edit/<int:pk>/", NoteUpdateView.as_view(), name="note-edit"),
    path("delete/<int:pk>/", NoteDeleteView.as_view(), name="note-delete"),
]
