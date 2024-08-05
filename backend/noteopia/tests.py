from django.test import TestCase
from django.urls import reverse
import random
from .models import Note

class TestNote(TestCase):
    words = 'sup dude I got a thought kinda like an idea or whatever you call it so basically I\'m creating a notes web app and for optimization we can store the notes in the local storage when the notes load initially we\'d update those whenever any operation is done hey that\'s a solid idea man storing notes in local storage can definitely speed things up here\'s a quick breakdown of how you can handle this okay so let\'s get going on the project shall we create a check list for me regarding the project'.split()

    def setUp(self):
        note = self.create_note()
        Note.objects.create(**note)

    def create_note(self):
        title = ' '.join(random.choices(self.words, k=10))
        content = ' '.join(random.choices(self.words, k=len(self.words)))

        return {
            'title': title,
            'content': content
        }
    def test_create_notes(self):
        url = reverse('list-create-notes')
        response = self.client.post(url, self.create_note())
        self.assertEqual(response.status_code, 201)
        print('Note created successfully!')
    
    def test_list_notes(self):
        url = reverse('list-create-notes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        print('Notes listed successfully!')

    def test_update_note(self):
        url = reverse('retrieve-update-delete-note', kwargs={'pk': 1})
        data = {
            'title': 'Test Note 1',
            'content': 'This is a demo note.',
        }
        response = self.client.put(url, data=data, content_type='application/json')
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['content'], data['content'])
        print('Note updated successfully!')

    def test_delete_note(self):
        url = reverse('retrieve-update-delete-note', kwargs={'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        print('Note deleted successfully!')