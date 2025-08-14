# -*- coding: utf-8 -*-

# from udala.zinegotziak import _
from udala.zinegotziak.views.vocabutils import vocab_term_title
from plone import api
from Products.CMFPlone.CatalogTool import getObjPositionInParent
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class IBatzordeaView(Interface):
    """ Marker Interface for IBatzordeaView"""


@implementer(IBatzordeaView)
class BatzordeaView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('batzordea_view.pt')

    def get_kideak(self):
        brains = api.content.find(
            batzordeak_index=self.context.UID(),
            portal_type="Zinegotzia",
            sort_on="getObjPositionInParent",
            Language=self.context.Language(),
        )
        zinegotziak = [brain.getObject() for brain in brains]
        batzordekideak = []
        for zinegotzia in zinegotziak:
            batzordekidea = self.get_batzordekidea(zinegotzia)
            if batzordekidea:
                batzordekideak.append(batzordekidea)
        return sorted(
            batzordekideak,
            key=lambda x: (
                int(x.get("kargua_ordena")),
                int(x.get("zinegotzia_ordena")),
            ),
        )

    def get_batzordekidea(self, zinegotzia):

        for kargua in zinegotzia.karguak:
            if kargua.get("batzordea", "") == self.context.UID():

                return_dict = {"kargua": kargua.get("kargua"),
                               "kargua_ordena": kargua.get("ordena", "1"),
                               "zinegotzia_ordena": getObjPositionInParent(zinegotzia)(),
                               "zinegotzia_title": zinegotzia.Title(),
                               "zinegotzia_url": zinegotzia.absolute_url(),
                               "alderdia": zinegotzia.get_alderdia(),
                               "item": zinegotzia}
                return return_dict
        return {}
