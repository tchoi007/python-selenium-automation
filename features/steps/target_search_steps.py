from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
# Updated code to include Behave variables
product_text=(By.CSS_SELECTOR,"span.h-text-bs.h-display-flex")

@given('Open target main page')
def open_main(context):
   context.driver.get('https://www.target.com/')


@when('Search for {search_word}')
def search_product(context, search_word):
    context.driver.find_element(By.CSS_SELECTOR, "#search").send_keys({search_word})
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(15) #have to leave sleep here because of shared search word functionality
#    context.driver.wait.until(EC.visibility_of_element_located(product_text),message=f'{search_word} was not visible')

@then('Verify search worked for {search_word}')
def verify_search_results(context, search_word):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
    assert search_word in actual_text, f"Error, expected {search_word} not in actual {actual_text}"