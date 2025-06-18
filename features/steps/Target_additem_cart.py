from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
add_cart2 = (By.CSS_SELECTOR, '[data-test="orderPickupButton"]')
cart_icon = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')
cart_amount = (By.CSS_SELECTOR, '[data-test="cartItem-deleteBtn"]')

@when ('click product title')
def click_title_product(context):
    context.app.Search_results_page.click_product_title()

@when ('click add to cart')
def click_add_to_cart(context):
    context.app.Search_results_page.click_add_to_cart()

@when('click close')
def click_close(context):
    context.app.Search_results_page.click_close_popup()

@then('verify {number_in_cart} item in cart')
def verify_cart_quantity(context, number_in_cart):
    context.app.Cart_page.verify_cart_quantity(number_in_cart)



#@then('verify {number_in_cart} item in cart')
#def verify_cart_quantity(context, number_in_cart):
#    cart_quantity = context.driver.find_elements(By.CSS_SELECTOR, '[data-test="cartItem-deleteBtn"]')
#    assert len(cart_quantity) == int(number_in_cart), f"Expected {number_in_cart} items in cart, got {len(cart_quantity)}"
