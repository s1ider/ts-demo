from behave import given, when, then, step

import support.pages as pages
import support.ui as ui


@given("I am on '{page}' page")
def step(context, page):
    pages = __import__('support.pages', fromlist=[str(page.lower())])
    pages_class = getattr(pages, page)
    pages_class(context).open()


@when("Enter text '{text}' to field '{field}'")
def step(context, text, field):
    ui.Input(context, field).set_value(text)

@when("Buy ticket #{option:d}")
def step(context, option):
    pages.Landing(context).buy_ticket(option)

@when("Submit form")
def step(context):
    if context.table:
        for row in context.table:
            ui.Input(context, row['label']).set_value(row['value'])
    ui.SubmitButton(context).click()

@then("Validation error message for '{label}' should be displayed")
def step(context, label):
    assert ui.Input(context, label).is_invalid

@then("'{page}' page should be displayed")
def step(context, page):
    pages = __import__('support.pages', fromlist=[str(page.lower())])
    pages_class = getattr(pages, page)
    assert pages_class(context).is_displayed

@then("Price should be '{price:d}'")
def step(context, price):
    assert pages.Registration(context).price == price
