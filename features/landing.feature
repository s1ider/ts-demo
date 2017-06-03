Feature: Landing

    Scenario Outline: Verify prices
        Given I am on 'Landing' page
        When Buy ticket #<option>
        Then Price should be '<price>'

    Examples:
        | option | price |
        | 1      | 2150  |
        | 2      | 2250  |
        | 3      | 3700  |


