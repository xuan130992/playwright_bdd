Feature: Login feature
  Scenario: Login successful with valid credentials
    Given I am on the login page
    When I enter username and password
    When I click the login button
    Then I should see the partner page
    Then I should see the storage state