from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class ICommission(model.Schema):
    """Marker interface and Dexterity Python Schema for Commission"""


@implementer(ICommission)
class Commission(Container):
    """Content-type class for ICommission"""
