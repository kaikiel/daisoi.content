# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s daisoi.content -t test_video_description.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src daisoi.content.testing.DAISOI_CONTENT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/daisoi/content/tests/robot/test_video_description.robot
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

Scenario: As a site administrator I can add a VideoDescription
  Given a logged-in site administrator
    and an add VideoDescription form
   When I type 'My VideoDescription' into the title field
    and I submit the form
   Then a VideoDescription with the title 'My VideoDescription' has been created

Scenario: As a site administrator I can view a VideoDescription
  Given a logged-in site administrator
    and a VideoDescription 'My VideoDescription'
   When I go to the VideoDescription view
   Then I can see the VideoDescription title 'My VideoDescription'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add VideoDescription form
  Go To  ${PLONE_URL}/++add++VideoDescription

a VideoDescription 'My VideoDescription'
  Create content  type=VideoDescription  id=my-video_description  title=My VideoDescription

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the VideoDescription view
  Go To  ${PLONE_URL}/my-video_description
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a VideoDescription with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the VideoDescription title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
