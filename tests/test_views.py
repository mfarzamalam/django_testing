from django.test import TestCase
from app_app.models import Author


class ModelAuthorTestCase(TestCase):

    @classmethod
    def setUpTestData(self):
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        print("METHOD: test_first_name_label")
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_date_of_death_label(self):
        print("METHOD: test_date_of_death_label")
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEqual(field_label, 'Died')

    def test_object_name_is_last_comma_first_name(self):
        print("METHOD: test_object_name_is_last_comma_first_name")
        author = Author.objects.get(id=1)
        field_label = f'{author.last_name}, {author.first_name}'
        self.assertEqual(field_label, 'Bob, Big')

    def test_get_absolute_url(self):
        print("METHOD: test_get_absolute_url")
        author = Author.objects.get(id=1)
        self.assertEqual('/author/1/', author.get_absolute_url())

