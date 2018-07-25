#!/usr/bin/python
# -*- coding: utf-8 -*-

from plone.indexer.decorator import indexer
from plone.app.contenttypes.interfaces import INewsItem
from plone.app.contenttypes.interfaces import IImage


@indexer(IImage)
def image_subject(obj):
    return obj.Subject

@indexer(INewsItem)
def news_subject(obj):
    return obj.Subject
