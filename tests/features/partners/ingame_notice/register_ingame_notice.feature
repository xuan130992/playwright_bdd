Feature: I create an ingame notice successfully with type Immediate Notice
  Scenario Outline: I input valid ingame notice filed
    Given I go to page In-game Notice Management
    When I click the Register button
    Then I select Platform <platform>
    Then I select Display Area <display_area>
    Then I select send type <send_type>
    Then I select countries
    Then I input the notice content
    Then I click the Register button
    Then I verify the notice register successfully

    Examples:
      | platform|display_area|send_type|
      | All     |All |Immediate Notice|
#      |IOS       |Park|Scheduled Notice|
#      |AOS        |MOD|Repeating Notice|