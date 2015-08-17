# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from pyramid.renderers import JSON


def includeme(config):
    json_renderer = JSON(indent=4)
    config.add_renderer("json", json_renderer)
