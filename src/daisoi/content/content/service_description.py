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


class IServiceDescription(model.Schema):
    service_description = schema.Text(
        title=_(u'Service description'),
        required=True,
    )

    description_img = namedfile.NamedBlobImage(
        title=_(u'description Image'),
        required=True,
    )

    img_top_text = schema.TextLine(
        title=_(u'Imgae description top text'),
        required=True,
    )

    service_img = namedfile.NamedBlobImage(
        title=_(u'Service Image'),
        required=True,
    )

    img_bottom_text = schema.TextLine(
        title=_(u'Image description bottom text'),
        required=True,
    )


@implementer(IServiceDescription)
class ServiceDescription(Item):
    """
    """
