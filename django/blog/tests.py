from django.test import TestCase
from blog.models import Entry

class EntryTests(TestCase):
    def test_str(self):
        my_title = Entry(title='this is a basic title for test case')
        self.assertEquals(
            str(my_title), 'this is a basic title for test case'
        )
