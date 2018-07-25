# -*- coding: utf-8 -*-
from plone import api
from Products.Five.browser import BrowserView
from daisoi.content import _
from Products.CMFCore.utils import getToolByName


class GeneralMethod(BrowserView):
    def getCompanyInfo(self):
        info = {'address':api.portal.get_registry_record('daisoi.content.configlet.company_configlet.IInfo.address', default=''),
         'description':api.portal.get_registry_record('daisoi.content.configlet.company_configlet.IInfo.description', default=''),
         'email':api.portal.get_registry_record('daisoi.content.configlet.company_configlet.IInfo.email', default=''),
         'fax':api.portal.get_registry_record('daisoi.content.configlet.company_configlet.IInfo.fax', default=''),
         'phone':api.portal.get_registry_record('daisoi.content.configlet.company_configlet.IInfo.phone', default=''),
         'r_email':api.portal.get_registry_record('daisoi.content.configlet.company_configlet.IInfo.r_email', default=''),
         'fb_link':api.portal.get_registry_record('daisoi.content.configlet.company_configlet.IInfo.fb_link', default='')}
        return info


class ContactUsView(GeneralMethod):
    def pdb(self):
        import pdb;pdb.set_trace()


class NewsView(BrowserView):
    pass


class PloneRootView(GeneralMethod):

    def getBanner(self):
        portal = api.portal.get()
        context = self.context
        if portal.hasObject('resource'):
            if portal['resource'].hasObject('banner'):
                context = portal['resource']['banner']
        banner = api.content.find(context=context, portal_type='Document', sort_on='getObjPositionInParent')
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

    def getService(self):
        portal = api.portal.get()
        context = self.context
        if portal.hasObject('service'):
            context = portal['service']
        service = api.content.find(context=context, portal_type='Document', sort_on='getObjPositionInParent', b_size=3)
        return service

    def getPerformance(self):
        portal = api.portal.get()
        context = self.context
        if portal.hasObject('performance'):
            context = portal['performance']
        performance = api.content.find(context=context, portal_type='Image', sort_on='getObjPositionInParent', b_size='4')
        return performance
    
    def getServiceIcon(self):
        portal = api.portal.get()
        context = self.context
        if portal.hasObject('resource'):
            if portal['resource'].hasObject('service-icon'):
                context = portal['resource']['service-icon']
        serviceicon = api.content.find(context=context, portal_type='Document', sort_on='getObjPositionInParent', b_size=12)
        return serviceicon

    def getTestimonials(self):
        portal = api.portal.get()
        context = self.context
        if portal.hasObject('resource'):
            if portal['resource'].hasObject('testimonials'):
                context = portal['resource']['testimonials']
        testimonials = api.content.find(context=context, portal_type='Document', sort_on='getObjPositionInParent')
        return testimonials

