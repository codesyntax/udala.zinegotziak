# -*- coding: utf-8 -*-

# from udala.zinegotziak import _
from plone import api
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class IZinegotziakView(Interface):
    """ Marker Interface for IZinegotziakView"""


@implementer(IZinegotziakView)
class ZinegotziakView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('zinegotziak_view.pt')

    def alderdi_eta_zinegotziak(self):
        brains = api.content.find(
            portal_type="Alderdia", sort_on="getObjPositionInParent",
            Language=self.context.Language(),
        )
        alderdiak = []
        for brain in brains:
            alderdia = brain.getObject()
            alderdia_dict = {"item": alderdia}

            zinegotziak_brains = api.content.find(
                                alderdia=brain.UID,
                                portal_type="Zinegotzia",
                                Language=self.context.Language(),
                                sort_on="getObjPositionInParent")
            zinegotziak_list = []
            for zinegotzia_brain in zinegotziak_brains:
                zinegotzia = zinegotzia_brain.getObject()

                zinegotziak_list.append(zinegotzia)

            alderdia_dict["zinegotziak"] = zinegotziak_list
            alderdiak.append(alderdia_dict)

        return alderdiak
