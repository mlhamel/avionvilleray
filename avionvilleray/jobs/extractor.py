import transaction

from avionvilleray.jobs.base_job import BaseJob
from avionvilleray.lib import jsonutil


class ExtractorJob(BaseJob):
    def run(self, host="127.0.0.1:8080"):
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
    extractor = ExtractorJob()
    extractor.run()


if __name__ == "__main__":
    main()
