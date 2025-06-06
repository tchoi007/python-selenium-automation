# Created by test at 6/5/2025
Feature: Target Cart test
  Scenario: Verify item is in cart
    Given Open target main page
    When Search for flashlight
    And click product title
    And click add to cart
    And click close
    And User clicks Cart icon
    Then verify 1 item in cart
