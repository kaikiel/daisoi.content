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
class ITopImg(model.Schema):

    topImg = NamedBlobImage(
        title=_(u'Top Image'),
        required=False,
    )


@implementer(ITopImg)
@adapter(IDexterityContent)
class TopImg(object):
    def __init__(self, context):
        self.context = context

    @property
    def topImg(self):
        if hasattr(self.context, 'topImg'):
            return self.context.topImg
        return None

    @topImg.setter
    def topImg(self, value):
        self.context.topImg = value


