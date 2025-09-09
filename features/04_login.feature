Feature: Logging In

  Scenario: Login with VALID credentials
    Given that the current state is logged-out
    When the user logs-in with VALID credentials
    Then the user validates that it has successfully logged-in

  Scenario: Login with INVALID credentials
    Given that the current state is logged-out
    When the user logs-in with INVALID credentials
    Then the user has unsuccessfully logged-in

