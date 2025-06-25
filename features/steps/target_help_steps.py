from behave import given, when, then

@given('Open Help page for Returns')
def open_help_page(context):
    context.app.target_help_page.open_help()



@when('Select Help topic {value}')
def select_help_topic(context, value):
    context.app.target_help_page.select_dd(value)


@then('Verify help Current {expected_header_text} page opens')
def verify_help_page_opens(context, expected_header_text):
    context.app.target_help_page.verify_header_text(expected_header_text)
