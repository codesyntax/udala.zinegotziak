from plone.restapi.interfaces import IJsonCompatible
from udala.zinegotziak.content.commission import ICommission
from zope.component import adapter
from zope.interface import implementer


@adapter(ICommission)
@implementer(IJsonCompatible)
def commission_converter(value):
    """
    We need a custom converter form Commission objects
    because we are saving a RelationField in a datagridfield

    And when serializing it for the REST API we need to convert
    it to the object's UID to be properly handled
    """
    if value is None:
        return value

    if type(value) in (str, bool, int, float, int):
        return value

    return value.UID()
