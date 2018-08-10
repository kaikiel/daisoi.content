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


class IVideoDescription(model.Schema):

    title = schema.TextLine(
        title=_(u'Title'),
        required=True,
    )

    image = namedfile.NamedBlobImage(
        title=_(u'Title Icon'),
        required=True,
    )

    description = schema.Text(
        title=_(u'Description'),
        required=True,
    )

    url = schema.URI(
        title=_(u'Link'),
        required=True,
    )


@implementer(IVideoDescription)
class VideoDescription(Item):
    """
    """
