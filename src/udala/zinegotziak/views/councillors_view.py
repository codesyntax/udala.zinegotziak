# from udala.zinegotziak import _
from plone import api
from Products.Five.browser import BrowserView


class CouncillorsView(BrowserView):
    def parties(self):
        brains = api.content.find(
            portal_type="Party",
            sort_on="getObjPositionInParent",
            Language=self.context.Language(),
        )
        return [brain.getObject() for brain in brains]
