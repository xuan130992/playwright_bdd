Feature: Validate Page Component Registration Form
  Background:
    Given I goes to Page component management
    And I selects country "Republic of Korea" and clicks Register Component button

    #require filed validation
  Scenario Outline: Verify Title field is required for <component_type>
    Given I select "<component_type>" component type
    When I click Register button without filling any fields
    Then I can see required error alert on "Title" field

    Examples:
      | component_type |
      | Hero Banner    |
      | Banner         |
    Scenario Outline: Verify Display Period is required for <component_type>
    Given I select "<component_type>" component type
    And I input valid "Title"
    When I click Register button
    Then I can see required error alert on "Display Period" field

   Examples:
      | component_type |
      | Hero Banner    |
      | Banner         |

  Scenario Outline: Verify Main Title in Banner section is required for <component_type>
    Given I select "<component_type>" component type
    And I input valid "Title"
    And I input valid "Display Period"
    And I input valid "Display Order"
    When I click Register button
    Then I can see required error alert on "Main Title" field
    Examples:
      | component_type |
      | Hero Banner    |
      | Banner         |
  Scenario Outline: Verify Banner Image PC is required for <component_type>
    Given I select "<component_type>" component type
    And I input valid "Title"
    And I input valid "Display Period"
    And I input valid "Display Order"
    And I input valid "Main Title"
    When I click Register button
    Then I can see required error alert on "Banner Image PC" field

    Examples:
      | component_type |
      | Hero Banner    |
      | Banner         |

  Scenario Outline: Verify Banner Image Mobile is required for <component_type>
    Given I select "<component_type>" component type
    And I input valid "Title"
    And I input valid "Display Period"
    And I input valid "Display Order"
    And I input valid "Main Title"
    And I upload valid image to "Banner Image PC"
    When I click Register button
    Then I can see required error alert on "Banner Image Mobile" field

    Examples:
      | component_type |
      | Hero Banner    |
      | Banner         |