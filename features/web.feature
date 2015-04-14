Feature: Testing

  @testing
  Scenario: Open the google homepage

    Given I open the following url https://www.google.com
    Then I am on the google website
