# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import common as base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import getSiteLogo
from daisoi.content.browser.views import GeneralMethod


class FolderBanner(base.ViewletBase):
    def getTopImage(self):
        context = self.context
        while True: 
            topImg = getattr(context, 'topImg', None)
            if topImg:
                return context.absolute_url() + '/@@images/topImg'
            context = getattr(context, 'getParentNode', None)
            if not context:
                return self.context.portal_url() + '/resource/website_image/default_folder_banner'
            else:
                context = context()


class TopViewlet(base.ViewletBase, GeneralMethod):
    pass

class FooterViewlet(base.ViewletBase, GeneralMethod):
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
        view = getMultiAdapter((self.context, self.request), name='sitemap_builder_view').siteMap().copy()
        siteMap = view['children'][:]
        data = []
        for item in siteMap:
            if item['id'] == 'performance':
                item_children = self.getImgSubject().values()
                item['children'] = item_children
                data.append(item)
            elif item['id'] == 'news_daisoi':
                item['children'] = []
                data.append(item)
            else:
                data.append(item)
        return data

    def getTopTabs(self):
        portal_tabs_view = getMultiAdapter((self.context, self.request), name='portal_tabs_view')
        portal_tabs = portal_tabs_view.topLevelTabs()
        return portal_tabs
