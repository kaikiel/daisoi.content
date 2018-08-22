# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from plone.autoform import directives
from plone.app.z3cform.widget import LinkFieldWidget
from zope.interface import implementer
from daisoi.content import _


class IBanner(model.Schema):
    s_text = schema.TextLine(
        title=_(u'small text'),
        required=False,
    )
 
    description = schema.Text(
        title=_(u'Description'),
        required=False,
    )

    image = namedfile.NamedBlobImage(
        title=_(u'Image'),
        required=True,
    )

    link_title = schema.TextLine(
        title=_(u'banner link title'),
        required=False,
    )

    directives.widget(link=LinkFieldWidget)
    link = schema.TextLine(
        title=_(u'banner link'),
        required=False,
    )


@implementer(IBanner)
class Banner(Item):
    """
    """
