# -*- coding: utf-8 -*-

from AccessControl.unauthorized import Unauthorized
from plone import api
from Products.Five.browser import BrowserView
from zope.interface import Interface, implementer


class IZinegotziaView(Interface):
    """ Marker Interface for IZinegotziaView"""


@implementer(IZinegotziaView)
class ZinegotziaView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('zinegotzia_view.pt')

    def datuak(self):
        datuak_dict = {"title": self.context.Title()}


        alderdia = self.context.alderdia
        alderdiak_brains = api.content.find(UID = alderdia)
        if alderdiak_brains:
            alderdia_obj = alderdiak_brains[0].getObject()
            datuak_dict['alderdia'] = alderdia_obj

        return datuak_dict

    def get_karguak(self):
        karguak = {}
        for item in self.get_batzordekidetzak():
            value = karguak.setdefault(item.get("kargua"), [])
            value.append(item)
            karguak[item.get("kargua")] = value

        return karguak.items()

    def get_batzordekidetzak(self):
        for kargua in self.context.karguak:
            batzordea_id = kargua.get("batzordea")
            batzordea = self.get_item(batzordea_id)
            if batzordea is not None:
                yield {
                    "kargua": kargua.get("kargua"),
                    "batzordea": batzordea.Title(),
                    "batzordea_url": batzordea.absolute_url(),
                }

    def get_item(self, uid):
        try:
            item = api.content.get(UID=uid)
            if api.user.has_permission('View', obj=item):
                return item
        except Unauthorized:
            return None

        return None
