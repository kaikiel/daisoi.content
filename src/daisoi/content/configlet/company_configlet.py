# -*- coding: utf-8 -*-
from daisoi.content import _
from Products.Five.browser import BrowserView
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from zope.interface import Invalid
from zope.interface import invariant
from zope import schema
from plone import schema as plone_schema
from plone.z3cform import layout
from z3c.form import form
from plone.supermodel import model
import re
#from plone.directives import form as Form


class IInfo(model.Schema):
    description = schema.Text(
        title=_(u'Company Description'),
        description=_(u'Display on Footer'),
        required=False,
    )

    address = schema.Text(
        title=_(u'Address'),
        description=_(u'Display on Top and Footer and Contact Us Page'),
        required=False
    )

    email = schema.Text(
        title=_(u'E-Mail'),
        description=_(u'Display on Footer and Contact Us Page'),
        required=False,
    )

    phone = schema.Text(
        title=_(u'Phone'),
        description=_(u'Display on Index and Top and Footer and Contact Us Page'),
        required=False,
    )

    fax = schema.Text(
        title=_(u'Fax'),
        description=_(u'Display on Footer and Contact Us Page'),
        required=False,
    )
    
    r_email = schema.TextLine(
        title=_(u'E-Mail (Receive)'),
        description=_(u'Used to receive E-Mail from Contact Us Page'),
        required=False,
    )
    
    fb_link = schema.TextLine(
        title=_(u'Facebook Link'),
        description=_(u'Displan on Top'),
        required=False,
    )

    @invariant
    def email_invariant(data):
        com_email = data.email
        r_email = data.r_email
        if com_email:
            for email in com_email.split('\r\n'):
                if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
                    raise Invalid(_(u'Your Email is not valid!'))
        if r_email and not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", r_email):
            raise Invalid(_(u'Receive Email is not valid!'))    


class CompanyInfoControlPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = IInfo

CustomControlPanelView = layout.wrap_form(CompanyInfoControlPanelForm, ControlPanelFormWrapper)
CustomControlPanelView.label = _(u"Compony Info")

