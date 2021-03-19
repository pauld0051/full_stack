from django.test import TestCase
from .models import item

# Create your tests here.

class TestViews(TestCase):

    # Test if we can get the home page
    def test_get_todo_list(self):
        # We only need the '/' because this is the homepage
        response = self.client.get('/')
        # Assert that the response is a 200 "successful HTTP response"
        self.assertEqual(response.status_code, 200)
        # Make sure the template used is the one we want
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    # Test the add_item page
    def test_add_item(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    # Test the edit_item page
    def test_edit_item(self):
        # Because we have a <item_id> with this one, we need to parse an id to check
        # So we will create an item to test in this test
        items = item.objects.create(name="Test Item 1")
        # The "f" is a template literal to tell python to convert the {item.id} into a string
        response = self.client.get(f'/edit/{items.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    # Test if we can add, delete, and toggle items
    def test_can_add_item(self):
        # test that you can add a post
        response = self.client.post('/add', {"name": "Test can add"})
        # test that once added, redirects occur
        self.assertRedirects(response, "/")

    def test_can_toggle_item(self):
        items = item.objects.create(name="Test Item 1", done=True)
        response = self.client.get(f'/toggle/{items.id}')
        self.assertRedirects(response, "/")
        updated_item = item.objects.get(id=items.id)
        self.assertFalse(updated_item.done)

    def test_can_delete_item(self):
        # Create an item to delete
        items = item.objects.create(name="Test Item 1")
        response = self.client.get(f'/delete/{items.id}')
        self.assertRedirects(response, "/")
        existing_items = item.objects.filter(id=items.id)
        self.assertEqual(len(existing_items), 0)

    # Test the post method
    def test_can_edit_item(self):
        # Create an item to edit
        items = item.objects.create(name="Test Item 1")
        # The "f" is a template literal to tell python to convert the {item.id} into a string
        response = self.client.post(f'/edit/{items.id}', {'name': 'updated name'})
        self.assertRedirects(response, "/")
        updated_item = item.objects.get(id=items.id)
        self.assertEqual(updated_item.name, 'updated name')