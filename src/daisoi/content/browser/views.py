# -*- coding: utf-8 -*-
from plone import api
from Products.Five.browser import BrowserView
from daisoi.content import _
from Products.CMFCore.utils import getToolByName


class ContactUsView(BrowserView):
    def pdb(self):
        import pdb;pdb.set_trace()


class NewsView(BrowserView):
    pass


class PloneRootView(BrowserView):
    def getBanner(self):
        portal = api.portal.get()
        context = self.context
        if portal.hasObject('resource'):
            if portal['resource'].hasObject('banner'):
                context = portal['resource']['banner']
        banner = api.content.find(context=context, portal_type='Document', sort_on='getObjPositionInParent')
        return banner

    def getPerformance(self):
        portal = api.portal.get()
        context = self.context
        if portal.hasObject('performance'):
            context = portal['performace']
        banner = api.content.find(context=context, portal_type='Image', sort_on='getObjPositionInParent', b_size=4)
        return banner
    
