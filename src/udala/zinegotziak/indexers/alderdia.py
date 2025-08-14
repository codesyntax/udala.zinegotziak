# -*- coding: utf-8 -*-

from udala.zinegotziak.content.zinegotzia import IZinegotzia
from plone.dexterity.interfaces import IDexterityContent
from plone.indexer import indexer


@indexer(IDexterityContent)
def dummy(obj):
    """ Dummy to prevent indexing other objects thru acquisition """
    raise AttributeError('This field should not indexed here!')


@indexer(IZinegotzia)  # ADJUST THIS!
def alderdia(obj):
    """Calculate and return the value for the indexer"""
    return obj.alderdia
