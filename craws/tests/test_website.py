# Created by Alexander Watzinger. Please see README.md for licensing information
from craws.test_base import TestBaseCase


class CrawsTests(TestBaseCase):

    def test_sites(self):
        assert b'Creating Reality' in self.app.get('/').data
        assert b'Software Development' in self.app.get('/team').data
        assert b'404' in self.app.get('/go to the main page').data
