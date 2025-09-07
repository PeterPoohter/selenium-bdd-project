Feature: Product Filtering

  Scenario: Filter high to low
    Given the user is on the main dashboard
    When the user filters the displayed product's price from hi to low
    Then the user expects the first product to have the highest price

  Scenario: A to Z
    Given the user is on the main dashboard
    When the user filters the displayed product from a to z
    Then the user expects the product list to be sorted alphabetically (a-z)
