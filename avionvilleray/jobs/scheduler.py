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


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(DataDumper.execute, trigger='cron', minute='*')
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()  # Not strictly necessary if daemonic mode is enabled but should be done if possible