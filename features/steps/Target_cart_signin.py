from selenium.webdriver.common.by import By

from behave import given, when, then
from time import sleep



#@given('Open target main page')
#def open_main_page(context):
#    context.app.Main_page.open_main()

@when('User clicks Cart icn')
def click_cart_icn(context):
    context.app.header.click_cart_btn()

@then('Cart shows empty')
def check_cart_empty(context):
    context.app.Cart_page.verify_empty_cart("Your cart is empty")

#    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='styles_ndsHeading']").text
#    assert 'Your cart is empty' in actual_text


#@when('User clicks account')
#def click_account(context):
#    context.driver.find_element(By.CSS_SELECTOR, "#account-sign-in").click()
#    sleep(5)

#@when('User clicks sign in')
#def click_sign_in(context):
#    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
#    sleep(5)
#@then('Sign in page displays')
#def check_sign_in_page(context):
#    signin_text = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='styles_ndsHeading']").text
#    assert 'Sign in or create account' in signin_text
