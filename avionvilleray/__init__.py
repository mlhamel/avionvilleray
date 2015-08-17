# -*- coding: utf-8 -*-

from pkg_resources import get_distribution

from pyramid.config import Configurator

from git import Repo

from avionvilleray.lib.request import AvionvillerayRequest


def main(global_config, **settings):
    """This function returns a Pyramid WSGI application."""
    repo_path = get_distribution("avionvilleray").location

    settings["config_uri"] = global_config["__file__"]
    settings["asset_version"] = Repo(repo_path).head.commit.hexsha

    settings.setdefault("jinja2.i18n.domain", "avionvilleray")

    config = Configurator(settings=settings,
                          request_factory=AvionvillerayRequest)

    config.include("avionvilleray.jinja")
    config.include("avionvilleray.route")
    config.include("avionvilleray.renderers")

    static_url = config.registry.settings.get("app.static.url", "static")
    config.registry.settings["app.static.url"] = static_url
    config.add_static_view(static_url, "%s:static" % __name__.split(".")[0],
                           cache_max_age=3600)

    config.scan("avionvilleray.subscribers")
    config.scan("avionvilleray.views")

    return config.make_wsgi_app()
