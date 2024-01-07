import unittest

from craws import app


class TestBaseCase(unittest.TestCase):

    def setUp(self) -> None:
        app.testing = True
        app.config['SERVER_NAME'] = 'local.host'
        self.app = app.test_client()


class CrawsTests(TestBaseCase):

    def test_sites(self) -> None:
        assert b'Creating Reality' in self.app.get('/').data
        assert b'Software Development' in self.app.get('/team').data
        assert b'404' in self.app.get('/go to the main page').data
