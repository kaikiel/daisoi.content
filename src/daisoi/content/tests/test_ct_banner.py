# -*- coding: utf-8 -*-
from daisoi.content.content.banner import IBanner  # NOQA E501
from daisoi.content.testing import DAISOI_CONTENT_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


try:
    from plone.dexterity.schema import portalTypeToSchemaName
except ImportError:
    # Plone < 5
    from plone.dexterity.utils import portalTypeToSchemaName


class BannerIntegrationTest(unittest.TestCase):

    layer = DAISOI_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_ct_banner_schema(self):
        fti = queryUtility(IDexterityFTI, name='Banner')
        schema = fti.lookupSchema()
        self.assertEqual(IBanner, schema)

    def test_ct_banner_fti(self):
        fti = queryUtility(IDexterityFTI, name='Banner')
        self.assertTrue(fti)

    def test_ct_banner_factory(self):
        fti = queryUtility(IDexterityFTI, name='Banner')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IBanner.providedBy(obj),
            u'IBanner not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_banner_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Banner',
            id='banner',
        )

        self.assertTrue(
            IBanner.providedBy(obj),
            u'IBanner not provided by {0}!'.format(
                obj.id,
            ),
        )

    def test_ct_banner_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Banner')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )
