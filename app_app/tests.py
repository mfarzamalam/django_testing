from django.test import TestCase

# Create your tests here.

class MyTestCase(TestCase):
    
    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_true_is_true(self):
        print("Method: test_true_is_true.")
        self.assertTrue(True)