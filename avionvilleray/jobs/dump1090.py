import subprocess

from avionvilleray.scheduler.interface import IScheduler
from avionvilleray.jobs.base_job import BaseJob


class Dump1090(BaseJob):
    def run(self, path):
        subprocess.call([path, "--net",  "--net-beast",  "--net-ro-port",
                         "31001", "--quiet"])


def includeme(config):
    registry = config.registry
    scheduler = registry.getUtility(IScheduler)
    settings = registry.settings
    scheduler.add_job(Dump1090(settings["dump1090.path"]))
