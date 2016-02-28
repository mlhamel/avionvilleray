from pyramid.threadlocal import get_current_registry
from avionvilleray.scheduler.interface import IScheduler
from pystalkd.Beanstalkd import Connection

import requests


class PlaneProducer:
    def get_connection(self):
        return Connection(host='localhost', port=11300)

    def get_url(self, host):
        return "http://{host}/data.json".format(host=host)

    def get_content(self, url):
        content = requests.get(url).content
        return content.decode("utf8")

    def __call__(self, host="127.0.0.1:8080"):
        url = self.get_url(host)
        content = self.get_content(url)
        connection = self.get_connection()
        print("Saving: {content}".format(content=content))
        connection.put(content)


def includeme(config):
    registry = config.registry
    scheduler = registry.getUtility(IScheduler)
    scheduler.add_job(PlaneProducer(), trigger='cron', minute='*',
                      second="*/5")


def main():
    producer = PlaneProducer()
    producer()


if __name__ == "__main__":
    main()
