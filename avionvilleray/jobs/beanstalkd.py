import subprocess

from avionvilleray.scheduler.interface import IScheduler
from avionvilleray.jobs.base_job import BaseJob


class Beanstalkd(BaseJob):
    def run(self):
        subprocess.call(["beanstalkd", "-l", "127.0.0.1", "-p", "14711", "-V"])


def includeme(config):
    registry = config.registry
    scheduler = registry.getUtility(IScheduler)
    scheduler.add_job(Beanstalkd())
