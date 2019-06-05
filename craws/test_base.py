# Created by Alexander Watzinger and others. Please see README.md for licensing information
import unittest

from craws import app


class TestBaseCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        app.config['SERVER_NAME'] = 'localhost'
        self.app = app.test_client()
