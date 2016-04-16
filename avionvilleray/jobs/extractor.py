import transaction

from avionvilleray.jobs.base_job import BaseJob
from avionvilleray.lib import jsonutil
from avionvilleray import models as m


class ExtractorJob(BaseJob):
    def run(self, host):
        while True:
            content = self.receive()

            if content == {"command": "quit"}:
                break

            self.save(content)

    def save(self, content):
        with transaction.manager:
            for item in content:
                self.add_item(**item)

    def add_item(self, item):
        m.add(m.Event(**item))


def includeme(config):
    scheduler = BaseJob.get_scheduler(config)
    scheduler.add_job(ExtractorJob())


def main():
    extractor = PlaneExtractor()
    extractor()


if __name__ == "__main__":
    main()
