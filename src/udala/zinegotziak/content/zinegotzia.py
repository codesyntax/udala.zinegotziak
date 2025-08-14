# -*- coding: utf-8 -*-
# from plone.autoform import directives
from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield.registry import DictRow
from plone.app.multilingual.dx.interfaces import ILanguageIndependentField
from plone.app.textfield import RichText
from plone.autoform.directives import widget
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobFile
from plone.supermodel import model
from udala.zinegotziak import _
from udala.zinegotziak.views.vocabutils import vocab_term_title

# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import alsoProvides
from zope.interface import implementer
from zope.interface import Interface


class ISocialLinkRowSchema(Interface):
    name = schema.TextLine(title=_("Name of social network"))
    url = schema.TextLine(title=_("URL of social network"))
    cssclass = schema.TextLine(title=_("CSS Class to be applied to this item"))


class IKarguaRowSchema(Interface):
    kargua = schema.TextLine(title=_("Karguaren izena"))
    ordena = schema.TextLine(
        title=_("Ordena"),
        description="Zinegotzi hau, aukeratutako batzordean zein posiziotan agertuko den adierazten du.",
    )
    batzordea = schema.Choice(
        title=_("batzordea"),
        vocabulary="udala.zinegotziak.BatzordeakVocabulary",
    )


class IZinegotzia(model.Schema):
    """Marker interface and Dexterity Python Schema for Zinegotzia"""

    widget("sociallinks", DataGridFieldFactory, allow_reorder=True)
    sociallinks = schema.List(
        title=_("sociallinks"),
        value_type=DictRow(title=_("sociallinks"), schema=ISocialLinkRowSchema),
        default=[
            {
                "name": "Twitter",
                "url": "https://twitter.com/EibarkoUdala",
                "cssclass": "twitter",
            },
            {
                "name": "FaceBook",
                "url": "https://www.facebook.com/pages/Eibarko-Udala/371951916348590",
                "cssclass": "facebook",
            },
            {
                "name": "Youtube",
                "url": "https://www.youtube.com/channel/UCTNEPKwdQgEuhO0S4nUGaPw",
                "cssclass": "youtube",
            },
        ],
        required=False,
    )

    alderdia = schema.Choice(
        title=_("alderdia"),
        vocabulary="udala.zinegotziak.AlderdiakVocabulary",
        required=True,
    )

    widget("karguak", DataGridFieldFactory, allow_reorder=True)
    karguak = schema.List(
        title=_("karguak"),
        value_type=DictRow(title=_("karguak"), schema=IKarguaRowSchema),
        default=[
            {"kargua": "Zinegotzia", "batzordea": "", "ordena": "1"},
        ],
        required=False,
    )

    bestelako_karguak = RichText(
        title=_("Bestelako karguak"),
        required=False,
    )

    cv_text = RichText(
        title=_("CV"),
        required=False,
    )

    cv_file = NamedBlobFile(title="CV fitxategia", required=False)

    dirusarrerak_text = RichText(
        title=_("Diru sarrerak"),
        required=False,
    )

    dirusarrerak_file = NamedBlobFile(title="Dirusarrerak fitxategia", required=False)

    ondasunenaitorpena_text = RichText(
        title=_("Ondasunen aitorpena"),
        required=False,
    )

    ondasunenaitorpena_file = NamedBlobFile(
        title="Ondasunen aitorpena fitxategia", required=False
    )

    jarduerenaitorpena_text = RichText(
        title=_("Jardueren aitorpena"),
        required=False,
    )

    jarduerenaitorpena_file = NamedBlobFile(
        title="Jardueren aitorpena fitxategia", required=False
    )


alsoProvides(IZinegotzia["cv_file"], ILanguageIndependentField)
alsoProvides(IZinegotzia["dirusarrerak_file"], ILanguageIndependentField)
alsoProvides(IZinegotzia["ondasunenaitorpena_file"], ILanguageIndependentField)
alsoProvides(IZinegotzia["jarduerenaitorpena_file"], ILanguageIndependentField)


@implementer(IZinegotzia)
class Zinegotzia(Container):
    """Content-type class for IZinegotzia"""

    def get_alderdia(self):
        return vocab_term_title(
            self, "udala.zinegotziak.AlderdiakVocabulary", self.alderdia
        )
