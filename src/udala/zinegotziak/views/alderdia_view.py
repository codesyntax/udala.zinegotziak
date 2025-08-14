# -*- coding: utf-8 -*-

# from udala.zinegotziak import _
from plone import api
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IAlderdiaView(Interface):
    """Marker Interface for IAlderdiaView"""


@implementer(IAlderdiaView)
class AlderdiaView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('alderdia_view.pt')

    def zinegotziak(self):
        # Implement your own actions:
        zinegotziak_brains = api.content.find(
            alderdia=self.context.UID(),
            portal_type="Zinegotzia",
            Language=self.context.Language(),
            sort_on="getObjPositionInParent",
        )
        zinegotziak_list = []
        for zinegotzia_brain in zinegotziak_brains:
            zinegotziak_list.append(zinegotzia_brain.getObject())
        return zinegotziak_list
