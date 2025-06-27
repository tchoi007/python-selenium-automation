Feature: Target sign in page
  @hwtest
  Scenario: User can go to sign in page
    Given Open target main page
    When User clicks account
    When User clicks sign in
    Then Sign in page displays Sign in or create account