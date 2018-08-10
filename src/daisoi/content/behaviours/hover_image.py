# -*- coding: utf-8 -*-
from daisoi.content import _
from plone import schema
from plone.supermodel import model
from plone.namedfile.field import NamedBlobImage, NamedBlobFile, NamedImage
from zope.interface import implementer
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from zope.interface import provider
from zope.component import adapter

@provider(IFormFieldProvider)
class IHoverImg(model.Schema):

    hoverImg = NamedBlobImage(
        title=_(u'Image2'),
        required=False,
    )


@implementer(IHoverImg)
@adapter(IDexterityContent)
class HoverImg(object):
    def __init__(self, context):
        self.context = context

    @property
    def hoverImg(self):
        if hasattr(self.context, 'hoverImg'):
            return self.context.hoverImg
        return None

    @hoverImg.setter
    def hoverImg(self, value):
        self.context.hoverImg = value

