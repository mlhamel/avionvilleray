import unittest

from pyramid import testing


class AbstractTestCase(unittest.TestCase):
    host = "127.0.0.1:8080"

    def setUp(self):
        testing.setUp()

    def tearDown(self):
        testing.tearDown()
