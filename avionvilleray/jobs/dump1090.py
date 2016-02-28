import subprocess

from avionvilleray.scheduler.interface import IScheduler


class Dump1090:
    def __init__(self, path):
        self.path = path

    def __call__(self):
        subprocess.call([self.path, "--net",  "--net-beast",  "--net-ro-port",
                         "31001", "--quiet"])


def includeme(config):
    registry = config.registry
    scheduler = registry.getUtility(IScheduler)
    settings = registry.settings
    scheduler.add_job(Dump1090(settings["dump1090.path"]))
