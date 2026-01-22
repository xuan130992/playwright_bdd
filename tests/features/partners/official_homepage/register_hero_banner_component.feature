Feature: I input field for Herro banner component
  Scenario Outline: I input valid Herro banner information
    Given I go to Page component management
    When I selects country "Republic of Korea (used)" and clicks Register Component button
    Then I select "Hero Banner" component type
    Then I can see "Hero Banner" register form
    When I input all information fields include <display_order> and input <link> and <upload_locator_PC> and <filepath_PC> and <upload_locator_mobile> and <filepath_mobile> for image type
    Then I register new Hero Banner component successful
    Then I can see New component in list
    Then I can see New component in main displayed
    Examples:
      |display_order|link|upload_locator_PC|filepath_PC|upload_locator_mobile|filepath_mobile|
      |0            |https://translate.google.com/|xpath=(//*[contains(text(),'Upload')])[1]|./tests/resourse/banner_images/png_2560x542.png|xpath=(//*[contains(text(),'Upload')])[2]|./tests/resourse/banner_images/png_1364x642.png|

     Scenario Outline: I create a Hero banner with video type
    Given I go to Page component management
    When I selects country "Republic of Korea (used)" and clicks Register Component button
    Then I select "Hero Banner" component type
    Then I can see "Hero Banner" register form
    When I input all information fields include <display_order>
    When I input information fields for video type include <background_color_selected> and <link> and <video_url>
    When I upload thumbnail image <upload_locator_PC> and <filepath_PC> for video type
    Then I register new Hero Banner component successful
    Then I can see New component in list
    Then I can see New component in main displayed
    Examples:
      |display_order|background_color_selected|link|video_url|upload_locator_PC|filepath_PC|
      |0            |#256646       |#https://translate.google.com/|https://www.youtube.com/watch?v=VvAVTFVvcyI|xpath=(//*[contains(text(),'Upload')])[1]|./tests/resourse/banner_images/1280x720.jpg|
