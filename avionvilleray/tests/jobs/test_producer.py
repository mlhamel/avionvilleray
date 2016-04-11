import vcr

from unittest.mock import MagicMock, Mock

from avionvilleray.tests.abstract_test_case import AbstractTestCase
from avionvilleray.jobs.producer import ProducerJob
from avionvilleray.lib import jsonutil


class TestProducerJob(AbstractTestCase):
    def setUp(self):
        AbstractTestCase.setUp(self)

        self.job = ProducerJob()
        self.expected = [{'lon': -73.571085,
                          'track': 100,
                          'speed': 311,
                          'altitude': 5100,
                          'hex': '740527',
                          'lat': 45.554443,
                          'flight': 'RJA6102 '}]

    @vcr.use_cassette('fixtures/vcr/jobs/producer/get_content.yaml')
    def test_get_content(self):
        url = "http://{host}/data.json".format(host=self.host)
        result = self.job.get_content(url)
        self.assertEqual(result, self.expected)

    @vcr.use_cassette('fixtures/vcr/jobs/producer/run.yaml')
    def test_run(self):
        connection = Mock()
        connection.put = MagicMock(return_value=True)

        self.job.get_connection = MagicMock(return_value=connection)
        self.job.run(host=AbstractTestCase.host)

        content = jsonutil.encode(self.expected)

        connection.put.assert_called_once_with(content)
