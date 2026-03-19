Feature: I create an ingame notice successful
  Scenario Outline: I input valid ingame notice filed
    Given I go to page In-game Notice Management
    When I click the Register button
    Then I select Platform
    Then I select Display Area
    Then I select Send Type
    Then I set countries
    Then I input the language
    Then I click Register button
    Examples:
      |  |