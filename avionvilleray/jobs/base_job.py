import logging
import json

from functools import lru_cache
from collections import OrderedDict

from avionvilleray.scheduler.interface import IScheduler
from pystalkd.Beanstalkd import Connection

log = logging.getLogger(__name__)


class BaseJob(object):
    @staticmethod
    def get_registry(config):
        return config.registry

    @staticmethod
    def get_scheduler(config):
        return BaseJob.get_registry(config).getUtility(IScheduler)

    @lru_cache(maxsize=None)
    def get_connection(self):
        return Connection(host='localhost', port=11300)

    def encode(self, content):
        return json.dumps(content, sort_keys=True)

    def decode(self, content):
        return json.loads(content.decode("utf8"), object_pairs_hook=OrderedDict)

    def receive(self):
        try:
            job = self.get_connection.reserve()
            body = self.decode(job.body)
            log.debug("Getting job {body}".format(body=body))
            return body
        finally:
            job.delete()

    def send(self, content):
        log.debug("Saving: {content}".format(content=content))

        value = self.encode(content)
        connection = self.get_connection()

        return connection.put(value)
