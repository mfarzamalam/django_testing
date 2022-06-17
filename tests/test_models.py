from django.test import TestCase

# Create your tests here.

class MyTestCase(TestCase):
    
    # @classmethod
    # def setUpTestData(cls):
    #     print("setUpTestData")

    # def setUp(self):
    #     print("setUp")

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)