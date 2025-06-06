from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('User opens target circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')

@then('Verify there are {number} benefits')
def check_benefits(context, number):
    links = context.driver.find_elements(By.CSS_SELECTOR, '.cell-item-content')
    assert len(links) == int(number), f'Expected {number} links, got {len(links)}'