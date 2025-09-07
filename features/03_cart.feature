Feature: Shopping Cart

  Scenario: Add to cart on dashboard
    Given the user clicks the add to cart button
    When the user opens the cart
    Then the user expects that the product is already on the cart and checks the product name


  Scenario: Remove from cart and go back to dashboard
    Given the user is on the cart and clicks the remove button
    When the user clicks the continue shopping button
