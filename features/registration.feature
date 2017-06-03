Feature: Registration

    Background:
        Given I am on 'Registration' page

    Scenario: Validate promo code
        When Submit form:
            | label    | value            |
            | Фамилия  | Robot            |
            | Имя      | Bobot            |
            | Email    | r2d2@bcdtrip.com |
            | Телефон  | 123456789        |
            | Промокод | 12355            |
        Then Validation error message for 'Промокод' should be displayed

    Scenario: Validate all mandatory fields
        When Submit form
        Then Validation error message for 'Фамилия' should be displayed
        Then Validation error message for 'Имя' should be displayed
        Then Validation error message for 'Email' should be displayed

    @wip
    Scenario: Buy a ticket
        When Submit form:
            | label    | value            |
            | Фамилия  | Robot            |
            | Имя      | Bobot            |
            | Email    | r2d2@bcdtrip.com |
            | Телефон  | 123456789        |
        Then 'Checkout' page should be displayed

