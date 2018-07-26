from plone import api
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import implements
from zope import schema
from daisoi.content import _
from daisoi.content.browser.views import GeneralMethod

class IImg_Subject(IPortletDataProvider):
    pass


class Assignment(base.Assignment):
    implements(IImg_Subject)

    def __init__(self):
        pass

    @property
    def title(self):
        return _(u'Img_Subject')


class Renderer(base.Renderer, GeneralMethod):
    render = ViewPageTemplateFile('img_subject_portlet.pt')


class AddForm(base.AddForm):
    schema = IImg_Subject
    label = _(u"Add Img_Subject Portlet")

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    schema = IImg_Subject
    label = _(u"Edit Img_Subject Portlet")

