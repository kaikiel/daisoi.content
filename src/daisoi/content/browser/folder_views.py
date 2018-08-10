# -*- coding: utf-8 -*-
from plone import api
from Products.Five.browser import BrowserView
from daisoi.content import _
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from plone.app.contenttypes.browser.folder import FolderView
from plone.app.contentlisting.interfaces import IContentListing
from daisoi.content.browser.views import GeneralMethod
from random import randint


class FolderPerformanceView(FolderView, GeneralMethod):
    def pdb(self):
        import pdb;pdb.set_trace()

    @property
    def img_subject(self):
        img_subject = getattr(self.request, 'img_subject', '')
        return img_subject

    @property
    def sort_on(self):
        sort_on = getattr(self.request, 'sort_on', 'getObjPositionInParent')
        return sort_on

    @property
    def b_size(self):
        b_size = getattr(self.request, 'b_size', None)\
            or getattr(self.request, 'limit_display', None) or 6
        return int(b_size)

    def results(self, **kwargs):
        """Return a content listing based result set with contents of the
        folder.

        :param **kwargs: Any keyword argument, which can be used for catalog
                         queries.
        :type  **kwargs: keyword argument

        :returns: plone.app.contentlisting based result set.
        :rtype: ``plone.app.contentlisting.interfaces.IContentListing`` based
                sequence.
        """
        # Extra filter
        kwargs.update(self.request.get('contentFilter', {}))
        if 'object_provides' not in kwargs:  # object_provides is more specific
            kwargs.setdefault('portal_type', 'Image')
        portal = api.portal.get()
        context = self.context
        kwargs.setdefault('path', context.absolute_url_path())
        kwargs.setdefault('batch', False)
        
        if self.img_subject:
            kwargs['img_subject'] = self.img_subject

        listing = aq_inner(self.context).restrictedTraverse(
            '@@folderListing', None)
        if listing is None:
            return []
        results = listing(**kwargs)
        
        if not self.img_subject:
            temp_results = []
            imgSubject = self.getImgSubject().keys()
            results = list(results[:])
            while len(results) > 0:
                for sub in imgSubject:
                    while True:
                        if len(results) == 0:
                            break
                        index = randint(0, len(results)-1) or 0
                        randImg = results[index]
                        if not randImg.img_subject:
                            temp_results.append(results.pop(index))
                        if sub in randImg.img_subject:
                            temp_results.append(results.pop(index))
                            break
                        imgSubject = set()
                        for img in results:
                            for subject in img.img_subject:
                                imgSubject.add(subject)
                        if sub not in imgSubject:
                            break
            results = temp_results
                
        return results


class FolderNewsView(FolderView):

    @property
    def searchableText(self):
        searchableText = getattr(self.request, 'searchableText', '')
        return searchableText

    @property
    def news_subject(self):
        news_subject = getattr(self.request, 'news_subject', '')
        return news_subject

    @property
    def sort_on(self):
        sort_on = getattr(self.request, 'sort_on', 'getObjPositionInParent')
        return sort_on

    @property
    def b_size(self):
        b_size = getattr(self.request, 'b_size', None)\
            or getattr(self.request, 'limit_display', None) or 3
        return int(b_size)

    def results(self, **kwargs):
        """Return a content listing based result set with contents of the
        folder.

        :param **kwargs: Any keyword argument, which can be used for catalog
                         queries.
        :type  **kwargs: keyword argument

        :returns: plone.app.contentlisting based result set.
        :rtype: ``plone.app.contentlisting.interfaces.IContentListing`` based
                sequence.
        """
        # Extra filter
        kwargs.update(self.request.get('contentFilter', {}))
        if 'object_provides' not in kwargs:  # object_provides is more specific
            kwargs.setdefault('portal_type', 'News Item')
        portal = api.portal.get()
        context = self.context
        kwargs.setdefault('path', context.absolute_url_path())
        kwargs.setdefault('batch', True)
        kwargs.setdefault('b_size', self.b_size)
        kwargs.setdefault('b_start', self.b_start)
        
        if self.news_subject:
            kwargs['news_subject'] = self.news_subject

        if self.searchableText:
            kwargs['SearchableText'] = self.searchableText

        listing = aq_inner(self.context).restrictedTraverse(
            '@@folderListing', None)
        if listing is None:
            return []
        results = listing(**kwargs)
        return results


class QuestionListing(FolderView):
    @property
    def b_size(self):
        b_size = getattr(self.request, 'b_size', None)\
            or getattr(self.request, 'limit_display', None) or 5
        return int(b_size)

    def results(self, **kwargs):
        # Extra filter
        kwargs.update(self.request.get('contentFilter', {}))
        if 'object_provides' not in kwargs:  # object_provides is more specific
            kwargs.setdefault('portal_type', 'Document')
        portal = api.portal.get()
        context = self.context
        kwargs.setdefault('path', context.absolute_url_path())
        kwargs.setdefault('batch', True)


        listing = aq_inner(self.context).restrictedTraverse(
            '@@folderListing', None)
        if listing is None:
            return []
        results = listing(**kwargs)
        return results
