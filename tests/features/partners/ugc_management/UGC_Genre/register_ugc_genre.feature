Feature: I create a new genre
  Scenario Outline: I create a new genre successful
    Given I navigate to ugc gere management
    Then I click register1 button
    Then I input genre information with <usage_status>
    Then I upload with <genre_image> and <filepath_genre_image>
    Then I click register2 button
    Then I see a new genre was created
    Examples:
      |usage_status|genre_image|filepath_genre_image|
      |xpath=//label[normalize-space(text())="Usable"]|xpath=(//*[contains(text(),"Upload")])[1]|./tests/resourse/genre_image/64x64.png|
     # |xpath=//label[normalize-space(text())="Not Usable"]|xpath=(//*[@class="p-button-label" and contains(text(),"Upload")])[1]|./tests/resourse/genre_image/64x64 jpeg.jpeg|
