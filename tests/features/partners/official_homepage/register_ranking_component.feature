Feature: User register ranking component
  Scenario: I register ranking component successful
    Given I go to Page component management
    When I select country "Republic of Korea (used)" and clicks Register Component button
    Then I select "Ranking" mod type
    Then I can see "Ranking" register form
    When I input all information fields
    When I select Aggregation Period
    Then I select mod
    Then I register new ranking component successful
    Then I can see New component in list
#    Then I can see New component in main displayed