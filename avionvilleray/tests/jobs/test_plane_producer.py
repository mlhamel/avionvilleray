import unittest
import vcr

from unittest.mock import MagicMock, Mock

from pyramid import testing
from avionvilleray.jobs.plane_producer import PlaneProducer


class TestPlaneProducer(unittest.TestCase):
    host = "127.0.0.1:8080"

    def setUp(self):
        self.config = testing.setUp()
        self.job = PlaneProducer()

    def tearDown(self):
        testing.tearDown()

    @vcr.use_cassette('fixtures/vcr/jobs/plane_producer/get_content.yaml')
    def test_get_content(self):
        url = "http://{host}/data.json".format(host=self.host)
        self.assertEqual(self.job.get_content(url),
                         [{'lon': -73.571085,
                           'track': 100,
                           'speed': 311,
                           'altitude': 5100,
                           'hex': '740527',
                           'lat': 45.554443,
                           'flight': 'RJA6102 '}])

    @vcr.use_cassette('fixtures/vcr/jobs/plane_producer/run.yaml')
    def test_run(self):
        connection = Mock()
        connection.send = MagicMock(return_value=True)
        connection.send.assert_called_once()

        self.job.get_connection = MagicMock(return_value=connection)
        self.job.run(self.host)
