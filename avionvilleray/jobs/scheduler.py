"""
Demonstrates how to use the background scheduler to schedule a job that executes on 3 second intervals.
"""

from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler


from avionvilleray.jobs.data_dumper import DataDumper


def tick():
    print('Tick! The time is: %s' % datetime.now())


def main():
    scheduler = BackgroundScheduler()
    scheduler.add_job(DataDumper.execute, trigger='cron', minute='*')
    scheduler.start()
    print("Avion Villeray: Scheduler Started")
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()


if __name__ == '__main__':
    main()
