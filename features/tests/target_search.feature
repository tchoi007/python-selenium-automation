Feature: Tests for Target Search

  Scenario: User can search for a product on Target
    Given Open target main page
    When Search for tea
    Then Verify search worked for tea

#  Scenario: User can search for a product on Target
#    Given Open target main page
#    When Search for coffee
#    Then Verify search worked for coffee


#  Scenario: User can search for a product on Target
#    Given Open target main page
#    When Search for mug
#    Then Verify search worked for mug
