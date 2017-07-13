import logging

from pystalkd.Beanstalkd import Connection

from avionvilleray.lib import jsonutil
from avionvilleray.interface import IScheduler

log = logging.getLogger(__name__)


class BaseJob(object):
    def __init__(self):
        self.connection = None

    @staticmethod
    def get_registry(config):
        return config.registry

    @staticmethod
    def get_scheduler(config):
        return BaseJob.get_registry(config).getUtility(IScheduler)

    def get_connection(self):
        if not self.connection:
            self.connection = Connection(host='localhost', port=11300)
        return self.connection

    def receive(self):
        job = None
        try:
            job = self.get_connection().reserve()
            body = jsonutil.decode(job.body)
            log.debug("Getting job {body}".format(body=body))
            return body
        finally:
            if job:
                job.delete()

    def send(self, content):
        log.debug("Saving: {content}".format(content=content))

        value = jsonutil.encode(content)
        connection = self.get_connection()

        return connection.put(value)
