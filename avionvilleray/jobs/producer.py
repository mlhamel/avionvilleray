from avionvilleray.services.dump1090 import Dump1090Client
from avionvilleray.jobs.base_job import BaseJob
from avionvilleray.lib import jsonutil


class ProducerJob(BaseJob):
    def run(self, host):
        client = Dump1090Client(host=host)
        content = client.receive()
        return self.send(content)


def includeme(config):
    scheduler = BaseJob.get_scheduler(config)
    scheduler.add_job(ProducerJob(), trigger='cron', minute='*',
                      second="*/5")
