import time

from apscheduler.schedulers.background import BackgroundScheduler

from zope.interface import implementer

from avionvilleray.scheduler.interface import IScheduler


@implementer(IScheduler)
class ApsScheduler(BackgroundScheduler):
    def __init__(self, *args, **kwargs):
        super(ApsScheduler, self).__init__(*args, **kwargs)

    def __call__(self):
        self.start()
        print("Avion Villeray: Scheduler Started")
        print('Press Ctrl+c to exit')

        try:
            while True:
                time.sleep(2)
        except (KeyboardInterrupt, SystemExit):
            self.shutdown()


def includeme(config):
    config.registry.registerUtility(ApsScheduler())

    config.include("avionvilleray.jobs.dump1090")
    config.include("avionvilleray.jobs.beanstalkd")
    config.include("avionvilleray.jobs.plane_extractor")
    config.include("avionvilleray.jobs.plane_producer")
