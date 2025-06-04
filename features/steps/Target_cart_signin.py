from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_main_page(context):
    context.driver.get("https://www.target.com/")

@when('User clicks Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
    sleep(5)
@then('Cart shows empty')
def check_cart_empty(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='styles_ndsHeading']").text
    assert 'Your cart is empty' in actual_text


@when('User clicks account')
def click_account(context):
    context.driver.find_element(By.CSS_SELECTOR, "#account-sign-in").click()
    sleep(5)

@when('User clicks sign in')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    sleep(5)
@then('Sign in page displays')
def check_sign_in_page(context):
    signin_text = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='styles_ndsHeading']").text
    assert 'Sign in or create account' in signin_text
