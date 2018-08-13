# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s daisoi.content -t test_philosophy.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src daisoi.content.testing.DAISOI_CONTENT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/daisoi/content/tests/robot/test_philosophy.robot
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

Scenario: As a site administrator I can add a Philosophy
  Given a logged-in site administrator
    and an add Philosophy form
   When I type 'My Philosophy' into the title field
    and I submit the form
   Then a Philosophy with the title 'My Philosophy' has been created

Scenario: As a site administrator I can view a Philosophy
  Given a logged-in site administrator
    and a Philosophy 'My Philosophy'
   When I go to the Philosophy view
   Then I can see the Philosophy title 'My Philosophy'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Philosophy form
  Go To  ${PLONE_URL}/++add++Philosophy

a Philosophy 'My Philosophy'
  Create content  type=Philosophy  id=my-philosophy  title=My Philosophy

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Philosophy view
  Go To  ${PLONE_URL}/my-philosophy
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Philosophy with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Philosophy title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
