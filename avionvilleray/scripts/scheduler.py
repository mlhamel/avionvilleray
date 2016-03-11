"""
ETL solution to track planes on top of Villeray

Usage:
    avion-scheduler <config>

Options:
    -h, --help            Display this message.
    -v, --verbose         Display verbose output.
"""
from pyramid.config import Configurator
from docopt import docopt

from pyramid.paster import bootstrap, setup_logging

from avionvilleray.scheduler.interface import IScheduler


def main():
    opts = docopt(__doc__)

    env = bootstrap(opts["<config>"])
    setup_logging(opts["<config>"])

    try:
        settings, closer = env['registry'].settings, env['closer']
        config = Configurator(settings=settings)

        config.include("avionvilleray.scheduler.aps_scheduler")

        scheduler = config.registry.getUtility(IScheduler)
        scheduler()
    finally:
        closer()


if __name__ == '__main__':
    main()
