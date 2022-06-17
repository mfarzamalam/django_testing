import imp
from django.test import TestCase
from .models import Author

# Create your tests here.

class MyDummyTestCase(TestCase):
    
    def test_false_is_false(self):
        print("METHOD: test_false_is_false.")
        self.assertFalse(False)

    def test_true_is_true(self):
        print("METHOD: test_true_is_true.")
        self.assertTrue(True)


class ModelAuthorTestCase(TestCase):

    @classmethod
    def setUpTestData(self):
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        print("METHOD: test_first_name_label")
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')