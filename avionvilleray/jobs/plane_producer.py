import requests

from avionvilleray.jobs.base_job import BaseJob


class PlaneProducer(BaseJob):
    def run(self, host="127.0.0.1:8080"):
        url = self.get_url(host)
        content = self.get_content(url)

        return self.send(content)

    def get_url(self, host):
        return "http://{host}/data.json".format(host=host)

    def get_content(self, url):
        content = requests.get(url).content
        return self.decode(content)


def includeme(config):
    scheduler = BaseJob.get_scheduler(config)
    scheduler.add_job(PlaneProducer(), trigger='cron', minute='*',
                      second="*/5")
