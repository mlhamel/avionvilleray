import logging
import json

from functools import lru_cache

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
        return json.dumps(content.decode("utf8"))

    def decode(self, content):
        return json.loads(content)

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
        return self.get_connection().put(self.encode(content))
