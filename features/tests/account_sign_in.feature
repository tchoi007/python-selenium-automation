Feature: Signing in functions
  Scenario: Verify password error
    Given Open sign in page
    When enter correct email
    And click continue
    And enter incorrect password
    And click continue
    Then Verify password text is Please enter a valid password