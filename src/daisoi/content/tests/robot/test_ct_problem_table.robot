# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s daisoi.content -t test_problem_table.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src daisoi.content.testing.DAISOI_CONTENT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/daisoi/content/tests/robot/test_problem_table.robot
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

Scenario: As a site administrator I can add a ProblemTable
  Given a logged-in site administrator
    and an add ProblemTable form
   When I type 'My ProblemTable' into the title field
    and I submit the form
   Then a ProblemTable with the title 'My ProblemTable' has been created

Scenario: As a site administrator I can view a ProblemTable
  Given a logged-in site administrator
    and a ProblemTable 'My ProblemTable'
   When I go to the ProblemTable view
   Then I can see the ProblemTable title 'My ProblemTable'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add ProblemTable form
  Go To  ${PLONE_URL}/++add++ProblemTable

a ProblemTable 'My ProblemTable'
  Create content  type=ProblemTable  id=my-problem_table  title=My ProblemTable

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the ProblemTable view
  Go To  ${PLONE_URL}/my-problem_table
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a ProblemTable with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the ProblemTable title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
