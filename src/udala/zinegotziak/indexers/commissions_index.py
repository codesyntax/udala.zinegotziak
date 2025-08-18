from plone.dexterity.interfaces import IDexterityContent
from plone.indexer import indexer
from udala.zinegotziak.content.councillor import ICouncillor


@indexer(IDexterityContent)
def dummy(obj):
    """Dummy to prevent indexing other objects thru acquisition"""
    raise AttributeError("This field should not indexed here!")


@indexer(ICouncillor)  # ADJUST THIS!
def commissions_index(obj):
    """Calculate and return the value for the indexer"""
    items = []
    if obj.positions:
        for position in obj.positions:
            commission = position.get("commission", None)
            if commission is not None:
                items.append(commission.UID())

    return items
