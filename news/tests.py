from django.test import TestCase
from .models import Author
# Create your tests here.


class AuthorTestCase(TestCase):

    def setUp(self):

        Author.objects.create(first_name='Jack', last_name='Crew',)
        Author.objects.create(first_name='Jill', last_name='Creamer', )

    def test_authors_full_name(self):

        author1 = Author.objects.get(first_name__icontains='jack')

        self.assertEquals(author1.first_name, 'Jack')
        self.assertEquals(author1.full_name(), 'Jack Crew')