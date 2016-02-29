import unittest
from pyramid import testing


class TestApsScheduler(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()
