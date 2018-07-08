from unittest import TestCase
import indexhr


class TestMetaData(TestCase):

    def test_contains_version(self):
        self.assertTrue(hasattr(indexhr, '__version__'))

    def test_contains_title(self):
        self.assertTrue(hasattr(indexhr, '__title__'))

    def test_contains_author(self):
        self.assertTrue(hasattr(indexhr, '__author__'))
