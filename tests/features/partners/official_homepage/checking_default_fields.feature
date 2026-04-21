Feature: I check the default value in component register
    Scenario Outline: I check the default for common fields value
    Given I go to Page component management
    When I selects country "Republic of Korea (used)" and clicks Register Component button
    Then I select "<component_type>" component type
    Then I verify if the Display Country field is display "Republic of Korea"
    Then I verify if the Component Type is "<component_type>"
    Then I verify if the Component ID has the placeholder "Automatically generated upon registration." and disable
    Then I verify if the Title field has the placeholder "Please enter within 60 characters." and enable
   # Then I verify if the display Status is "Display"
    Then I verify if the period from and period to is display correct period from and period to
    Then I verify if Display Order is "0"
    Then I verify if the Use Component Title Option is <component_tile_option>
    Then I verify if the default language is "English"
    Examples:
      |component_type|component_tile_option|
      |Banner|Do Not Use                    |
      |Featured Mod|Use|
      |Hero Banner|Do Not Use|
      |Highlight Mod|Use|
      |Normal Mod|Use|
      |Ranking|Use|



    Scenario Outline: I check the default for other specific fields
      Given I go to Page component management
      When I selects country "Republic of Korea (used)" and clicks Register Component button
      Then I select "<component_type>" component type
      Then the field "<field>" should be "<visibility>" with default "<defaultValue>"
        Examples:
            |component_type| field |visibility|defaultValue|
            |Banner   |Add Banner  |visible   |enable      |
            |Featured Mod|Mod Register|visible|enable      |
            |Hero Banner |Add Banner  |visible|enable      |
            |Highlight Mod|Mod Register|visible|enable      |
            |Normal Mod   |Manual Registration |visible|checked|
            |Normal Mod   |Maximum Display Count  |visible|All|
            |Normal Mod   |Mod Register           |visible|enable|
            |Normal Mod   |Mod Bulk Register           |visible|enable|
            |Ranking   |Entire          |visible|enable|
            |Ranking   |Mod Register         |visible|enable|


