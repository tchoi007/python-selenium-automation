from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@when ('click product title')
def click_title_product(context):
    context.driver.find_element(By.CSS_SELECTOR, '[title*="Orange LED Flashlight Orange"]').click()
    sleep(10)


@when ('click add to cart')
def click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="orderPickupButton"]').click()

@when('click close')
def click_close(context):
    context.driver.find_element(By.CSS_SELECTOR, '[aria-label="close"]').click()

    sleep(5)

@when('User clicks Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
    sleep(5)


@then('verify {number_in_cart} item in cart')
def verify_cart_quantity(context, number_in_cart):
    cart_quantity = context.driver.find_elements(By.CSS_SELECTOR, '[data-test="cartItem-deleteBtn"]')
    assert len(cart_quantity) == int(number_in_cart), f"Expected {number_in_cart} items in cart, got {len(cart_quantity)}"
