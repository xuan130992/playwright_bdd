Feature: I create an ingame notice successfully with type Immediate Notice
  Scenario Outline: I input valid ingame notice filed
    Given I go to page In-game Notice Management
    When I click the Register button
    Then I select Platform <platform>
    Then I select Display Area <display_area>
    Then I select Send Type is Immediate
    Then I select countries
    Then I input the notice content
    Then I click the Register button
    Then I verify the notice register successfully
    #Then I click Register button
    Examples:
      |  platform|display_area|
      | All     |All |
#     |iOS       |Park|Notice iOS vs Park    |
#      |AOS        |MOD|Notice AOS vs MOD |