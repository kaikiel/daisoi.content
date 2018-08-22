# -*- coding: utf-8 -*-
from plone import api
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from daisoi.content import _
from Products.CMFCore.utils import getToolByName
from email.mime.text import MIMEText


class GeneralMethod(BrowserView):
    def getCompanyInfo(self):
        info = {'address':api.portal.get_registry_record('daisoi.content.configlet.company_configlet.IInfo.address', default=''),
         'description':api.portal.get_registry_record('daisoi.content.configlet.company_configlet.IInfo.description', default=''),
         'email':api.portal.get_registry_record('daisoi.content.configlet.company_configlet.IInfo.email', default=''),
         'fax':api.portal.get_registry_record('daisoi.content.configlet.company_configlet.IInfo.fax', default=''),
         'phone':api.portal.get_registry_record('daisoi.content.configlet.company_configlet.IInfo.phone', default=''),
         'r_email':api.portal.get_registry_record('daisoi.content.configlet.company_configlet.IInfo.r_email', default=''),
         'fb_link':api.portal.get_registry_record('daisoi.content.configlet.company_configlet.IInfo.fb_link', default=''),
         'youtube_link':api.portal.get_registry_record('daisoi.content.configlet.company_configlet.IInfo.youtube_link', default='')}
        return info

    def getImgSubject(self):
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        index = portal_catalog.Indexes['img_subject']
        imgSubjectList = {}
        for key in index.uniqueValues():
            subDict = {key:{'Title':key,
                            'getURL':'{}/performance?img_subject={}'.format(self.context.portal_url(), key),
                            'absolute_url':'{}/performance?img_subject={}'.format(self.context.portal_url(), key),
                            'children':[]}
                      }
            imgSubjectList.update(subDict)
        return imgSubjectList

    def getNewsSubject(self):
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        index = portal_catalog.Indexes['news_subject']
        newsSubjectList = {}
        for key in index.uniqueValues():
            subDict = {key:{'Title':key,
                            'getURL':'{}/news_daisoi?news_subject={}'.format(self.context.portal_url(), key),
                            'absolute_url':'{}/news_daisoi?news_subject={}'.format(self.context.portal_url(), key),
                            'children':[]}
                      }
            newsSubjectList.update(subDict)
        return newsSubjectList


class ContactUsView(GeneralMethod):
    template = ViewPageTemplateFile('templates/contact_us_view.pt')
    def __call__(self):
        request = self.request
        name = request.get('name')
        email = request.get('email')
        message = request.get('message')
        if name and email and message:
            try:
                phone = request.get('phone')
                subject = getattr(self.request, 'subject', "Contact Daisoi From:"+name)
                body_str = "Name:{}<br/>Email:{}<br/>Phone:{}<br/>Message:<br/>{}".format(name, email, phone, message)
                mime_text = MIMEText(body_str, 'html', 'utf-8')
                api.portal.send_email(
                    recipient=self.getCompanyInfo()['r_email'].encode('utf8'),
                    sender=email,
                    subject="Contact Daisoi: {}".format(subject),
                    body=mime_text.as_string(),
                )
                api.portal.show_message(message='發送成功!'.decode('utf-8'), request=request)
            except Exception as ex:
                print ex
            current_url = self.request.URL
            self.request.response.redirect(current_url)
        return self.template()


class NewsView(GeneralMethod):
    pass


