# from udala.zinegotziak import _
from plone import api
from Products.CMFPlone.CatalogTool import getObjPositionInParent
from Products.Five.browser import BrowserView


class CommissionView(BrowserView):
    def get_members(self):
        brains = api.content.find(
            commissions_index=self.context.UID(),
            portal_type="Councillor",
            sort_on="getObjPositionInParent",
            Language=self.context.Language(),
        )
        councillors = [brain.getObject() for brain in brains]
        members = []
        for councillor in councillors:
            member = self.get_member(councillor)
            if member:
                members.append(member)

        # Sort members, first according to their position in their own edit form
        # and then according to their position in the councillors folder
        return sorted(
            members,
            key=lambda x: (
                int(x.get("position_order")),
                int(x.get("councillor_order")),
            ),
        )

    def get_member(self, councillor):
        """get member data in a manageable dict"""

        def get_commission_object(commission):
            """in some cases the object is not acquisition wrapped
            and we need to manually look for the item
            """
            if commission is not None:
                url = commission.absolute_url()
                # If it has a proper URL it is a proper object
                if url:
                    return commission

                return api.content.get(UID=commission.UID())

            return None

        for position in councillor.positions:
            # for whatever reason it does not work to check with `is` :)
            if get_commission_object(position.get("commission", None)) == self.context:
                return {
                    "position": position.get("position"),
                    "position_order": position.get("ordena", "1"),
                    "councillor_order": getObjPositionInParent(councillor)(),
                    "councillor": councillor,
                }

        return {}
