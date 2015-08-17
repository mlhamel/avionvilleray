# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import os
import avionvilleray

from pyramid.response import FileResponse
from pyramid.view import view_config


@view_config(route_name="favicon")
def favicon_view(request):
    root = os.path.dirname(avionvilleray.__file__)
    static = request.registry.settings["app.static.url"]
    icon = os.path.join(root, static, "favicon.ico")
    return FileResponse(icon, request=request)


@view_config(route_name="index", renderer="index.jinja2")
def index(request, **kwargs):
    return dict()
