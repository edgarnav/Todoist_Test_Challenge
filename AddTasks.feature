Feature: Add tasks

  Scenario: Add 5 tasks
    Given Prepare classes
    When Validate library page
    Then Get title tasks
    Given Go to login page
    When Validate login page
    When Send email and password
    Then Click login button
    Then Add tasks