class PloneRootView(GeneralMethod):
    def pdb(self):
        import pdb;pdb.set_trace()

    def getBanner(self):
        portal = api.portal.get()
        context = self.context
        if portal.hasObject('resource'):
            if portal['resource'].hasObject('banner'):
                context = portal['resource']['banner']
        banner = api.content.find(context=context, portal_type='Banner', sort_on='getObjPositionInParent')
        return banner

    def getIconBox(self):
        portal = api.portal.get()
        context = self.context
        if portal.hasObject('resource'):
            if portal['resource'].hasObject('icon-box'):
                context = portal['resource']['icon-box']
        iconbox = api.content.find(context=context, portal_type='Document', sort_on='getObjPositionInParent', b_size=3)
        return iconbox

    def getIndexAbout(self):
        portal = api.portal.get()
        context = self.context
        if portal.hasObject('resource'):
            if portal['resource'].hasObject('index-about'):
                context = portal['resource']['index-about']
        indexabout = api.content.find(context=context, portal_type='Document', sort_on='getObjPositionInParent', b_size=1)
        return indexabout

    def getPerformance(self):
        portal = api.portal.get()
        context = self.context
        if portal.hasObject('performance'):
            context = portal['performance']
        performance = api.content.find(context=context, portal_type='Image', sort_on='getObjPositionInParent', b_size='4')
        return performance
    
    def getServiceIconFolder(self):
        portal = api.portal.get()
        context = self.context
        if portal.hasObject('resource'):
            if portal['resource'].hasObject('service-icon'):
                context = portal['resource']['service-icon']
        return context

    def getServiceIcon(self):
        portal = api.portal.get()
        context = self.context
        if portal.hasObject('resource'):
            if portal['resource'].hasObject('service-icon'):
                context = portal['resource']['service-icon']
        serviceicon = api.content.find(context=context, portal_type='Document', sort_on='getObjPositionInParent', b_size=12)
        return serviceicon

    """
    def getService(self):
        portal = api.portal.get()
        context = self.context
        if portal.hasObject('resource'):
            if portal['resource'].hasObject('main-service'):
                context = portal['resource']['main-service']
        service = api.content.find(context=context, portal_type='Document', sort_on='getObjPositionInParent', b_size=3)
        return service
    """

    """
    def getTestimonials(self):
        portal = api.portal.get()
        context = self.context
        if portal.hasObject('resource'):
            if portal['resource'].hasObject('testimonials'):
                context = portal['resource']['testimonials']
        testimonials = api.content.find(context=context, portal_type='Document', sort_on='getObjPositionInParent')
        return testimonials
    """


class LoginView(GeneralMethod):
    pass


class ImgView(BrowserView):
    pass


class FactoryManagementView(BrowserView):
    def getLargeText(self, text):
        l_text_start = text.find('<')
        l_text_end = text.find('>')
        if l_text_start != -1 and l_text_end != -1:
            text = text.replace(text[l_text_start: l_text_end+1], \
                                '<span class="large-text">{}</span>'.format(text[l_text_start+1: l_text_end]))
        return text

    def getVideoDescription(self):
        videoDescription = api.content.find(context=self.context, portal_type="VideoDescription", sort_on='getObjPositionInParent')
        return videoDescription

    def getTopText(self):
        topText = api.content.find(context=self.context, portal_type="ProblemTable", sort_on='getObjPositionInParent', b_size="1")
        return topText[0]

    def getProblemTable(self):
        problemTable = api.content.find(context=self.context, portal_type="ProblemTable", sort_on='getObjPositionInParent', b_size="1")
        p_table = []
        if len(problemTable) > 0:
            problemTable = problemTable[0].getObject()
            t_row = ['problem', 'smart']
            t_col = ['people', 'machine', 'materials', 'method', 'EC']
            for row in t_row:
                for col in t_col:
                    p_table.append(getattr(problemTable, '_'.join([row,col]) ))
            return p_table
        return []

    def getProblemTable_mobile(self):
        problemTable = api.content.find(context=self.context, portal_type="ProblemTable", sort_on='getObjPositionInParent', b_size="1")
        p_table = []
        if len(problemTable) > 0:
            problemTable = problemTable[0].getObject()
            t_row    = ['people', 'machine', 'materials', 'method', 'EC']
            col_name = ['人員'  , '機器'   , '物料'     , '方法'  , '環控']
            t_col = ['problem', 'smart']
            for i, row in enumerate(t_row):
                p_table.append([col_name[i]])
                for col in t_col:
                    p_table[i].append(getattr(problemTable, '_'.join([col,row]) ))
            return p_table
        return []


class TwelveFunctionView(BrowserView):
    def get12Function(self):
        functions = api.content.find(context=self.context, portal_type="Document", sort_on='getObjPositionInParent', b_size="12")
        return functions


class ServiceView(BrowserView):
    def getVideoDescription(self):
        videoDescription = api.content.find(context=self.context, portal_type="VideoDescription", sort_on='getObjPositionInParent', b_size="1")
        return videoDescription[0]

    def getServiceDescription(self):
        description = api.content.find(context=self.context, portal_type="ServiceDescription", sort_on='getObjPositionInParent', b_size="1")
        return description[0]


class PhilosophyView(BrowserView):
    pass

