import unittest

from unittest.mock import MagicMock, Mock

from avionvilleray.tests.abstract_test_case import AbstractTestCase
from avionvilleray.jobs.extractor import ExtractorJob


class TestPlaneExtractor(AbstractTestCase):

    def setUp(self):
        AbstractTestCase.setUp(self)

        self.job = ExtractorJob()

        self.expected = [{'lon': -73.571085,
                          'track': 100,
                          'speed': 311,
                          'altitude': 5100,
                          'hex': '740527',
                          'lat': 45.554443,
                          'flight': 'RJA6102 '}]

    def test_quit(self):
        self.job.receive = MagicMock(return_value={"command": "quit"})
        self.job.save = Mock()
        self.job.save.assert_not_called()
        self.job.run(host=AbstractTestCase.host)
