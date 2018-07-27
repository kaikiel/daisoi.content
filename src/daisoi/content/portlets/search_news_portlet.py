from plone import api
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import implements
from zope import schema
from daisoi.content import _


class ISearch_News(IPortletDataProvider):
    pass


class Assignment(base.Assignment):
    implements(ISearch_News)

    def __init__(self):
        pass

    @property
    def title(self):
        return _(u'Search_News')


class Renderer(base.Renderer):
    render = ViewPageTemplateFile('search_news_portlet.pt')
    
    def searchableText(self):
        s = getattr(self.request, 'searchableText', '')
        return s


class AddForm(base.AddForm):
    schema = ISearch_News
    label = _(u"Add Search_News Portlet")

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    schema = ISearch_News
    label = _(u"Edit Search_News Portlet")


