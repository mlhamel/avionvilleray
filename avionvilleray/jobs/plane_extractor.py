import transaction

from avionvilleray.jobs.base_job import BaseJob
from avionvilleray import models as m


class PlaneExtractor(BaseJob):
    def run(self):
        while True:
            content = self.receive()
            if self.is_valid(content):
                self.save(content)

    def save(self, content):
        with transaction.manager:
            for item in content:
                m.add(m.Event(**item))


def includeme(config):
    scheduler = BaseJob.get_scheduler(config)
    scheduler.add_job(PlaneExtractor())


def main():
    extractor = PlaneExtractor()
    extractor()


if __name__ == "__main__":
    main()
