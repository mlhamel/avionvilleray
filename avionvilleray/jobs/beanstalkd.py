import subprocess

from avionvilleray.scheduler.interface import IScheduler


class Beanstalkd:
    def __call__(self):
        subprocess.call(["beanstalkd", "-l", "127.0.0.1", "-p", "14711", "-V"])


def includeme(config):
    registry = config.registry
    scheduler = registry.getUtility(IScheduler)
    scheduler.add_job(Beanstalkd())
