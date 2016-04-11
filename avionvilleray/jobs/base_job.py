import logging

from functools import lru_cache

from pystalkd.Beanstalkd import Connection

from avionvilleray.lib import jsonutil
from avionvilleray.scheduler.interface import IScheduler

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

    def receive(self):
        try:
            job = self.get_connection.reserve()
            body = jsonutil.decode(job.body)
            log.debug("Getting job {body}".format(body=body))
            return body
        finally:
            job.delete()

    def send(self, content):
        log.debug("Saving: {content}".format(content=content))

        value = jsonutil.encode(content)
        connection = self.get_connection()

        return connection.put(value)
