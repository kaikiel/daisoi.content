# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from daisoi.content.testing import DAISOI_CONTENT_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that daisoi.content is properly installed."""

    layer = DAISOI_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if daisoi.content is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'daisoi.content'))

    def test_browserlayer(self):
        """Test that IDaisoiContentLayer is registered."""
        from daisoi.content.interfaces import (
            IDaisoiContentLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IDaisoiContentLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = DAISOI_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['daisoi.content'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if daisoi.content is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'daisoi.content'))

    def test_browserlayer_removed(self):
        """Test that IDaisoiContentLayer is removed."""
        from daisoi.content.interfaces import \
            IDaisoiContentLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IDaisoiContentLayer,
            utils.registered_layers())
