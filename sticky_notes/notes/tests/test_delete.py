from django.test import TestCase
from django.urls import reverse
from notes.models import Note


class DeleteNoteTest(TestCase):
    """
    Test: Deleting an existing note via POST.
    Args:
        - A note with title 'Delete Me'
    Expected outcome:
        - Note is removed from the database.
        - Redirect occurs after deletion.
    """

    def setUp(self):
        self.note = Note.objects.create(
            title="Note to delete", content="Delete this content"
        )

    def test_delete_note(self):
        response = self.client.post(reverse("note-delete", args=[self.note.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())
