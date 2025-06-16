from django.test import TestCase
from django.urls import reverse
from notes.models import Note


class ViewNotesTest(TestCase):
    """
    Test: Viewing the notes list.
    Args:
       - Pre-populated database with 1 note.
    Expected outcome:
       - Page loads successfully (status code 200).
       - The note title appears in the response context.
    """

    def setUp(self):
        self.note = Note.objects.create(title="View Note", content="View note content")

    def test_list_notes(self):
        response = self.client.get(reverse("note-list"))
        self.assertAlmostEqual(response.status_code, 200)
        self.assertContains(response, self.note.title)
