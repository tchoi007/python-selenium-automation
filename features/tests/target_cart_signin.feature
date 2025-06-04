Feature:Target empty cart and sign in page
  Scenario: User can go to an empty cart
    Given Open target main page
    When User clicks Cart icon
    Then Cart shows empty



  Scenario: User can go to sign in page
    Given Open target main page
    When User clicks account
    When User clicks sign in
    Then Sign in page displays