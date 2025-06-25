from time import sleep
from behave import given, when, then


@when('User clicks account')
def click_account_btn(context):
    context.app.header.click_account_btn()

@when('User clicks sign in')
def click_sign_in_btn(context):
    context.app.header.click_sign_in()

@then("Sign in page displays {signin_text}")
def sign_in_page_displays(context, signin_text):
    context.app.Sign_in_page.sign_in_text(signin_text)


@when("enter correct email")
def enter_correct_email(context):
    context.app.Sign_in_page.enter_email()

@when("click continue")
def click_continue(context):
    context.app.Sign_in_page.click_continue_btn()


@when("enter incorrect password")
def enter_incorrect_password(context):
    context.app.Sign_in_page.enter_password_field()



@then("Verify password text is {error_text}")
def verify_invalid_password_text(context, error_text):
    context.app.Sign_in_page.verify_incorrect_password(error_text)
