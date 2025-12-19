Feature: I input field for banner component
  Scenario: I input valid banner information
    Given I go to Page component management
    When I User selects country "Republic of Korea (used)" and clicks Register Component button
    Then I select "Banner" component type
    Then I can see "Banner" register form
    When I input all information fields include <display_order> and input <link>
    Then I register new Banner component successful
    Then I can see New component in list
    Example:
      |  display_order|link|
      |0             |https:hddjshdjhs|