# -*- coding: utf-8 -*-

from pyramid.request import Request


class AvionvillerayRequest(Request):
    """ Custom Request object """

    def route_active(self, name):
        """Return true of the current route is one we've expected."""
        return self.matched_route and self.matched_route.name == name

    @property
    def settings(self):
        return self.registry.settings
