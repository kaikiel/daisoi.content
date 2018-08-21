# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s daisoi.content -t test_banner.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src daisoi.content.testing.DAISOI_CONTENT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/daisoi/content/tests/robot/test_banner.robot
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

Scenario: As a site administrator I can add a Banner
  Given a logged-in site administrator
    and an add Banner form
   When I type 'My Banner' into the title field
    and I submit the form
   Then a Banner with the title 'My Banner' has been created

Scenario: As a site administrator I can view a Banner
  Given a logged-in site administrator
    and a Banner 'My Banner'
   When I go to the Banner view
   Then I can see the Banner title 'My Banner'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Banner form
  Go To  ${PLONE_URL}/++add++Banner

a Banner 'My Banner'
  Create content  type=Banner  id=my-banner  title=My Banner

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Banner view
  Go To  ${PLONE_URL}/my-banner
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Banner with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Banner title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
