Feature: I input field for banner component
  Scenario Outline: I input valid banner information
    Given I go to Page component management
    When I selects country "Republic of Korea (used)" and clicks Register Component button
    Then I select "Banner" component type
    Then I can see "Banner" register form
    When I input all information fields include <display_order> and input <link> and <upload_locator_PC> and <filepath_PC> and <upload_locator_mobile> and <filepath_mobile>
    Then I register new Banner component successful
    Then I can see New component in list
    Then I can see New component in main displayed
    Examples:
      |display_order|link|upload_locator_PC|filepath_PC|upload_locator_mobile|filepath_mobile|
      |0            |https://translate.google.com/|xpath=(//*[contains(text(),'Upload')])[1]|./tests/resourse/banner_images/png_1300x325.png|xpath=(//*[contains(text(),'Upload')])[2]|./tests/resourse/banner_images/png_1138x210.png|
      #|1            |https://wiki.smilegate.net/pages/|xpath=(//*[contains(text(),'Upload')])[1]|./tests/resourse/banner_images/jpeg_1300x325.jpeg|xpath=(//*[contains(text(),'Upload')])[2]|./tests/resourse/banner_images/jpeg_1138x210.jpeg|