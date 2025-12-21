Feature: I input field for banner component
  Scenario: I input valid banner information
    Given I go to Page component management
    When I User selects country "Republic of Korea (used)" and clicks Register Component button
    Then I select "Banner" component type
    Then I can see "Banner" register form
    When I input all information fields include <display_order> and input <link> and <upload_locator> and <filepath>
    Then I register new Banner component successful
    Then I can see New component in list
    Example:
      |  display_order|link|upload_locator|filepath|
      |0             |https:hddjshdjhs|xpath=(//*[contains(text(),'Upload')])[1]|./resourse/banner_images/png_1300x325.png)