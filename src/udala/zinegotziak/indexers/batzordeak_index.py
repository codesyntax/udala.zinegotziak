# -*- coding: utf-8 -*-

from udala.zinegotziak.content.zinegotzia import IZinegotzia
from plone.dexterity.interfaces import IDexterityContent
from plone.indexer import indexer


@indexer(IDexterityContent)
def dummy(obj):
    """ Dummy to prevent indexing other objects thru acquisition """
    raise AttributeError('This field should not indexed here!')


@indexer(IZinegotzia)  # ADJUST THIS!
def batzordeak_index(obj):
    """Calculate and return the value for the indexer"""
    items = []
    for kargua in obj.karguak:
        batzordea = kargua.get("batzordea", None)
        if batzordea is not None:
            items.append(batzordea)

    return items
