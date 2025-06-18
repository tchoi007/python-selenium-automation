from pages.Base_page import Page
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

@when('User clicks account')
def click_account_btn(context):
    context.app.header.click_account_btn()

@when('User clicks sign in')
def click_sign_in_btn(context):
    context.app.header.click_sign_in()

@then("Sign in page displays {signin_text}")
def sign_in_page_displays(context, signin_text):
    context.app.Sign_in_page.sign_in_text(signin_text)
