from pages.Base_page import Page
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

from pages.Sign_in_page import Signin


@given("Open sign in page")
def open_sign_in_page(context):
    context.app.Sign_in_page.open_sign_in_page()


@when('Store original window')
def store_window(context):
    context.original_window = context.app.Sign_in_page.get_current_window_id()



@when('Click on Target terms and conditions link')
def click_target_terms_and_conditions(context):
    context.app.Sign_in_page.click_terms_and_conditions()

@when('Switch to the newly opened window')
def switch_to_newly_opened_window(context):
    context.app.Base_page.switch_to_new_window()

@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page(context):
    context.app.terms_and_conditions_page.verify_terms_condition()

@then('User can close new window and switch back to original')
def user_close_new_window(context):
    context.app.Base_page.close_window()
    context.app.Base_page.switch_to_window_by_id(context.original_window)