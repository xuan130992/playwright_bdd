@regression
Feature: Validate Page Component Registration Form
  Background:
    Given I go to Page component management
    Given I selects country "Republic of Korea" and clicks Register Component button

#================require filed validation=============================
  @regression @checking1
  Scenario Outline: Verify Title field is required for <component_type>
    Given I select "<component_type>" component type
    When I click Register button without filling any fields
    Then I can see required error alert for "Title" field

    Examples:
      | component_type |
      | Hero Banner    |
      | Banner         |
      |Featured Mod    |
      |Hero Banner|
      |Highlight Mod|
      |Normal Mod|
      |Ranking|
    @regression @checking3
    Scenario Outline: Verify Display Period is required for <component_type>
    Given I select "<component_type>" component type
    Then I input valid "Title"
    Then I input invalid "Display Period from"
    Then I input invalid "Display Period to"
    When I click Register button
    Then I can see required error alert for "Display Period" field

   Examples:
      | component_type |
      | Hero Banner    |
      | Banner         |
      |Featured Mod    |
      |Highlight Mod|
      |Normal Mod|
      |Ranking|
  @regression
  Scenario Outline: Verify Banner section is required for <component_type>
    Given I select "<component_type>" component type
    Then I input valid "Title"
    When I click Register button
    Then I can see required error alert for "Banner" field
    Examples:
      | component_type |
      | Hero Banner    |
      | Banner         |
  @regression
  Scenario Outline: Verify Main Title in Banner section is required for <component_type>
    Given I select "<component_type>" component type
    Then I input valid "Title"
    Then I click Add banner button
    When I click Register button
    Then I can see required error alert for "Main Title" field
    Examples:
      | component_type |
      | Hero Banner    |
      | Banner         |
  @regression
  Scenario Outline: Verify Banner Image PC is required for <component_type>
    Given I select "<component_type>" component type
    Then I input valid "Title"
    Then I click Add banner button
    Then I input valid "Main Title"
    When I click Register button
    Then I can see required error alert for "PC image" field

    Examples:
      | component_type |
      | Hero Banner    |
      | Banner         |
  @regression
  Scenario Outline: Verify Banner Image Mobile is required for <component_type>
    Given I select "<component_type>" component type
    Then I input valid "Title"
    Then I click Add banner button
    Then I input valid "Main Title"
    Then I upload valid image to PC image
    When I click Register button
    Then I can see required error alert for "mobile image" field

    Examples:
      | component_type |
      | Hero Banner    |
      | Banner         |
  @regression @checking3
  Scenario Outline: Verify link URL Mobile is required for <component_type>
    Given I select "<component_type>" component type
    Then I input valid "Title"
    Then I click Add banner button
    Then I input valid "Main Title"
    Then I upload valid image to PC image
    Then I upload valid image to mobile image
    When I click Register button
    Then I can see required error alert for "Link URL" field

    Examples:
      | component_type |
      | Hero Banner    |
      | Banner         |

    #=========================Mod component_title requirement======================
  @regression
  Scenario Outline:Verify component title is required for <component_type>
    Given I select "<component_type>" component type
    Then I input valid "Title"
    When I click Register button
    Then I can see required error alert for "component title" field
    Examples:
      | component_type |
      |Featured Mod    |
      |Highlight Mod|
      |Normal Mod|
      |Ranking|

      #=============================Mod mod register requirement======================
  @regression
   Scenario Outline:Verify mod register is required for <component_type>
    Given I select "<component_type>" component type
    Then I input valid "Title"
    Then I input valid "component title"
    When I click Register button
    Then I can see required error alert for "mod register" field
    Examples:
      | component_type |
      |Featured Mod    |
      |Highlight Mod|
      |Normal Mod|

