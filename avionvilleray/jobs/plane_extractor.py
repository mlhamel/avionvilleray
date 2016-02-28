from avionvilleray.scheduler.interface import IScheduler
from pystalkd.Beanstalkd import Connection


class PlaneExtractor:
    def get_connection(self):
        return Connection(host='localhost', port=11300)

    def __call__(self):
        connection = self.get_connection()
        while True:
            job = connection.reserve()
            print("Getting job {body}".format(body=job.body))
            job.delete()


def includeme(config):
    registry = config.registry
    scheduler = registry.getUtility(IScheduler)
    scheduler.add_job(PlaneExtractor())


def main():
    extractor = PlaneExtractor()
    extractor()


if __name__ == "__main__":
    main()
