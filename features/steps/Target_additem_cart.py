from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
add_cart2 = (By.CSS_SELECTOR, '[data-test="orderPickupButton"]')
cart_icon = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')
cart_amount = (By.CSS_SELECTOR, '[data-test="cartItem-deleteBtn"]')

@when ('click product title')
def click_title_product(context):
    context.driver.find_element(By.CSS_SELECTOR, '[title*="Orange LED Flashlight Orange - Embark"]').click()

#    sleep(10)

    context.driver.wait.until(EC.visibility_of_element_located(add_cart2))

@when ('click add to cart')
def click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="orderPickupButton"]').click()

@when('click close')
def click_close(context):
    context.driver.find_element(By.CSS_SELECTOR, '[aria-label="close"]').click()

#    sleep(5)
    context.driver.wait.until(EC.element_to_be_clickable(cart_icon))

@when('User clicks Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
#    sleep(5)
    context.driver.wait.until(EC.presence_of_element_located(cart_amount))

@then('verify {number_in_cart} item in cart')
def verify_cart_quantity(context, number_in_cart):
    cart_quantity = context.driver.find_elements(By.CSS_SELECTOR, '[data-test="cartItem-deleteBtn"]')
    assert len(cart_quantity) == int(number_in_cart), f"Expected {number_in_cart} items in cart, got {len(cart_quantity)}"
