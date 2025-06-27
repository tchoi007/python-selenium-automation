Feature: Tests the Help page
  @hwtest
  Scenario: User can select Help topic Gift Cards
    Given Open Help page for Returns
    Then Verify help Current Returns page opens
    When Select Help topic Gift Cards
    Then Verify help Current Target GiftCard balance page opens