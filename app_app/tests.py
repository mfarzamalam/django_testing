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