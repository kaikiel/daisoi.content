# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from daisoi.content import _


class IPhilosophy(model.Schema):
    title = schema.TextLine(
        title=_(u'title'),
        required=True,
    )

    philosophy_description = RichText(
        title=_(u'philosophy description'),
        required=True,
    )

    philosophy_img = namedfile.NamedBlobImage(
        title=_(u'philosophy Image'),
        required=True,
    )

    text_title_img = namedfile.NamedBlobImage(
        title=_(u'text title Image'),
        required=True,
    )

    philosophy_text = schema.Text(
        title=_(u'philosophy text'),
        required=True,
    )

    text_img = namedfile.NamedBlobImage(
        title=_(u'philosophy Text Image'),
        required=True,
    )

    philosophy_body = RichText(
        title=_(u'philosophy body'),
        required=True,
    )


@implementer(IPhilosophy)
class Philosophy(Item):
    """
    """
