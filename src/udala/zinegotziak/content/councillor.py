from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield.registry import DictRow
from plone.app.multilingual.dx.interfaces import ILanguageIndependentField
from plone.app.textfield import RichText
from plone.app.vocabularies.catalog import StaticCatalogVocabulary
from plone.app.z3cform.widgets.contentbrowser import ContentBrowserFieldWidget
from plone.app.z3cform.widgets.select import SelectFieldWidget
from plone.autoform.directives import widget
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobFile
from plone.supermodel import model
from udala.zinegotziak import _
from z3c.relationfield.schema import RelationChoice

# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import alsoProvides
from zope.interface import implementer
from zope.interface import Interface
from plone.app.dexterity import textindexer


class ISocialLinkRowSchema(Interface):
    name = schema.TextLine(title=_("Name of social network"))
    url = schema.TextLine(title=_("URL of social network"))
    iconname = schema.TextLine(title=_("Icon name"))


class IPositionRowSchema(Interface):
    position = schema.TextLine(
        title=_("Position name"),
        description=_("Ex.: Member, President, Councillor, ..."),
    )
    order = schema.TextLine(
        title=_("Order"),
        description=_(
            "The order in which this councillor will be shown "
            "in the selected Commission"
        ),
    )

    # widget("commission", SelectWidget)
    widget(
        "commission",
        ContentBrowserFieldWidget,
        pattern_options={"recentlyUsed": False, "selectableTypes": ["Commission"]},
    )
    commission = RelationChoice(
        title=_("Commission"),
        vocabulary="plone.app.vocabularies.Catalog",
        required=True,
    )


class ICouncillor(model.Schema):
    """Marker interface and Dexterity Python Schema for Zinegotzia"""

    widget("social_links", DataGridFieldFactory, allow_reorder=True)
    social_links = schema.List(
        title=_("Social network links"),
        value_type=DictRow(title=_("Social network link"), schema=ISocialLinkRowSchema),
        default=[
            {
                "name": "Twitter",
                "url": "https://twitter.com/EibarkoUdala",
                "iconname": "twitter",
            },
            {
                "name": "FaceBook",
                "url": "https://www.facebook.com/pages/Eibarko-Udala/371951916348590",
                "iconname": "facebook",
            },
            {
                "name": "Youtube",
                "url": "https://www.youtube.com/channel/UCTNEPKwdQgEuhO0S4nUGaPw",
                "iconname": "youtube",
            },
        ],
        required=False,
    )

    widget("party", SelectFieldWidget)
    party = RelationChoice(
        title=_("Party"),
        vocabulary=StaticCatalogVocabulary({"portal_type": "Party"}),
        required=True,
    )

    widget("positions", DataGridFieldFactory, allow_reorder=True)
    positions = schema.List(
        title=_("Positions"),
        value_type=DictRow(title=_("Position"), schema=IPositionRowSchema),
        default=[
            {"position": "Councillor", "commission": "", "order": "1"},
        ],
        required=False,
    )

    textindexer.searchable("other_positions")
    other_positions = RichText(
        title=_("Other positions"),
        description=_("Write here any other position that this councillor holds"),
        required=False,
    )

    textindexer.searchable("cv_text")
    cv_text = RichText(
        title=_("CV"),
        description=_(
            "Write here the CV of this councillor. You can also attach a file below."
        ),
        required=False,
    )

    textindexer.searchable("cv_file")
    cv_file = NamedBlobFile(
        title=_("CV file"),
        description=_("Upload the file with the CV of this councillor."),
        required=False,
    )

    textindexer.searchable("earnings_text")
    earnings_text = RichText(
        title=_("Earnings"),
        description=_(
            "Enter the earnings of this councillor. You can also attach a file below."
        ),
        required=False,
    )

    textindexer.searchable("earnings_file")
    earnings_file = NamedBlobFile(
        title=_("Earnings file"),
        description=_("Upload the file with the earning details of this councillor."),
        required=False,
    )

    textindexer.searchable("assets_declaration_text")
    assets_declaration_text = RichText(
        title=_("Assets declaration"),
        description=_(
            "Enter the assets declaration of this councillor. "
            "You can also attach a file below."
        ),
        required=False,
    )

    textindexer.searchable("assets_declaration_file")
    assets_declaration_file = NamedBlobFile(
        title=_("Assets declaration file"),
        description=_(
            "Upload the file with the assets declaration of this councillor."
        ),
        required=False,
    )

    textindexer.searchable("activities_declaration_text")
    activities_declaration_text = RichText(
        title=_("Activities declaration"),
        description=_(
            "Enter the activities declaration of this councillor. "
            "You can also attach a file below."
        ),
        required=False,
    )

    textindexer.searchable("activities_declaration_file")
    activities_declaration_file = NamedBlobFile(
        title=_("Activities declaration file"),
        description=_(
            "Upload the file with the activities declaration of this councillor."
        ),
        required=False,
    )


alsoProvides(ICouncillor["cv_file"], ILanguageIndependentField)
alsoProvides(ICouncillor["earnings_file"], ILanguageIndependentField)
alsoProvides(ICouncillor["assets_declaration_file"], ILanguageIndependentField)
alsoProvides(ICouncillor["activities_declaration_file"], ILanguageIndependentField)


@implementer(ICouncillor)
class Councillor(Container):
    """Content-type class for ICouncillor"""

    def get_party(self):
        return (self.party and self.party.to_object) or None
