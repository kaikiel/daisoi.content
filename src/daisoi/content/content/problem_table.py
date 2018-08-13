# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from daisoi.content import _


class IProblemTable(model.Schema):
    fieldset(_('Basic Text'), fields=['description_header', 'description_text', 'description_img'])
    description_header = schema.Text(
        title=_(u'description header'),
        required=True,
    )

    description_text = schema.Text(
        title=_(u'description text'),
        required=True,
    )

    description_img = namedfile.NamedBlobImage(
        title=_(u'description Image'),
        required=True,
    )

    fieldset(_('General Problem'), fields=['problem_people', 'problem_machine', 'problem_materials', 'problem_method', 'problem_EC'])
    problem_people = schema.Text(
        title=_(u'problem_people'),
        required=True,
    )

    problem_machine = schema.Text(
        title=_(u'problem_machine'),
        required=True,
    )

    problem_materials = schema.Text(
        title=_(u'problem_materials'),
        required=True,
    )

    problem_method = schema.Text(
        title=_(u'problem_method'),
        required=True,
    )

    problem_EC = schema.Text(
        title=_(u'problem_EC'),
        required=True,
    )

    fieldset(_('Smart Problem'), fields=['smart_people', 'smart_machine', 'smart_materials', 'smart_method', 'smart_EC'])
    smart_people = schema.Text(
        title=_(u'smart_people'),
        required=True,
    )

    smart_machine = schema.Text(
        title=_(u'smart_machine'),
        required=True,
    )

    smart_materials = schema.Text(
        title=_(u'smart_materials'),
        required=True,
    )

    smart_method = schema.Text(
        title=_(u'smart_method'),
        required=True,
    )

    smart_EC = schema.Text(
        title=_(u'smart_EC'),
        required=True,
    )


@implementer(IProblemTable)
class ProblemTable(Item):
    """
    """
