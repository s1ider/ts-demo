Feature: Landing

    Scenario: Verify prices
        Given I am on 'Landing' page
        When Buy ticket #2
        Then Price should be '2150'
