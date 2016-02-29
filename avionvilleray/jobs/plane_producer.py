import requests
import json

from avionvilleray.jobs.base_job import BaseJob


class PlaneProducer(BaseJob):
    def __call__(self, host="127.0.0.1:8080"):
        return self.run(host)

    def run(self, host):
        url = self.get_url(host)
        content = self.get_content(url)
        return self.send(content)

    def get_url(self, host):
        return "http://{host}/data.json".format(host=host)

    def get_content(self, url):
        return json.loads(requests.get(url).content.decode("utf8"))


def includeme(config):
    scheduler = BaseJob.get_scheduler(config)
    scheduler.add_job(PlaneProducer(), trigger='cron', minute='*',
                      second="*/5")
