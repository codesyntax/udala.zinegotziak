from plone import api
from Products.Five.browser import BrowserView


class CouncillorView(BrowserView):
    def get_positions(self):
        positions = {}
        for item in self.get_commission_memberships():
            value = positions.setdefault(item.get("position"), [])
            value.append(item)
            positions[item.get("position")] = value

        return positions.items()

    def get_commission_memberships(self):
        def get_commmission_url(commission):
            """in some cases the object is not acquisition wrapped
            and we need to manually look for the item to get the URL
            """
            url = commission.absolute_url()
            if not url:
                content_object = api.content.get(UID=commission.UID())
                if content_object is not None:
                    url = content_object.absolute_url()

            return url

        if self.context.positions:
            for position in self.context.positions:
                commission = position.get("commission")
                yield {
                    "position": position.get("position"),
                    "commission_title": commission.Title(),
                    "commission_url": get_commmission_url(commission),
                }
