from avionvilleray.jobs.base_job import BaseJob


class PlaneExtractor(BaseJob):
    def __call__(self):
        return self.run

    def run(self):
        while True:
            content = self.read()
            if self.is_valid(content):
                self.save(content)

    def save(self, content):


def includeme(config):
    scheduler = BaseJob.get_scheduler(config)
    scheduler.add_job(PlaneExtractor())


def main():
    extractor = PlaneExtractor()
    extractor()


if __name__ == "__main__":
    main()
