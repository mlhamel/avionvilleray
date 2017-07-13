"""
ETL solution to track planes on top of Villeray

Usage:
    avion-collector <config>

Options:
    -h, --help            Display this message.
    -v, --verbose         Display verbose output.
"""
import requests

from pyramid.config import Configurator
from docopt import docopt

from pyramid.paster import bootstrap, setup_logging

from avionvilleray.interface import ICollector


def main():
    opts = docopt(__doc__)

    env = bootstrap(opts["<config>"])
    setup_logging(opts["<config>"])

    try:
        settings, closer = env['registry'].settings, env['closer']
        config = Configurator(settings=settings)

        config.include("avionvilleray.scheduler.aps_scheduler")

        collector = config.registry.getUtility(ICollector)
        collector.collect()
    finally:
        closer()


if __name__ == '__main__':
    main()
