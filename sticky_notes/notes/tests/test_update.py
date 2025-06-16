from django.test import TestCase
from django.urls import reverse
from notes.models import Note


class UpdateNoteTest(TestCase):
    """
    Test: Editing an existing note via POST.
    Args:
        - Initial title: 'Old Title'
        - New title: 'Updated Title'
    Expected outcome:
        - Note's title and content are updated.
        - updated_at field is automatically populated.
    """

    def setUp(self):
        self.note = Note.objects.create(
            title="Initial title", content="Initial content"
        )

    def test_update_note(self):
        response = self.client.post(
            reverse("note-edit", args=[self.note.pk]),
            {"title": "Updated Title", "content": "Updated content"},
        )
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated Title")
        self.assertEqual(self.note.content, "Updated content")
        self.assertIsNotNone(self.note.updated_at)
