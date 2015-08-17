# -*- coding: utf-8 -*-


def includeme(config):
    config.add_route("favicon", "/favicon.ico")
    config.add_route("index", "/")

    config.scan()
