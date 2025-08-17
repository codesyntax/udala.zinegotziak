from plone import api
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class IParty(model.Schema):
    """Marker interface and Dexterity Python Schema for Party"""


@implementer(IParty)
class Party(Container):
    """Content-type class for IParty"""

    def get_councillors(self):
        """get the councillors of this party"""
        party_relations = api.relation.get(target=self, relationship="party")
        return [party_relation.from_object for party_relation in party_relations]
