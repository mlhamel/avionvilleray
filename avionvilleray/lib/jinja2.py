# -*- coding: utf-8 -*-

""" Pyramid Configuration for jinja2 """

from pyramid.threadlocal import get_current_request

from markupsafe import Markup
from markdown2 import markdown

from babel.dates import format_date, format_datetime


def add_renderer_globals(app_name, event):
    """A subscriber to the ``pyramid.events.BeforeRender`` events.  Updates
    the :term:`renderer globals` with values that are familiar to Pylons
    users."""
    request = event.get('request')
    if request is None:
        request = get_current_request()

    def _path(*args, **kwargs):
        return request.route_path(*args, **kwargs)

    def _static_path(asset):
        return request.static_path('%s:static/%s' % (app_name, asset))

    globs = dict()

    if request is not None:
        if hasattr(request, "translate"):
            globs['_'] = request.translate
        globs['localizer'] = request.localizer
        globs['path'] = _path
        globs['static_path'] = _static_path

    event.update(globs)


def includeme(config):
    jinja_env = config.get_jinja2_environment()

    jinja_env.globals['sorted'] = sorted
    jinja_env.globals['int'] = int
    jinja_env.globals['zip'] = zip
    jinja_env.globals['len'] = len
    jinja_env.filters['markdown'] = lambda x: Markup(markdown(x))
    jinja_env.filters['format_date'] = format_date
    jinja_env.filters['format_datetime'] = format_datetime
