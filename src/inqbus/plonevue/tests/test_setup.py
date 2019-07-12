# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from inqbus.plonevue.testing import INQBUS_PLONEVUE_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that inqbus.plonevue is properly installed."""

    layer = INQBUS_PLONEVUE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if inqbus.plonevue is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'inqbus.plonevue'))

    def test_browserlayer(self):
        """Test that IInqbusPlonevueLayer is registered."""
        from inqbus.plonevue.interfaces import (
            IInqbusPlonevueLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IInqbusPlonevueLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = INQBUS_PLONEVUE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['inqbus.plonevue'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if inqbus.plonevue is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'inqbus.plonevue'))

    def test_browserlayer_removed(self):
        """Test that IInqbusPlonevueLayer is removed."""
        from inqbus.plonevue.interfaces import \
            IInqbusPlonevueLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IInqbusPlonevueLayer,
            utils.registered_layers())
