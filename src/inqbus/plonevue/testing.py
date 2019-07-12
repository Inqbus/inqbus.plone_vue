# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import inqbus.plonevue


class InqbusPlonevueLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=inqbus.plonevue)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'inqbus.plonevue:default')


INQBUS_PLONEVUE_FIXTURE = InqbusPlonevueLayer()


INQBUS_PLONEVUE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(INQBUS_PLONEVUE_FIXTURE,),
    name='InqbusPlonevueLayer:IntegrationTesting',
)


INQBUS_PLONEVUE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(INQBUS_PLONEVUE_FIXTURE,),
    name='InqbusPlonevueLayer:FunctionalTesting',
)


INQBUS_PLONEVUE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        INQBUS_PLONEVUE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='InqbusPlonevueLayer:AcceptanceTesting',
)
