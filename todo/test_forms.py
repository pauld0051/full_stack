from django.test import TestCase
from .forms import ItemForm

# Create your tests here.


class TestDjango(TestCase):
    def test_name_is_required(self):
        # This would suggest a blank field
        form = ItemForm({'name': ""}) 
        # This will look to see if the field tested is valid
        self.assertFalse(form.is_valid())
        # When a form is invalid a dict of errors will return
        # So we can assertIn and see if there is a name key in the form of errors
        self.assertIn('name', form.errors.keys())
        # We can now look to see if this is the string that is returned
        # The [0] index just looks for the list of each errors in the field
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_is_not_required(self):
        # Because the done status is NOT REQUIRED test to see if the form passes 
        # when a filled in form is added
        form = ItemForm({'name': "New todo form"})
        self.assertTrue(form.is_valid())

    def test_form_is_explicit_in_meta_class(self):
        # Because we have defined form names, we do not want excess forms that
        # may be hidden from the user to display. 
        # Create a blank form and make sure it only has the meta classes name and done associated
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
        # If someone were to change the form later down the road, then only the meta displays are seen