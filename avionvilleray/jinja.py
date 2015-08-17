# -*- coding: utf-8 -*-

from urllib.parse import urlencode, quote_plus


def includeme(config):
    config.include("pyramid_jinja2")

    config.commit()

    config.add_jinja2_search_path("avionvilleray:templates")

    jinja_env = config.get_jinja2_environment()

    jinja_env.globals["enumerate"] = enumerate
    jinja_env.globals["sum"] = sum
    jinja_env.filters["urlencode"] = urlencode
    jinja_env.filters["quote_plus"] = quote_plus
