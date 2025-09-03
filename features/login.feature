Feature: User Login and Filter

  Scenario: Filter high to low
    Given the user is on the main dashboard
    When the user filters the displayed product's price from hi to low
    Then the user expects the first product to have the highest price

  Scenario: A to Z
    Given the user is on the main dashboard
    When the user filters the displayed product from a to z


  Scenario: add to cart on dashboard
    Given the user clicks the add to cart button
    When the user opens the cart
    Then the user expects that the product is already on the cart and checks the product name

  Scenario: click remove and go back to inventory dashboard
    Given the user is on the cart and clicks the remove button
    When the user clicks the continue shopping button

