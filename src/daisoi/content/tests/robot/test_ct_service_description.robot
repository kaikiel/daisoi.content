# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s daisoi.content -t test_service_description.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src daisoi.content.testing.DAISOI_CONTENT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/daisoi/content/tests/robot/test_service_description.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a ServiceDescription
  Given a logged-in site administrator
    and an add ServiceDescription form
   When I type 'My ServiceDescription' into the title field
    and I submit the form
   Then a ServiceDescription with the title 'My ServiceDescription' has been created

Scenario: As a site administrator I can view a ServiceDescription
  Given a logged-in site administrator
    and a ServiceDescription 'My ServiceDescription'
   When I go to the ServiceDescription view
   Then I can see the ServiceDescription title 'My ServiceDescription'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add ServiceDescription form
  Go To  ${PLONE_URL}/++add++ServiceDescription

a ServiceDescription 'My ServiceDescription'
  Create content  type=ServiceDescription  id=my-service_description  title=My ServiceDescription

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the ServiceDescription view
  Go To  ${PLONE_URL}/my-service_description
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a ServiceDescription with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the ServiceDescription title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
