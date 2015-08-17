"""Support for automatically compiling SCSS files."""

from __future__ import absolute_import

import logging
import os

import scss

from contextlib import contextmanager

_scss_opts = dict()

log = logging.getLogger(__name__)


@contextmanager
def chdir(path):
    old_dir = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(old_dir)


def initialize(static_url, static_root):
    """Configure default values for the pyScss package."""
    scss.STATIC_ROOT = static_root
    scss.ASSETS_ROOT = os.path.sep.join([scss.STATIC_ROOT, 'assets', ''])
    scss.STATIC_URL = '%s/' % static_url
    scss.ASSETS_URL = '%s/%s/' % (static_url, 'assets')


def compile(assets_dir, options):
    """Compile SCSS files if they have changed.

    Partly based on https://bitbucket.org/sjl/flask-lesscss

    """
    scss_paths = []
    compiler = scss.Scss(scss_opts=options)

    for path, subdirs, filenames in os.walk(assets_dir):
        scss_paths.extend([os.path.join(path, f)
                           for f in filenames
                           if os.path.splitext(f)[1] == '.scss'
                           and not f.startswith('_')])

    with chdir(assets_dir):
        for scss_path in scss_paths:
            css_path = os.path.splitext(scss_path)[0] + '.css'
            if not os.path.isfile(css_path):
                css_mtime = -1
            else:
                css_mtime = os.path.getmtime(css_path)

            if os.path.getmtime(scss_path) >= css_mtime:
                try:
                    compiled = compiler.compile(open(scss_path).read())
                    with open(css_path, 'w') as f:
                        f.write(compiled)
                    log.info('Compiled scss file: %s' % scss_path)
                except:
                    log.debug("Can't compile scss file: %s" % scss_path)
