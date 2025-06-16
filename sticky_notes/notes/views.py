from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Note


# View to list all notes
class NoteListView(ListView):
    model = Note
    template_name = "notes/note_list.html"
    context_object_name = (
        "notes"  # So you can use `{% for note in notes %}` in the template
    )

    def get_queryset(self):
        notes = Note.objects.all()
        print("DEBUG: Notes in DB:", notes)
        return notes


# View to create a new note
class NoteCreateView(CreateView):
    model = Note
    template_name = "notes/note_form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("note-list")  # Redirect after successful creation


# View to update an existing note
class NoteUpdateView(UpdateView):
    model = Note
    template_name = "notes/note_form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("note-list")


# View to delete a note
class NoteDeleteView(DeleteView):
    model = Note
    template_name = "notes/note_confirm_delete.html"
    success_url = reverse_lazy("note-list")
