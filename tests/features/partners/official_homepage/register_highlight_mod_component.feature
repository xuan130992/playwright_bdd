Feature: User input highlight Mod information
  Scenario: Input valid highlight mod information
    Given User goes to Page component management
    When User selects country "Republic of Korea (used)" and clicks Register Component button
    Then I select "Highlight Mod" mod type
    Then I can see "Highlight Mod" register form
    When I input all information fields
    Then I select mod
    Then I register new highlight Mod component successful
    Then I can see New component in list
    Then I can see New component in main displayed
