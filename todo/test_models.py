from django.test import TestCase
from .models import item

class TestModels(TestCase):
    def test_done_defaults_to_false(self):
        items = item.objects.create(name="Test todo item")
        self.assertFalse(items.done)

# Test the string method
    def test_item_string_returns_name(self):
         items = item.objects.create(name="Test todo item")
         self.assertEqual(str(items), "Test todo item")