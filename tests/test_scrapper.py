from unittest import TestCase
from indexhr.scrapper import scrapped_data, _sections


class TestScrapper(TestCase):

    def setUp(self):
        self.data = scrapped_data()

    def test_data_has_been_collected(self):
        """
        It needs to have more then sections number which are there by default.
        """
        self.assertTrue(len(self.data) > len(_sections))

    def test_it_has_articles_from_all_sections(self):
        for section in _sections:
            exists = False
            for article in self.data:
                if article.get('section') == section:
                    exists = True
                    break
            self.assertTrue(exists)

    def tearDown(self):
        self.data = []
