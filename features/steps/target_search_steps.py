from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# Updated code to include Behave variables

@given('Open target main page')
def open_main(context):
   context.driver.get('https://www.target.com/')


@when('Search for {search_word}')
def search_product(context, search_word):
    context.driver.find_element(By.CSS_SELECTOR, "#search").send_keys({search_word})
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(10)

@then('Verify search worked for {search_word}')
def verify_search_results(context, search_word):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
    assert search_word in actual_text, f"Error, expected {search_word} not in actual {actual_text}"