Feature: User register normal Mod component
  Scenario: I register normal Mod component successful
    Given I go to Page component management
    When I select country "Republic of Korea (used)" and clicks Register Component button
    Then I select "Normal Mod" mod type
    Then I can see "Standard MOD" register form
    When I input all information fields
    When I select manual registration method
    Then I select mod
    Then I register new normal Mod component successful
    Then I can see New component in list
    Then I can see New component in main displayed
