from django.test import TestCase


class BlogModelTests(TestCase):

    def test_one(self):
        """
        test_one
        python3.9 ./server/manage.py test blog
        """
        self.assertIs("asdf", "asdfasasdf")
