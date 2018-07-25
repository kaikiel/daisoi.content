# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import common as base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from zope.component import getMultiAdapter
from Products.CMFPlone.utils import getSiteLogo
from daisoi.content.browser.views import GeneralMethod


class TopViewlet(base.ViewletBase, GeneralMethod):
    pass

class FooterViewlet(base.ViewletBase, GeneralMethod):
    def pdb(self):
        import pdb;pdb.set_trace()

    def getSiteLogo(self):
        return getSiteLogo()

    def getFriendLink(self):
        portal = api.portal.get()
        context = self.context
        if portal.hasObject('resource'):
            if portal['resource'].hasObject('friend-link'):
                context = portal['resource']['friend-link']
        friendLink = api.content.find(context=context, portal_type='Link', sort_on='getObjPositionInParent')
        return friendLink

    def getSiteMap(self):
        view = getMultiAdapter((self.context, self.request), name='sitemap_builder_view')
        data = view.siteMap()['children']
        return data

    def getTopTabs(self):
        portal_tabs_view = getMultiAdapter((self.context, self.request), name='portal_tabs_view')
        portal_tabs = portal_tabs_view.topLevelTabs()
        return portal_tabs

