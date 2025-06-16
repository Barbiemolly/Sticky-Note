from django.test import TestCase
from django.urls import reverse
from notes.models import Note
from datetime import datetime


class CreateNoteTest(TestCase):
    """
    Test: Creating a new note via POST request.
    Args:
       title: "Test Note"
       content: "This is a test."
    Expected outcome:
       - A new note is added to the database.
       - The created_at field is automatically populated.
       - The user is redirected to the note list page.
    """

    def test_create_note(self):
        response = self.client.post(
            reverse("note-create"),
            {"title": "Test Create Note", "content": "Test Content"},
        )

        # Ensure redirect after creation
        self.assertEqual(response.status_code, 302)

        # Check that the note was created
        self.assertEqual(Note.objects.count(), 1)
        note = Note.objects.first()
        self.assertEqual(note.title, "Test Create Note")
        self.assertIsNotNone(note.created_at)  # created_at should be set
